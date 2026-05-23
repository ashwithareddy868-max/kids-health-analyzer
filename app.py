import gradio as gr

FOOD_DATABASE = {
    "apple": {"calories": 52, "protein": 0.3, "calcium": 6, "vitaminD": 0, "iron": 0.1, "vitaminC": 4.6, "vitaminA": 3, "vitaminB12": 0, "zinc": 0.04, "magnesium": 5, "potassium": 107, "folate": 3, "fiber": 2.4, "fat": 0.2, "carbs": 14, "sugar": 10, "category": "fruit", "junk_risk": 0},
    "banana": {"calories": 89, "protein": 1.1, "calcium": 5, "vitaminD": 0, "iron": 0.3, "vitaminC": 8.7, "vitaminA": 3, "vitaminB12": 0, "zinc": 0.15, "magnesium": 27, "potassium": 358, "folate": 20, "fiber": 2.6, "fat": 0.3, "carbs": 23, "sugar": 12, "category": "fruit", "junk_risk": 0},
    "orange": {"calories": 47, "protein": 0.9, "calcium": 40, "vitaminD": 0, "iron": 0.1, "vitaminC": 53, "vitaminA": 11, "vitaminB12": 0, "zinc": 0.07, "magnesium": 10, "potassium": 181, "folate": 30, "fiber": 2.4, "fat": 0.1, "carbs": 12, "sugar": 9, "category": "fruit", "junk_risk": 0},
    "spinach": {"calories": 23, "protein": 2.9, "calcium": 99, "vitaminD": 0, "iron": 2.7, "vitaminC": 28, "vitaminA": 469, "vitaminB12": 0, "zinc": 0.53, "magnesium": 79, "potassium": 558, "folate": 194, "fiber": 2.2, "fat": 0.4, "carbs": 3.6, "sugar": 0.4, "category": "vegetable", "junk_risk": 0},
    "carrot": {"calories": 41, "protein": 0.9, "calcium": 33, "vitaminD": 0, "iron": 0.3, "vitaminC": 5.9, "vitaminA": 835, "vitaminB12": 0, "zinc": 0.24, "magnesium": 12, "potassium": 320, "folate": 19, "fiber": 2.8, "fat": 0.2, "carbs": 10, "sugar": 5, "category": "vegetable", "junk_risk": 0},
    "broccoli": {"calories": 34, "protein": 2.8, "calcium": 47, "vitaminD": 0, "iron": 0.7, "vitaminC": 89, "vitaminA": 31, "vitaminB12": 0, "zinc": 0.41, "magnesium": 21, "potassium": 316, "folate": 63, "fiber": 2.6, "fat": 0.4, "carbs": 7, "sugar": 1.7, "category": "vegetable", "junk_risk": 0},
    "chicken": {"calories": 165, "protein": 31, "calcium": 15, "vitaminD": 0.1, "iron": 1.0, "vitaminC": 0, "vitaminA": 6, "vitaminB12": 0.3, "zinc": 1.0, "magnesium": 29, "potassium": 256, "folate": 4, "fiber": 0, "fat": 3.6, "carbs": 0, "sugar": 0, "category": "protein", "junk_risk": 0},
    "egg": {"calories": 155, "protein": 13, "calcium": 56, "vitaminD": 2.0, "iron": 1.8, "vitaminC": 0, "vitaminA": 149, "vitaminB12": 1.11, "zinc": 1.29, "magnesium": 12, "potassium": 138, "folate": 47, "fiber": 0, "fat": 11, "carbs": 1.1, "sugar": 1.1, "category": "protein", "junk_risk": 0},
    "fish": {"calories": 136, "protein": 26, "calcium": 12, "vitaminD": 9.0, "iron": 0.9, "vitaminC": 0, "vitaminA": 15, "vitaminB12": 3.0, "zinc": 0.64, "magnesium": 32, "potassium": 502, "folate": 10, "fiber": 0, "fat": 3.0, "carbs": 0, "sugar": 0, "category": "protein", "junk_risk": 0},
    "milk": {"calories": 61, "protein": 3.2, "calcium": 113, "vitaminD": 1.2, "iron": 0.03, "vitaminC": 0, "vitaminA": 46, "vitaminB12": 0.45, "zinc": 0.4, "magnesium": 11, "potassium": 150, "folate": 5, "fiber": 0, "fat": 3.3, "carbs": 4.8, "sugar": 5.1, "category": "dairy", "junk_risk": 0},
    "cheese": {"calories": 402, "protein": 25, "calcium": 721, "vitaminD": 0.6, "iron": 0.7, "vitaminC": 0, "vitaminA": 265, "vitaminB12": 1.1, "zinc": 3.1, "magnesium": 28, "potassium": 98, "folate": 18, "fiber": 0, "fat": 33, "carbs": 1.3, "sugar": 0.5, "category": "dairy", "junk_risk": 0},
    "yogurt": {"calories": 59, "protein": 3.5, "calcium": 110, "vitaminD": 0.1, "iron": 0.1, "vitaminC": 0.5, "vitaminA": 26, "vitaminB12": 0.37, "zinc": 0.5, "magnesium": 12, "potassium": 141, "folate": 11, "fiber": 0, "fat": 3.3, "carbs": 3.6, "sugar": 3.2, "category": "dairy", "junk_risk": 0},
    "rice": {"calories": 130, "protein": 2.7, "calcium": 10, "vitaminD": 0, "iron": 0.2, "vitaminC": 0, "vitaminA": 0, "vitaminB12": 0, "zinc": 0.49, "magnesium": 12, "potassium": 35, "folate": 3, "fiber": 0.4, "fat": 0.3, "carbs": 28, "sugar": 0, "category": "grain", "junk_risk": 0},
    "bread": {"calories": 265, "protein": 9.0, "calcium": 182, "vitaminD": 0, "iron": 3.6, "vitaminC": 0, "vitaminA": 0, "vitaminB12": 0, "zinc": 0.7, "magnesium": 23, "potassium": 115, "folate": 29, "fiber": 2.7, "fat": 3.2, "carbs": 49, "sugar": 5, "category": "grain", "junk_risk": 0},
    "oats": {"calories": 389, "protein": 17, "calcium": 54, "vitaminD": 0, "iron": 4.7, "vitaminC": 0, "vitaminA": 0, "vitaminB12": 0, "zinc": 3.97, "magnesium": 177, "potassium": 429, "folate": 56, "fiber": 10.6, "fat": 6.9, "carbs": 66, "sugar": 0, "category": "grain", "junk_risk": 0},
    "burger": {"calories": 295, "protein": 17, "calcium": 100, "vitaminD": 0.1, "iron": 2.7, "vitaminC": 1, "vitaminA": 15, "vitaminB12": 1.2, "zinc": 3.5, "magnesium": 23, "potassium": 280, "folate": 30, "fiber": 1.3, "fat": 14, "carbs": 24, "sugar": 5, "category": "junk", "junk_risk": 9},
    "pizza": {"calories": 266, "protein": 11, "calcium": 200, "vitaminD": 0.2, "iron": 1.75, "vitaminC": 2, "vitaminA": 50, "vitaminB12": 0.5, "zinc": 1.5, "magnesium": 20, "potassium": 200, "folate": 25, "fiber": 1.8, "fat": 10, "carbs": 33, "sugar": 3.6, "category": "junk", "junk_risk": 8},
    "chips": {"calories": 536, "protein": 7.0, "calcium": 40, "vitaminD": 0, "iron": 1.7, "vitaminC": 22, "vitaminA": 2, "vitaminB12": 0, "zinc": 0.9, "magnesium": 50, "potassium": 1642, "folate": 22, "fiber": 4.4, "fat": 35, "carbs": 53, "sugar": 0.4, "category": "junk", "junk_risk": 9},
    "candy": {"calories": 394, "protein": 0, "calcium": 2, "vitaminD": 0, "iron": 0.1, "vitaminC": 0, "vitaminA": 0, "vitaminB12": 0, "zinc": 0, "magnesium": 1, "potassium": 5, "folate": 0, "fiber": 0, "fat": 0, "carbs": 98, "sugar": 82, "category": "junk", "junk_risk": 10},
    "soda": {"calories": 41, "protein": 0, "calcium": 6, "vitaminD": 0, "iron": 0.1, "vitaminC": 0, "vitaminA": 0, "vitaminB12": 0, "zinc": 0, "magnesium": 3, "potassium": 4, "folate": 0, "fiber": 0, "fat": 0, "carbs": 10, "sugar": 10, "category": "junk", "junk_risk": 10},
    "almonds": {"calories": 579, "protein": 21, "calcium": 264, "vitaminD": 0, "iron": 3.7, "vitaminC": 0, "vitaminA": 0, "vitaminB12": 0, "zinc": 3.12, "magnesium": 270, "potassium": 733, "folate": 44, "fiber": 12.5, "fat": 50, "carbs": 22, "sugar": 4.4, "category": "nuts", "junk_risk": 0},
    "peanuts": {"calories": 567, "protein": 26, "calcium": 92, "vitaminD": 0, "iron": 4.6, "vitaminC": 0, "vitaminA": 0, "vitaminB12": 0, "zinc": 3.27, "magnesium": 168, "potassium": 705, "folate": 240, "fiber": 8.5, "fat": 49, "carbs": 16, "sugar": 4.7, "category": "nuts", "junk_risk": 0},
}

WHO_STANDARDS = {
    "1-3":  {"calories": 1000, "protein": 13, "calcium": 700, "vitaminD": 15, "iron": 7, "vitaminC": 15, "vitaminA": 300, "vitaminB12": 0.9, "zinc": 3, "magnesium": 80, "potassium": 2000, "folate": 150, "fiber": 14},
    "4-6":  {"calories": 1200, "protein": 20, "calcium": 1000, "vitaminD": 15, "iron": 10, "vitaminC": 25, "vitaminA": 400, "vitaminB12": 1.2, "zinc": 5, "magnesium": 130, "potassium": 2300, "folate": 200, "fiber": 20},
    "7-10": {"calories": 1600, "protein": 28, "calcium": 1000, "vitaminD": 15, "iron": 10, "vitaminC": 45, "vitaminA": 500, "vitaminB12": 1.8, "zinc": 7, "magnesium": 200, "potassium": 2500, "folate": 250, "fiber": 25},
    "11-14":{"calories": 2000, "protein": 45, "calcium": 1300, "vitaminD": 15, "iron": 12, "vitaminC": 65, "vitaminA": 600, "vitaminB12": 2.4, "zinc": 9, "magnesium": 300, "potassium": 3000, "folate": 300, "fiber": 31},
}

SLEEP_STANDARDS = {"1-3": "11-14 hours", "4-6": "10-13 hours", "7-10": "9-11 hours", "11-14": "8-10 hours"}
EXERCISE_STANDARDS = {"1-3": "180 mins active play", "4-6": "60 mins activity", "7-10": "60 mins moderate-vigorous", "11-14": "60 mins vigorous"}
SCREEN_STANDARDS = {"1-3": "Max 1 hour", "4-6": "Max 1-2 hours", "7-10": "Max 2 hours", "11-14": "Max 2-3 hours"}
STUDY_STANDARDS = {"1-3": "20-30 mins with breaks", "4-6": "30-45 mins", "7-10": "1-2 hours + reading", "11-14": "2-3 hours + reading"}

def get_age_group(age):
    if age <= 3: return "1-3"
    elif age <= 6: return "4-6"
    elif age <= 10: return "7-10"
    else: return "11-14"

def calculate_bmi(weight, height):
    if weight <= 0 or height <= 0: return 0, "Not calculated"
    bmi = round(weight / ((height/100) ** 2), 1)
    if bmi < 14: status = "UNDERWEIGHT - Needs more nutrition!"
    elif bmi < 18: status = "HEALTHY WEIGHT - Great!"
    elif bmi < 22: status = "SLIGHTLY OVERWEIGHT - Monitor diet"
    else: status = "OVERWEIGHT - Consult a doctor"
    return bmi, status

def analyze_child_health(child_name, age, weight, height, food1, qty1, food2, qty2, food3, qty3, food4, qty4, food5, qty5, food6, qty6, sleep_hours, exercise_mins, screen_hours, study_hours):
    age = int(age)
    age_group = get_age_group(age)
    standards = WHO_STANDARDS[age_group]
    bmi, bmi_status = calculate_bmi(float(weight), float(height))
    totals = {k: 0 for k in standards}
    totals["fat"] = 0
    totals["carbs"] = 0
    totals["sugar"] = 0
    foods_eaten = []
    junk_foods = []
    total_junk_risk = 0
    for food, qty in [(food1,qty1),(food2,qty2),(food3,qty3),(food4,qty4),(food5,qty5),(food6,qty6)]:
        food = food.lower().strip()
        if food and qty and food in FOOD_DATABASE:
            factor = float(qty)/100
            item = FOOD_DATABASE[food]
            for nutrient in totals:
                if nutrient in item: totals[nutrient] += item[nutrient] * factor
            foods_eaten.append(food + "(" + str(qty) + "g)")
            if item["junk_risk"] >= 7:
                junk_foods.append(food)
                total_junk_risk += item["junk_risk"]
    report = "=" * 50 + "\n"
    report += "   CHILD HEALTH AND NUTRITION REPORT\n"
    report += "=" * 50 + "\n"
    report += "Child: " + child_name + " | Age: " + str(age) + " yrs | Group: " + age_group + "\n"
    report += "Weight: " + str(weight) + "kg | Height: " + str(height) + "cm | BMI: " + str(bmi) + "\n"
    report += "BMI Status: " + bmi_status + "\n\n"
    report += "FOODS TODAY: " + (", ".join(foods_eaten) if foods_eaten else "None entered") + "\n\n"
    if junk_foods:
        report += "JUNK FOOD WARNING:\n"
        report += "Detected: " + ", ".join(junk_foods) + "\n"
        if total_junk_risk > 20: report += "CRITICAL: Way too much junk food! Risks: obesity, diabetes, tooth decay!\n\n"
        else: report += "WARNING: Limit junk food to once a week!\n\n"
    nutrients_display = [("calories","Calories","kcal"),("protein","Protein","g"),("calcium","Calcium","mg"),("vitaminD","Vitamin D","mcg"),("iron","Iron","mg"),("vitaminC","Vitamin C","mg"),("vitaminA","Vitamin A","mcg"),("vitaminB12","Vitamin B12","mcg"),("zinc","Zinc","mg"),("magnesium","Magnesium","mg"),("potassium","Potassium","mg"),("folate","Folate","mcg"),("fiber","Fiber","g")]
    report += "NUTRITION ANALYSIS:\n" + "-"*40 + "\n"
    deficiencies = []
    critical = []
    good = []
    for key, name, unit in nutrients_display:
        got = round(totals[key], 1)
        needed = standards[key]
        pct = round((got/needed)*100, 1)
        if pct >= 80: status = "GOOD"; good.append(name)
        elif pct >= 50: status = "LOW"; deficiencies.append(name)
        else: status = "CRITICAL"; critical.append(name)
        report += name + ": " + str(got) + unit + "/" + str(needed) + unit + " (" + str(pct) + "%) - " + status + "\n"
    report += "\nLIFESTYLE:\n" + "-"*40 + "\n"
    report += "Sleep: " + str(sleep_hours) + " hrs (Recommended: " + SLEEP_STANDARDS[age_group] + ")\n"
    report += "Exercise: " + str(exercise_mins) + " mins (Recommended: " + EXERCISE_STANDARDS[age_group] + ")\n"
    report += "Screen time: " + str(screen_hours) + " hrs (Recommended: " + SCREEN_STANDARDS[age_group] + ")\n"
    report += "Study: " + str(study_hours) + " hrs (Recommended: " + STUDY_STANDARDS[age_group] + ")\n\n"
    report += "WARNINGS:\n" + "-"*40 + "\n"
    if float(sleep_hours) < 9: report += "NOT ENOUGH SLEEP! Affects growth and concentration!\n"
    else: report += "Sleep: Good!\n"
    if float(exercise_mins) < 60: report += "NOT ENOUGH EXERCISE! Vital for bone and muscle growth!\n"
    else: report += "Exercise: Good!\n"
    if float(screen_hours) > 2: report += "TOO MUCH SCREEN TIME! Causes eye strain and poor sleep!\n"
    else: report += "Screen time: Good!\n"
    report += "\nDOCTOR RECOMMENDATIONS:\n" + "-"*40 + "\n"
    if critical:
        report += "URGENT - Very low in: " + ", ".join(critical) + "\n"
        if "Calcium" in critical: report += "- Give milk, cheese, yogurt for strong bones!\n"
        if "Iron" in critical: report += "- Give spinach, eggs, chicken - prevents anemia!\n"
        if "Vitamin D" in critical: report += "- 30 mins sunlight + fish and eggs daily!\n"
        if "Vitamin C" in critical: report += "- Add oranges, kiwi, broccoli every day!\n"
        if "Protein" in critical: report += "- Add eggs, chicken, lentils for growth!\n"
        if "Zinc" in critical: report += "- Add nuts, seeds - zinc boosts immunity!\n"
    if deficiencies: report += "LOW - Increase: " + ", ".join(deficiencies) + "\n"
    if good: report += "GOOD - Keep it up: " + ", ".join(good) + "\n"
    health_score = round((len(good)/len(nutrients_display))*100)
    report += "\n" + "="*50 + "\n"
    report += "OVERALL HEALTH SCORE: " + str(health_score) + "/100\n"
    if health_score >= 80: report += "EXCELLENT! Your child is very healthy!\n"
    elif health_score >= 60: report += "GOOD! Some improvements needed.\n"
    elif health_score >= 40: report += "FAIR! Please improve diet and lifestyle.\n"
    else: report += "POOR! Please consult a pediatrician!\n"
    report += "="*50 + "\n"
    return report

demo = gr.Interface(
    fn=analyze_child_health,
    inputs=[
        gr.Textbox(label="Child Name"),
        gr.Slider(minimum=1, maximum=14, step=1, label="Age (years)", value=7),
        gr.Number(label="Weight (kg)", value=25),
        gr.Number(label="Height (cm)", value=120),
        gr.Textbox(label="Food 1", placeholder="milk, egg, banana, rice, chicken, spinach, burger, pizza, chips, apple, carrot, oats"),
        gr.Number(label="Quantity 1 (grams)", value=100),
        gr.Textbox(label="Food 2", placeholder="cheese, yogurt, broccoli, almonds, peanuts"),
        gr.Number(label="Quantity 2 (grams)", value=100),
        gr.Textbox(label="Food 3", placeholder="orange, spinach, carrot, fish, lentils"),
        gr.Number(label="Quantity 3 (grams)", value=100),
        gr.Textbox(label="Food 4", placeholder="chocolate, candy, soda, burger, pizza"),
        gr.Number(label="Quantity 4 (grams)", value=100),
        gr.Textbox(label="Food 5", placeholder="fish, lentils, sweet potato, strawberry"),
        gr.Number(label="Quantity 5 (grams)", value=100),
        gr.Textbox(label="Food 6", placeholder="grapes, mango, tomato, potato, bread"),
        gr.Number(label="Quantity 6 (grams)", value=100),
        gr.Slider(minimum=0, maximum=14, step=0.5, label="Sleep Hours", value=8),
        gr.Slider(minimum=0, maximum=180, step=5, label="Exercise Minutes", value=60),
        gr.Slider(minimum=0, maximum=12, step=0.5, label="Screen Time Hours", value=2),
        gr.Slider(minimum=0, maximum=8, step=0.5, label="Study Hours", value=2),
    ],
    outputs=gr.Textbox(label="Complete Health Report", lines=50),
    title="Kids Complete Health and Nutrition Analyzer",
    description="Enter child details and food eaten today to get a doctor-level health report!"
)

demo.launch()
