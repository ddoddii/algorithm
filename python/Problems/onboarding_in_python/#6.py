#6 닉네임 설정

def solution(forms):
    names = [form[1] for form in forms]
    emails = [form[0] for form in forms]
    
    duplicate_count = count_duplicate_letters(names)
    
    duplicate_substrings = []
    for substring, count in duplicate_count.items():
        if count > 1:
            duplicate_substrings.append(substring)
    
    duplicate_emails = set()
    for substring in duplicate_substrings:
        duplicate_emails_list = [email for name, email in zip(names, emails) if substring in name]
        duplicate_emails.update(duplicate_emails_list)

    all_duplicate_emails_list = list(duplicate_emails)
    sorted_emails = sorted(all_duplicate_emails_list)
    
    return (sorted_emails)
    
    
def count_duplicate_letters(names):

    duplicate_count = {}

    for name in names:
        for i in range(len(name)-1):
            substring = name[i:i+2]
            if substring not in duplicate_count:
                duplicate_count[substring] = 1
            else:
                duplicate_count[substring] += 1
    return duplicate_count
            



forms = [ ["jm@email.com", "제이엠"], ["jason@email.com", "제이슨"], ["woniee@email.com", "워니"], ["mj@email.com", "엠제이"], ["nows@email.com", "이제엠"]]
print(solution(forms))

