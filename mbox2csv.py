import pandas as pd # converting to csv
import mailbox # mbox parsing
from dateutil import parser # string to datetime
import pytz # timezone conversions




def main(file):
    
    print("Starting message collection")
    messages = [message for message in mailbox.mbox(file)]
    print("Done collecting all messages")
    content = {"UTC_time_str":   [],
               "UTC_time_dt":    [],
               "local_time_str": [],
               "local_time_dt":  [],
               "Sender_email":   [],
               "Subject":        [],
               "Content":        [],
               }

    i = 0
    for message in messages:
        print(f"Parsing message {i}")
        

        print("\tChecking header")
        for h in message._headers:
            if h[0] == "Date":
                #TODO: sometimes not received in UTC
                UTC_time_str = h[1]
                content["UTC_time_str"].append(UTC_time_str)
            elif h[0] == "Received":
                # 'Received' entries can appear twice
                # Assuming theyre both the same and the last part of the string
                split_newline   = h[1].split("\n        ")[-1]
                split_semicolon = split_newline.split("; ")[-1]
                if len(content["local_time_str"]) == i:
                    # if local time has NOT been added
                    content["local_time_str"].append(split_semicolon)
                else:
                    print("\t\tRedundant local time spotted")
            elif h[0] == "From":
                sender = h[1]
                content["Sender_email"].append(sender)
            elif h[0] == "Subject":
                subject = h[1]
                content["Subject"].append(subject)

        # filling in missing entries if not encountered
        expected_lengths = [i+1, i, i+1 , i , i+1, i+1 , i]
        for idx, col in enumerate(content):
            if len(content[col]) < expected_lengths[idx]:
                content[col].append(None)

        # datetime parsing
        print("\tFormatting datetime")
        time_format = "%Y-%m-%d %H:%M:%S"
        for tz in ["UTC","local"]:
            str_col = f"{tz}_time_str"
            dt_col = f"{tz}_time_dt"
            ith_time_str = content[str_col][i]
            if ith_time_str is not None:
                #print("\t",str_col,ith_time_str)
                if tz == "UTC":
                    # Enforcing UTC time
                    converted_tz = parser.parse(ith_time_str).astimezone(pytz.utc)
                else:
                    # Enforcing West coast time, PST or PDT
                    converted_tz = parser.parse(ith_time_str).astimezone(pytz.timezone("America/Los_Angeles"))
                time_strftime = converted_tz.strftime(time_format)
                content[dt_col].append(time_strftime)
            else:
                content[dt_col].append(None)

        # content["Sender_email"].append(content["Sender_email"]) # here for completeness
        # content["Subject"].append(content["Subject"])           # no processing needed
        content["Content"].append(message._payload)

        calculated_lengths = [len(content[col]) for col in content]
        assert calculated_lengths == [i+1]*7, f"Missing attributes, calculated={calculated_lengths}"
        i += 1

    print("Done parsing. Saving to csv")
    emails = pd.DataFrame(content)
    # pd.DataFrame(content).to_csv("internet_emails.csv")

    #theory11 task
    is_theory11 = emails["Subject"].str.contains("theory11")
    is_contest  = emails["Subject"].str.contains("ontest") #Contest
    emails[is_theory11 & is_contest][["UTC_time_dt","local_time_dt","Sender_email","Subject"]].to_csv("theory11_contest.csv")

if __name__=="__main__":

    mbox_file = "All mail Including Spam and Trash.mbox"
    main(mbox_file)



