import sys

from plot.utils.time_acc_base import plot_time_acc_fall

fed_avg = [85.59, 87.27, 88.35, 88.14, 88.65, 88.59, 88.97, 89.14, 89.22, 89.08, 89.3, 89.38, 89.16, 89.14, 89.32, 89.35, 89.43, 89.3, 89.14, 89.65, 89.41, 89.35, 89.62, 89.51, 89.68, 89.32, 89.22, 89.3, 89.57, 89.3, 89.32, 89.11, 89.22, 89.11, 89.24, 89.08, 89.38, 89.41, 89.73, 89.14, 89.27, 89.27, 89.32, 89.3, 89.59, 89.49, 89.38, 89.38, 89.41, 89.46, 89.27, 89.46, 89.05, 89.46, 89.49, 89.41, 89.16, 89.19, 89.08, 89.19, 89.3, 89.32, 89.43, 89.19, 89.32, 89.27, 89.41, 89.3, 89.43, 89.57, 89.65, 89.27, 89.24, 89.43, 89.38, 89.49, 89.35, 89.3, 89.41, 89.43, 89.3, 89.32, 89.35, 89.24, 89.24, 89.27, 89.32, 89.35, 89.35, 89.38, 89.24, 89.16, 89.3, 89.14, 89.24, 89.24, 89.08, 89.24, 89.0, 89.16, 89.16, 89.03, 89.0, 89.19, 89.14, 89.0, 89.03, 89.03, 89.0, 89.0, 89.0, 89.0, 89.0, 89.03, 89.0, 89.03, 89.0, 89.03, 89.03, 89.03, 89.0, 89.0, 89.08, 89.11, 89.03, 89.0, 89.05, 89.03, 89.03, 88.97, 89.03, 89.05, 89.03, 89.03, 88.97, 89.03, 89.0, 89.38, 89.19, 89.43, 89.35, 89.24, 89.16, 89.35, 89.35, 89.08, 89.3, 89.49, 89.43, 89.43, 89.27, 89.32, 89.35, 89.3, 89.38, 89.38, 89.27, 89.16, 89.27, 89.22, 89.22, 89.22, 89.22, 89.27, 89.3, 89.41, 89.32, 89.43, 89.32, 89.24, 89.27, 89.22, 89.19, 89.16, 89.22, 89.24, 89.22, 89.24, 89.24, 89.27, 89.22, 89.27, 89.19, 89.24, 89.11, 89.27, 89.3, 89.35, 89.22, 89.3, 89.32, 89.24, 89.32, 89.38, 89.32, 89.32, 89.24, 89.3, 89.32, 89.32]
fed_sync_sgd = [55.84, 0.86, 36.35, 20.51, 33.84, 21.14, 61.86, 21.89, 68.3, 24.43, 66.84, 28.7, 67.46, 31.7, 68.68, 36.62, 70.05, 41.97, 72.38, 46.14, 74.32, 49.86, 76.0, 54.51, 77.62, 57.41, 78.43, 60.65, 78.89, 62.14, 79.16, 64.05, 79.86, 66.0, 79.38, 67.05, 79.81, 68.41, 80.0, 69.7, 80.35, 70.76, 80.35, 72.19, 80.92, 74.16, 81.41, 75.32, 81.78, 76.59, 82.62, 77.19, 83.03, 78.62, 82.97, 79.65, 83.16, 80.62, 84.14, 81.68, 84.41, 82.68, 84.76, 83.35, 85.19, 84.0, 85.46, 84.22, 85.65, 84.86, 85.57, 85.41, 85.62, 86.03, 86.3, 86.16, 86.57, 85.84, 86.81, 86.22, 87.3, 86.65, 87.16, 86.65, 87.03, 86.68, 87.08, 86.89, 87.38, 87.19, 87.43, 87.11, 87.51, 87.35, 87.54, 87.68, 87.57, 87.32, 87.76, 87.7, 87.7, 87.81, 88.0, 88.14, 88.11, 88.03, 88.0, 88.16, 88.3, 88.22, 88.14, 88.08, 88.14, 88.14, 88.14, 88.19, 88.27, 88.27, 88.24, 88.3, 88.16, 88.14, 88.0, 88.08, 87.97, 88.19, 88.03, 88.05, 88.05, 88.05, 88.08, 88.08, 87.97, 88.0, 88.03, 88.05, 87.97, 87.97, 87.97, 88.03, 87.97, 88.0, 88.0, 87.95, 88.0, 87.89, 87.97, 87.92, 88.0, 87.97, 87.97, 87.95, 87.95, 87.95, 87.95, 88.03, 88.0, 88.0, 87.97, 88.03, 88.03, 88.0, 88.0, 88.0, 88.0, 88.0, 88.0, 88.0, 88.0, 88.0, 88.0, 87.97, 87.97, 87.97, 87.97, 88.05, 87.97, 88.05, 88.03, 87.97, 87.97, 88.05, 88.05, 88.05, 88.03, 88.05, 88.08, 88.05, 88.08, 88.08, 88.11, 88.11, 88.11, 88.11, 88.11, 88.08, 88.08, 88.11, 88.14, 88.14]
fed_efsign = [28.19, 0.35, 61.3, 46.46, 71.84, 70.62, 72.19, 71.73, 70.68, 71.57, 71.14, 74.73, 71.86, 73.92, 71.68, 72.86, 71.05, 72.35, 71.05, 71.78, 71.57, 71.68, 71.76, 71.89, 72.81, 73.38, 74.19, 74.51, 75.41, 74.68, 75.49, 75.08, 76.14, 75.76, 76.95, 76.62, 77.65, 77.65, 78.03, 77.89, 78.92, 78.7, 79.0, 78.95, 79.49, 79.27, 79.46, 79.27, 79.68, 79.27, 80.0, 79.65, 79.95, 79.49, 80.16, 79.65, 80.22, 79.49, 80.27, 79.81, 79.84, 79.89, 80.3, 80.19, 80.78, 80.49, 80.86, 80.84, 81.3, 81.3, 81.84, 81.7, 82.14, 82.41, 82.84, 83.14, 83.73, 83.76, 83.92, 83.73, 84.0, 83.84, 83.62, 83.78, 83.95, 83.95, 83.84, 83.68, 84.0, 83.81, 83.59, 83.27, 83.41, 83.24, 82.84, 82.57, 81.62, 81.24, 79.97, 77.65, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0]

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_time_acc_fall("", fed_sync_sgd, fed_efsign, fed_avg, save_path, plot_size="L")
