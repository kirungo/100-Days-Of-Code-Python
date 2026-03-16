# Life in Weeks

def life_in_weeks(current_age):
    life_span = 90
    years_remaining = life_span - current_age
    weeks_left = years_remaining * 52
    print(f"You have {weeks_left} weeks left.")

life_in_weeks(56)