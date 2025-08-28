import utils
import re

def scan_log_file(docu):
    if not utils.exist_this_doc(docu):return None
    with open(docu,'r',encoding='utf-8',newline=""):
        pass

def get_data(log_row,simbol):
    lim_one=log_row.find(simbol[0])
    lim_two=log_row.find(simbol[1])
    if lim_one == -1 or lim_two == -1:
        return False
    return log_row[lim_one+1:lim_two]

def get_status_size(log_row:str) -> list:
    sts_sz=log_row.split("\"")[2].strip().split()
    return sts_sz

def get_tokens(log:str)->dict:
    partes = log.split(" ")
    ip = partes[0]
    user = partes[1]
    indent = partes[2] if len(partes) > 2 else None
    return {'ip': ip, 'user': user, 'indent': indent}

def get_req(log_row:str)->dict:
    parts = log_row.split("\"")
    return {"referrer":parts[3],"user_agent":parts[5]}

def get_request_regex(log_row):
    match=re.search(r'"([A-Z]+ \/[^ ]+ HTTP\/[0-9.]+)"', log_row)
    return match.group(1) if match else False

def get_req(log_row):
    parts = log_row.split("\"")
    if len(parts) < 2:
        return False
    request=parts[1].strip()
    verbs=('GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'OPTIONS')
    if request.startswith(verbs):
        return request
