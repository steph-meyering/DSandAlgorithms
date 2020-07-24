class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        for email in emails:
            local_name = False
            temp_name = ""
            domain = False;
            for i, c in enumerate(email):
                if not local_name:
                    if c == "+":
                        local_name = temp_name
                    elif c == ".":
                        continue
                    elif c == "@":
                        domain = email[i:]
                        local_name = temp_name
                    else:
                        temp_name += c
                else:
                    if c == "@":
                        domain = email[i:]
                    if domain:
                        local_name += domain
                        unique_emails.add(local_name)
                        break
        return len(unique_emails)