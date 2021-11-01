import sys

from plot.utils.time_acc_base import plot_time_acc

fed_avg = [22.81, 34.0, 39.86, 43.81, 46.46, 47.65, 48.89, 49.35, 49.27, 50.86, 50.89, 50.54, 50.65, 51.14, 51.11, 51.86, 51.22, 50.92, 50.68, 51.46, 51.03, 50.97, 51.27, 50.11, 50.19, 50.3, 50.11, 49.89, 50.22, 50.16, 49.57, 49.78, 49.51, 49.46, 49.35, 49.11, 49.08, 49.73, 48.68, 48.41, 48.05, 48.27, 48.05, 48.11, 47.92, 47.97, 47.78, 47.76, 48.57, 48.08, 47.65, 47.81, 48.32, 49.05, 47.95, 47.35, 47.97, 48.59, 47.7, 48.57, 48.03, 48.49, 48.62, 48.7, 47.92, 48.95, 48.7, 47.05, 47.73, 47.54, 48.35, 48.62, 48.43, 48.43, 48.43, 48.35, 48.57, 48.65, 48.73, 48.14, 47.76, 47.54, 47.68, 47.97, 48.03, 48.05, 48.16, 47.51, 47.81, 48.16, 47.95, 47.65, 47.95, 48.16, 48.41, 48.51, 48.59, 48.46, 48.46, 48.41, 48.7, 48.65, 48.54, 48.68, 48.62, 48.76, 48.68, 48.46, 48.7, 48.78, 48.57, 48.57, 48.16, 48.35, 48.27, 48.24, 48.49, 48.68, 48.7, 48.59, 48.57, 48.27, 48.73, 48.73, 48.76, 48.27, 48.65, 48.59, 48.49, 48.46, 48.51, 48.54, 48.51, 48.51, 48.46, 48.24, 48.14, 48.46, 48.43, 48.32, 48.49, 48.68, 48.65, 48.62, 48.54, 48.57, 48.62, 48.65, 48.51, 48.68, 48.57, 48.49, 48.41, 48.68, 48.41, 48.49, 48.08, 48.11, 48.32, 48.11, 48.38, 48.32, 48.16, 48.27, 48.3, 48.24, 48.24, 48.57, 48.54, 47.84, 48.41, 48.27, 48.0, 47.86, 47.84, 48.3, 48.08, 48.22, 48.11, 48.03, 48.3, 48.59, 48.76, 48.51, 48.73, 48.86, 48.84, 48.89, 48.78, 48.81, 48.86, 48.92, 48.89, 49.0, 48.11, 48.73, 48.46, 47.92, 48.24, 48.08]
fed_efsign = [19.57, 25.38, 31.81, 36.08, 36.59, 37.68, 38.86, 42.78, 45.49, 46.73, 47.84, 47.59, 46.95, 46.62, 46.35, 45.62, 45.81, 45.16, 46.16, 47.38, 47.24, 47.51, 47.38, 48.73, 46.54, 46.43, 46.14, 46.86, 45.86, 45.81, 46.46, 45.3, 45.59, 45.16, 45.7, 44.22, 45.05, 44.7, 44.73, 44.27, 45.65, 46.43, 44.7, 45.54, 44.59, 45.24, 45.51, 44.7, 46.35, 45.24, 45.35, 44.22, 44.76, 44.22, 45.81, 43.84, 45.89, 43.46, 45.49, 44.59, 45.46, 42.86, 44.24, 43.65, 45.51, 43.49, 44.65, 43.76, 44.68, 42.97, 44.27, 43.73, 43.78, 44.03, 43.24, 43.3, 44.14, 43.76, 43.24, 44.0, 44.41, 43.57, 42.73, 42.08, 43.57, 43.84, 41.89, 43.0, 42.46, 44.54, 42.41, 43.46, 42.86, 42.35, 43.43, 44.0, 42.08, 43.51, 42.89, 42.89, 43.65, 42.89, 43.46, 42.51, 44.86, 43.54, 43.62, 43.89, 44.08, 42.08, 44.03, 43.08, 45.32, 42.49, 44.3, 42.97, 43.76, 42.78, 43.89, 43.81, 44.51, 41.84, 42.84, 42.43, 43.76, 42.32, 43.76, 41.95, 43.05, 43.0, 43.32, 43.27, 43.35, 42.46, 43.35, 42.03, 41.3, 43.03, 42.46, 42.19, 42.05, 42.05, 42.68, 41.27, 42.62, 43.14, 43.76, 42.08, 41.89, 41.41, 42.68, 41.27, 41.03, 40.46, 41.73, 40.89, 42.65, 41.81, 40.49, 39.86, 42.86, 40.62, 43.08, 42.68, 43.95, 41.92, 42.03, 41.27, 42.46, 41.19, 42.62, 40.43, 42.92, 41.81, 43.54, 40.38, 43.54, 39.05, 42.27, 40.76, 43.05, 40.49, 42.97, 41.95, 42.46, 41.65, 42.27, 39.92, 42.22, 39.97, 42.81, 41.32, 40.84, 41.03, 42.54, 40.81, 40.43, 40.16, 41.68, 40.05]
fed_sync = [25.54, 33.41, 39.49, 45.19, 46.95, 48.92, 49.76, 50.76, 50.59, 49.54, 50.76, 49.95, 49.54, 49.97, 50.32, 50.19, 49.76, 49.16, 49.38, 49.73, 49.38, 49.08, 48.86, 49.16, 48.54, 48.32, 48.22, 48.65, 48.19, 48.68, 47.89, 48.49, 48.11, 47.97, 47.76, 48.51, 47.89, 47.89, 47.65, 48.11, 47.27, 47.78, 47.35, 47.19, 47.54, 47.32, 46.84, 47.19, 46.86, 47.03, 46.92, 47.05, 47.16, 47.24, 46.78, 46.54, 47.05, 46.68, 46.49, 46.41, 47.24, 46.46, 46.54, 46.78, 46.76, 47.03, 46.89, 47.35, 46.65, 46.86, 46.89, 46.76, 46.0, 46.78, 46.46, 46.35, 46.81, 46.81, 46.65, 46.62, 46.16, 46.11, 46.16, 46.84, 46.49, 46.24, 46.51, 46.38, 46.78, 46.57, 46.81, 46.76, 46.59, 46.7, 46.86, 46.78, 46.95, 46.89, 46.97, 46.89, 46.97, 46.76, 46.7, 46.86, 46.76, 46.57, 46.46, 46.14, 46.08, 46.38, 46.38, 46.51, 46.54, 46.57, 46.51, 46.49, 46.81, 46.68, 46.89, 46.86, 47.03, 46.76, 46.76, 46.32, 46.78, 46.78, 46.92, 47.22, 47.24, 47.22, 47.19, 47.27, 47.14, 47.14, 47.11, 46.97, 46.86, 46.89, 46.92, 46.92, 46.78, 46.24, 45.97, 46.51, 46.73, 46.73, 46.78, 46.81, 46.76, 46.76, 46.86, 46.81, 46.86, 46.81, 46.86, 46.84, 46.78, 46.95, 46.92, 46.95, 46.81, 46.81, 46.86, 46.78, 46.38, 46.49, 46.54, 46.51, 46.32, 45.95, 45.97, 45.08, 46.0, 45.73, 45.97, 46.24, 46.43, 46.27, 46.68, 46.27, 46.57, 46.43, 46.16, 46.38, 46.49, 46.57, 46.57, 46.49, 46.49, 46.43, 46.59, 46.54, 46.51, 46.54, 46.73, 46.41, 46.62, 46.43, 46.65, 46.35]
fed_sync_sgd = [20.32, 15.7, 29.27, 33.16, 35.59, 38.65, 40.84, 42.11, 43.32, 45.19, 46.22, 46.84, 47.46, 47.76, 47.62, 48.41, 48.35, 48.89, 49.32, 49.41, 49.7, 49.95, 49.43, 49.3, 48.76, 48.38, 48.92, 48.84, 48.92, 49.03, 49.11, 49.24, 49.51, 49.54, 49.62, 49.35, 49.84, 49.68, 49.89, 49.54, 49.86, 49.76, 50.22, 50.03, 49.81, 49.92, 49.73, 49.68, 50.03, 49.89, 49.73, 49.7, 49.46, 49.54, 49.46, 49.41, 49.19, 48.86, 49.19, 49.08, 49.24, 49.08, 49.0, 49.0, 49.0, 48.65, 48.62, 49.08, 49.46, 49.54, 49.7, 49.84, 49.51, 49.22, 49.43, 49.51, 49.65, 49.68, 49.68, 49.32, 49.03, 48.7, 48.7, 48.92, 49.19, 49.22, 49.27, 49.16, 48.97, 48.89, 48.3, 48.41, 48.3, 48.27, 48.54, 49.08, 48.86, 48.95, 49.43, 49.35, 49.24, 49.27, 49.32, 49.3, 49.43, 49.38, 49.38, 49.46, 49.38, 49.19, 49.27, 49.38, 49.27, 49.27, 49.43, 49.38, 49.46, 49.41, 49.49, 49.49, 49.51, 49.51, 49.49, 49.41, 49.3, 49.24, 49.3, 49.35, 49.27, 49.3, 49.3, 49.3, 49.38, 49.32, 49.19, 49.19, 49.27, 49.24, 49.22, 49.24, 49.3, 49.38, 49.32, 49.35, 49.27, 49.24, 49.16, 49.11, 49.08, 49.08, 49.08, 49.08, 49.08, 49.11, 49.08, 49.08, 49.08, 49.08, 49.08, 49.08, 49.05, 49.05, 49.05, 49.11, 49.11, 49.11, 49.08, 49.08, 49.05, 49.05, 49.05, 49.05, 49.05, 49.05, 49.05, 49.05, 49.03, 49.03, 49.03, 49.03, 49.03, 49.03, 49.03, 49.05, 49.05, 49.05, 49.05, 49.03, 49.0, 49.0, 49.03, 49.05, 49.03, 49.03, 49.03, 49.05, 49.03, 49.03, 49.03, 49.05]
local_train = [23.62, 32.0, 39.76, 39.54, 40.27, 39.0, 37.43, 39.43, 39.76, 40.32, 40.41, 40.62, 40.51, 40.51, 40.62, 40.43, 40.54, 40.43, 40.49, 40.59, 40.51, 40.57, 40.59, 40.54, 40.57, 40.57, 40.49, 40.43, 40.38, 40.35, 40.43, 40.38, 40.46, 40.38, 40.41, 40.46, 40.49, 40.54, 40.54, 40.54, 40.54, 40.54, 40.54, 40.57, 40.54, 40.49, 40.51, 40.43, 40.43, 40.43, 40.43, 40.43, 40.43, 40.41, 40.41, 40.41, 40.41, 40.41, 40.41, 40.43, 40.43, 40.43, 40.49, 40.49, 40.49, 40.51, 40.49, 40.51, 40.51, 40.54, 40.51, 40.51, 40.49, 40.46, 40.46, 40.49, 40.46, 40.46, 40.43, 40.38, 40.38, 40.41, 40.41, 40.41, 40.35, 40.38, 40.38, 40.32, 40.32, 40.32, 40.32, 40.32, 40.3, 40.35, 40.32, 40.32, 40.32, 40.32, 40.32, 40.32, 40.32, 40.3, 40.3, 40.32, 40.32, 40.32, 40.32, 40.32, 40.32, 40.32, 40.32, 40.32, 40.32, 40.32, 40.32, 40.35, 40.41, 40.41, 40.41, 40.41, 40.41, 40.41, 40.41, 40.41, 40.41, 40.41, 40.41, 40.41, 40.41, 40.41, 40.41, 40.41, 40.38, 40.35, 40.35, 40.35, 40.35, 40.35, 40.35, 40.35, 40.35, 40.35, 40.32, 40.32, 40.32, 40.3, 40.3, 40.3, 40.3, 40.3, 40.3, 40.3, 40.3, 40.3, 40.3, 40.3, 40.27, 40.27, 40.27, 40.27, 40.27, 40.27, 40.27, 40.27, 40.24, 40.27, 40.24, 40.27, 40.27, 40.27, 40.27, 40.27, 40.27, 40.27, 40.27, 40.27, 40.27, 40.27, 40.27, 40.24, 40.24, 40.24, 40.27, 40.3, 40.32, 40.32, 40.32, 40.32, 40.32, 40.32, 40.32, 40.32, 40.32, 40.32, 40.32, 40.3, 40.3, 40.32, 40.3, 40.27]

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_time_acc("", fed_sync_sgd, fed_sync, fed_efsign, fed_avg, local_train, save_path, plot_size="M")
