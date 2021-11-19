import sys

from plot.utils.time_acc_base import plot_time_acc_sensitivity

lr_01 = [55.84, 0.86, 36.35, 20.51, 33.84, 21.14, 61.86, 21.89, 68.3, 24.43, 66.84, 28.7, 67.46, 31.7, 68.68, 36.62, 70.05, 41.97, 72.38, 46.14, 74.32, 49.86, 76.0, 54.51, 77.62, 57.41, 78.43, 60.65, 78.89, 62.14, 79.16, 64.05, 79.86, 66.0, 79.38, 67.05, 79.81, 68.41, 80.0, 69.7, 80.35, 70.76, 80.35, 72.19, 80.92, 74.16, 81.41, 75.32, 81.78, 76.59, 82.62, 77.19, 83.03, 78.62, 82.97, 79.65, 83.16, 80.62, 84.14, 81.68, 84.41, 82.68, 84.76, 83.35, 85.19, 84.0, 85.46, 84.22, 85.65, 84.86, 85.57, 85.41, 85.62, 86.03, 86.3, 86.16, 86.57, 85.84, 86.81, 86.22, 87.3, 86.65, 87.16, 86.65, 87.03, 86.68, 87.08, 86.89, 87.38, 87.19, 87.43, 87.11, 87.51, 87.35, 87.54, 87.68, 87.57, 87.32, 87.76, 87.7, 87.7, 87.81, 88.0, 88.14, 88.11, 88.03, 88.0, 88.16, 88.3, 88.22, 88.14, 88.08, 88.14, 88.14, 88.14, 88.19, 88.27, 88.27, 88.24, 88.3, 88.16, 88.14, 88.0, 88.08, 87.97, 88.19, 88.03, 88.05, 88.05, 88.05, 88.08, 88.08, 87.97, 88.0, 88.03, 88.05, 87.97, 87.97, 87.97, 88.03, 87.97, 88.0, 88.0, 87.95, 88.0, 87.89, 87.97, 87.92, 88.0, 87.97, 87.97, 87.95, 87.95, 87.95, 87.95, 88.03, 88.0, 88.0, 87.97, 88.03, 88.03, 88.0, 88.0, 88.0, 88.0, 88.0, 88.0, 88.0, 88.0, 88.0, 88.0, 87.97, 87.97, 87.97, 87.97, 88.05, 87.97, 88.05, 88.03, 87.97, 87.97, 88.05, 88.05, 88.05, 88.03, 88.05, 88.08, 88.05, 88.08, 88.08, 88.11, 88.11, 88.11, 88.11, 88.11, 88.08, 88.08, 88.11, 88.14, 88.14]
lr_1 = [10.0, 45.6, 40.3, 26.9, 23.3, 25.27, 35.1, 27.0, 35.63, 36.1, 36.13, 43.53, 37.97, 10.0, 40.1, 10.0, 42.17, 51.63, 47.0, 58.0, 28.27, 10.0, 10.0, 10.0, 10.0, 65.37, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 37.7, 75.73, 34.73, 72.07, 34.8, 10.0, 35.03, 76.27, 35.6, 76.03, 36.13, 73.23, 34.03, 76.23, 34.87, 78.83, 33.57, 79.23, 32.37, 78.97, 30.7, 78.4, 32.77, 78.47, 31.43, 79.37, 30.57, 79.2, 76.37, 79.97, 77.03, 79.83, 76.03, 79.53, 75.53, 81.7, 75.27, 82.17, 75.6, 82.13, 77.33, 82.43, 76.57, 82.27, 76.8, 82.63, 76.47, 82.27, 76.07, 82.23, 77.57, 83.07, 79.13, 83.4, 78.5, 82.9, 78.5, 83.07, 78.6, 83.5, 78.23, 83.2, 77.9, 82.73, 79.5, 83.77, 79.63, 80.0, 79.2, 79.43, 79.3, 79.7, 79.23, 79.57, 79.23, 79.47, 79.47, 80.13, 79.87, 80.27, 80.37, 80.37, 79.93, 80.17, 80.17, 80.2, 80.3, 80.57, 80.6, 81.1, 80.73, 81.07, 80.57, 80.67, 80.13, 80.5, 80.4, 80.8, 80.5, 80.87, 80.73, 81.1, 80.9, 81.3, 80.97, 81.13, 80.77, 80.87, 80.43, 80.73, 80.47, 80.5, 80.3, 80.9, 81.0, 81.03, 80.97, 81.0, 80.83, 80.9, 80.7, 80.73, 80.63, 80.8, 80.63, 80.67, 80.67, 80.7, 80.6, 80.6, 80.53, 80.63, 80.6, 80.83, 80.7, 81.0, 81.03, 81.33, 81.33, 81.4, 81.23, 81.33, 81.4, 81.53, 81.47, 81.4, 81.37, 81.37, 81.23, 81.3, 81.3, 81.3, 81.23, 81.37, 81.33, 81.5, 81.5, 81.57, 81.57, 81.73, 81.7, 81.7, 81.7, 82.1, 82.03, 82.03, 82.07, 82.03]
lr_001 = [22.07, 38.47, 47.23, 51.33, 51.1, 49.13, 46.63, 42.3, 38.23, 33.67, 31.87, 29.63, 29.97, 29.0, 28.63, 28.0, 28.33, 27.37, 27.5, 26.7, 27.3, 27.6, 28.27, 28.5, 29.3, 29.07, 29.7, 29.57, 30.07, 30.5, 31.37, 31.33, 32.37, 32.73, 33.87, 33.87, 33.87, 33.0, 33.53, 34.57, 36.37, 36.73, 37.77, 38.2, 39.1, 39.1, 39.67, 40.4, 42.2, 43.43, 44.33, 44.47, 45.13, 45.1, 45.63, 45.87, 45.97, 45.97, 47.3, 47.27, 47.8, 48.2, 49.57, 50.27, 51.57, 52.03, 52.63, 52.8, 53.6, 53.57, 54.43, 54.6, 54.8, 54.87, 54.5, 54.57, 55.33, 55.4, 55.57, 55.97, 56.1, 56.63, 56.97, 57.6, 57.5, 57.07, 57.63, 57.77, 58.17, 58.17, 58.67, 58.63, 58.97, 59.57, 59.93, 60.03, 60.53, 60.27, 60.3, 60.3, 60.47, 60.43, 60.4, 60.37, 60.33, 60.4, 60.4, 60.57, 60.63, 60.6, 60.63, 60.5, 60.6, 60.67, 60.7, 60.63, 60.73, 60.77, 60.87, 60.9, 60.87, 60.97, 60.8, 60.97, 60.87, 60.9, 60.97, 60.93, 60.93, 60.93, 61.03, 61.0, 60.97, 60.93, 61.03, 61.13, 61.17, 61.13, 61.13, 61.0, 60.87, 60.93, 61.0, 61.0, 60.9, 60.87, 60.8, 60.77, 60.93, 60.93, 60.93, 60.93, 60.93, 60.93, 60.93, 60.93, 60.93, 60.93, 60.93, 60.93, 60.9, 60.9, 60.87, 60.87, 60.87, 60.83, 60.83, 60.83, 60.87, 60.87, 60.87, 60.83, 60.9, 60.9, 60.9, 60.87, 60.87, 60.87, 60.9, 60.93, 60.9, 60.87, 60.87, 60.9, 60.9, 60.9, 60.9, 60.9, 60.9, 60.9, 60.9, 60.9, 60.9, 60.9, 60.9, 60.87, 60.87, 60.97, 60.9, 60.9]

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_time_acc_sensitivity("", lr_1, lr_01, lr_001, save_path, plot_size="3")
