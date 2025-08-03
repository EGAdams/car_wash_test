import subprocess

def get_public_ip():
    """Get the public IP address using curl."""
    try:
        ip = subprocess.check_output(["curl", "-s", "https://api.ipify.org"], text=True).strip()
        return ip
    except subprocess.CalledProcessError as e:
        print(f"Failed to get public IP: {e}")
        return None

def check_ip_in_mysql(ip):
    """Check if the IP address exists as an email in the wp_mcba_users table."""
    if not ip:
        print("No IP provided for MySQL check.")
        return False
    try:

        query = f"SELECT * FROM wp_mcba_users WHERE email='{ip}'"
        print ( f"running query {query}... " )
        result = subprocess.check_output(["mysql", "-e", query], text=True)
        # If result contains rows other than header, return True
        lines = result.strip().splitlines()
        if len(lines) > 1:
            print ( "found it. " )
            return True
        else:
            print ( "*** ERROR: ip address: {ip} not found in wp_mcba_users table. ***" )
            return False
    except subprocess.CalledProcessError as e:
        print( f"*** ERROR: MySQL query failed: {e} ***" )
        return False

def verify_ip_user():
    ip = get_public_ip()
    if ip:
        print(f"Public IP detected: {ip}")
    else:
        print("Could not detect public IP.")
        return False
    exists = check_ip_in_mysql(ip)
    if exists:
        print(f"User with email {ip} exists in wp_mcba_users.")
    else:
        print(f"No user with email {ip} found in wp_mcba_users.")
    return exists

if __name__ == "__main__":
    verify_ip_user()