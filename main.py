import constants as drom
import test1_filter
import test2_login_and_favorites
import test3_select_top20
import time 



def main():
   test1_filter.runner()
   test2_login_and_favorites.runner()
   test3_select_top20.runner()
   drom.driver.quit()
   
   
if __name__ == "__main__":
    main()
