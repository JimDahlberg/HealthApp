from math import sqrt
import Server
import random

class Functions():
    def __init__(self):
        self._sql_cursor = Server.Server()
        self._insert_statement = {}
        self._insert_statement['login'] = "INSERT INTO login Values "
        self._insert_statement['account_information'] = "INSERT INTO AccountInformation Values "
        self._insert_statement['daily_intake'] = "INSERT INTO DailyIntake Values "
        self._insert_statement['food_item'] = "INSERT INTO FoodItem Values "

    def add_food_item_to_db(
        self,
        food_name = "\'Unspecified\'", 
        kcal = 0, 
        fat = 0,
        carbs = 0,
        protein = 0
        ):
            food_item_ID = random.randint(0,1000)
            food_item_values = f"({food_item_ID},{food_name},{float(kcal)},{float(fat)},{float(carbs)},{float(protein)})"
            self._sql_cursor.execute(self._insert_statement['food_item'] + food_item_values)
            self._sql_cursor.commit()

    def change_goal_weight(
        self,
        login_id,
        new_goal_weight
    ):
        statement_update_goal_weight = f"UPDATE AccountInformation SET GoalWeight={new_goal_weight} WHERE loginID=\'{login_id}\'"
        self._sql_cursor.execute(statement_update_goal_weight)
        self._sql_cursor.commit()

    def update_weight(
        self,
        login_id,
        new_current_weight
    ):
        statement_update_current_weight = f"UPDATE AccountInformation SET Currentweight={new_current_weight} WHERE loginID={login_id}"
        self._sql_cursor.execute(statement_update_current_weight)
        self._sql_cursor.commit()

    def update_goal_weight_type(self):
        """Placeholder"""
        pass

    def add_consumed_item(
        self,
        login_id,
        item_name = "",
        amount = 0):

        statement_output_food_item_info = f"SELECT ItemName,kcal,Fat,Carbs,Protein FROM FoodItem WHERE ItemName=\'{item_name}\'"
        self._sql_cursor.execute(statement_output_food_item_info)
        result_set = self._sql_cursor.fetchall()

        values_view = (result_set[0].values())
        value_iterator = iter(values_view)
        ItemName_value = next(value_iterator)
        kcal_value = (float(next(value_iterator)) * amount * 0.01 )
        fat_value = (float(next(value_iterator)) * amount * 0.01 )
        carbs_value = (float(next(value_iterator)) * amount * 0.01 )
        protein_value = (float(next(value_iterator)) * amount * 0.01 )

        statement_output_account_ID = f"SELECT AccountID FROM AccountInformation WHERE loginID={login_id}"
        self._sql_cursor.execute(statement_output_account_ID)
        values_view_account_information = (result_set[0].values())
        value_iterator_account_information = iter(values_view_account_information)
        AccountID_value = next(value_iterator_account_information)

        Intake_ID = random.randint(0,10000)
        daily_intake_values = f"({Intake_ID},\'{ItemName_value}\',{kcal_value},{fat_value},{carbs_value},{protein_value},{AccountID_value})"
        self._sql_cursor.execute(self._insert_statement['daily intake'] + daily_intake_values)
        self._sql_cursor.commit()

    def calculate_daily_calorie_intake(self, weight, goal):
        """Input: nuvarande vikt och vilken typ av mål (1,2 eller 3)
        Output: dagliga kaloriemål """
        caloryintake = 0
        if goal == 1:
        ###för att öka i vikt###
            caloryintake = int(weight * 2.20462262 * 20)
        ###för att behålla vikt
        elif goal == 2:
            caloryintake = int(weight * 2.20462262 * 15) 
        ###för att gå ner i vikt
        elif goal == 3:
            caloryintake = int((weight * 2.20462262) - 10) * 12
        
        return caloryintake

    def viewstatus(
        self,
        login_id = ""):
        statement_output_account_ID = f"SELECT AccountID,DailyCalorieIntakeGoal FROM AccountInformation WHERE loginID={login_id}"
        self._sql_cursor.execute(statement_output_account_ID)
        result_set = self._sql_cursor.fetchall()
        values_view_account_information = (result_set[0].values())
        value_iterator_account_information = iter(values_view_account_information)
        AccountID_value = next(value_iterator_account_information)
        daily_calorie_goal = next(value_iterator_account_information)

        statement_output_calorie_total_day = f"SELECT SUM(Dailykcal), SUM(DailyFat), SUM(DailyCarbs), SUM(DailyProtein) FROM DailyIntake WHERE AccountID={login_id}"
        userid_test_login_value = (AccountID_value,)
        self._sql_cursor.execute(statement_output_calorie_total_day,userid_test_login_value)
        values_view = (result_set[0].values())
        value_iterator = iter(values_view)
        sum_calorie_day_value = next(value_iterator)
        sum_fat_day_value = next(value_iterator)
        sum_carbs_day_value = next(value_iterator)
        sum_protein_day_value = next(value_iterator)     

        return [daily_calorie_goal,sum_calorie_day_value,sum_fat_day_value,sum_carbs_day_value,sum_protein_day_value]   

    def remaining_calories(self):
        """Placeholder"""
        pass

    def sign_up(
        self,
        username,
        password,
        gender,
        current_weigth,
        weigth_goal
    ):
        self._sql_cursor.execute(f"SELECT username FROM login WHERE username = \'{username}\'")
        try:
            username_check = self._sql_cursor.fetchall()[0]
        except IndexError:
                self._sql_cursor.execute(self._insert_statement['login'] + f"({random.randint(0,10000)}, '{username}','{password}')")
                self._sql_cursor.commit()
                return "Succes"
        else:
                return "usrError"

    def login(
        self,
        username = "",
        password = ""):
        self._sql_cursor.execute(f"SELECT loginID,username,password From login WHERE username=\'{username}\'")
        try:
            login_info = self._sql_cursor.fetchall()[0]
        except IndexError:
            return "usrError"
        else:
            if login_info['username'] != username:
                return "usrError"
            if login_info['password'] != password:
                return "pwError"
            else:
                return int(login_info['loginID'])     

    def get_username(
        self, 
        user_id):
        self._sql_cursor.execute(f"Select username FROM login WHERE loginID = {user_id}")
        return self._sql_cursor.fetchall()[0]['username']

    def get_list_of_food(
        self
    ):
        self._sql_cursor.execute(f"Select * FROM FoodItem")
        return self._sql_cursor.fetchall()

if __name__ == "__main__":
    test = Functions()
    test.change_goal_weight(2037, 50.0)