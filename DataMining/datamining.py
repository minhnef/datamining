import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu từ file CSV
data = pd.read_csv('Book1.csv')

# Hiển thị thông tin cơ bản về dữ liệu
print(data.info())
print(data.describe())

# Phân tích các điểm nghẽn
# Giả sử cột 'cycle_time' là thời gian chu kỳ sản xuất
sns.histplot(data['cycle_time'], kde=True)
plt.title('Phân phối thời gian chu kỳ sản xuất')
plt.xlabel('Thời gian chu kỳ (giờ)')
plt.ylabel('Tần suất')
plt.show()

# Phát hiện các điểm bất thường (outliers)
Q1 = data['cycle_time'].quantile(0.25)
Q3 = data['cycle_time'].quantile(0.75)
IQR = Q3 - Q1
outliers = data[(data['cycle_time'] < (Q1 - 1.5 * IQR)) | (data['cycle_time'] > (Q3 + 1.5 * IQR))]
print("Các điểm bất thường trong thời gian chu kỳ sản xuất:")
print(outliers)

# Phân tích lãng phí
# Giả sử cột 'waste' là lượng lãng phí sản xuất
sns.boxplot(x=data['waste'])
plt.title('Phân tích lãng phí sản xuất')
plt.xlabel('Lượng lãng phí')
plt.show()

# Đề xuất khắc phục
# Giả sử cột 'machine_id' là mã máy móc và 'downtime' là thời gian ngừng hoạt động
downtime_analysis = data.groupby('machine_id')['downtime'].sum().reset_index()
downtime_analysis = downtime_analysis.sort_values(by='downtime', ascending=False)
print("Phân tích thời gian ngừng hoạt động của máy móc:")
print(downtime_analysis)

# Đề xuất: Tập trung vào các máy móc có thời gian ngừng hoạt động cao nhất để cải thiện hiệu suất