import os
from time import time
class DatabaseAdmin:
    def __init__(self):
        self.delete_monitors_script = "/home/adamsl/selenium-headless/mcba_tests/menu_shell_scripts/delete_monitors.sh"
        self.delete_all_but_admin_script = "/home/adamsl/selenium-headless/mcba_tests/menu_shell_scripts/delete_all_but_admin.sh"
        self.delete_all_messages_script = "/home/adamsl/selenium-headless/mcba_tests/menu_shell_scripts/delete_all_messages.sh"
        self.delete_all_conversations_script = "/home/adamsl/selenium-headless/mcba_tests/menu_shell_scripts/delete_all_conversations.sh"

    def delete_monitors( self ):
        print( f"executing { self.delete_monitors_script }..." )
        os.system( self.delete_monitors_script )

    def clear_database(self):
        print("clearing the jewelry machine database...")
        os.system(self.delete_monitors_script)

    def sleep(self, seconds):
        print(f"sleeping {seconds} seconds to let that sit in...")
        time.sleep(seconds)

    def delete_all_but_admin(self):
        print("deleting all users but admin...")
        os.system(self.delete_all_but_admin_script)

    def delete_all_messages(self):
        print("deleting all messages...")
        os.system(self.delete_all_messages_script)

    def delete_all_conversations(self):
        print("deleting all conversations...")
        os.system(self.delete_all_conversations_script)
    
    def get_ready_for_test( self ):
        print( "getting ready for test..." )
        self.clear_database()
        self.delete_all_but_admin()
        self.delete_all_messages()
        self.delete_all_conversations()

# Usage
# db_admin = DatabaseAdmin()
# db_admin.clear_database()
# db_admin.sleep(10)
# db_admin.delete_all_but_admin()
# db_admin.delete_all_messages()
# db_admin.delete_all_conversations()