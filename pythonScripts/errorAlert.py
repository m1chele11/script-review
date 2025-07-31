

def parse_errors(logFile):
    with open(logFile, 'r') as f:
        lines = f.readlines()

    errors = [line for line in lines if "ERROR" in line]

    with open('error_logs.txt', 'w') as out:
        out.writelines(errors)

    if len(errors) > 5:
        print("🚨 Alert: High number of errors detected!")
    else:
        print("✅ Error count normal.")



def parse_errors2(logFile):
    with open(logFile, "r") as f:
        lines = f.readlines()
     
    errors = [line for line in lines if "ERROR" in line]

    with open('error_logs.txt', 'w') as out:
        out.writelines(errors)
    
    if len(errors) > 5:
        print("Alert high errors")
    else:
        print("errors normal")
    

if __name__ == "__main__":
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    log_path = os.path.join(script_dir, 'server.log')
    parse_errors2(log_path)