from predict import predict

print("HealthLogix Assistant")

bmi=float(input("BMI: "))
activity=int(input("Activity (0-5): "))
sleep=int(input("Sleep hours: "))
hr=int(input("Heart Rate: "))

print("\nRecommendation:")
print(predict(bmi,activity,sleep,hr))
