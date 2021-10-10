import sys

from plot.utils.time_acc_base import plot_time_acc_lrsc

fed_avg = [71.05, 78.33, 81.75, 85.0, 85.89, 85.54, 87.02, 86.99, 87.12, 87.74, 87.63, 87.58, 88.04, 87.37, 87.2, 87.69, 87.15, 88.01, 88.06, 88.04, 87.28, 88.12, 88.15, 87.98, 88.39, 87.85, 88.2, 87.45, 87.93, 88.06, 87.77, 87.66, 88.12, 87.88, 87.37, 87.55, 88.09, 87.96, 87.72, 87.45, 87.55, 87.42, 87.5, 87.53, 87.63, 87.69, 87.5, 87.55, 87.85, 87.53, 87.69, 87.66, 87.66, 87.2, 87.69, 87.58, 87.63, 87.66, 87.63, 87.66, 87.8, 87.58, 87.85, 87.72, 87.66, 87.53, 87.47, 87.39, 87.12, 87.58, 87.8, 87.39, 87.77, 87.88, 87.39, 87.88, 87.9, 87.96, 87.42, 87.53]
fed_sync = [67.74, 72.8, 74.92, 78.31, 79.97, 83.28, 83.09, 83.9, 84.01, 83.95, 84.03, 85.99, 84.95, 85.08, 85.13, 85.32, 85.65, 86.16, 84.95, 85.78, 85.91, 86.29, 86.51, 85.48, 85.13, 85.78, 85.94, 85.59, 86.48, 85.94, 86.13, 86.02, 86.67, 85.94, 86.75, 86.16, 85.65, 86.21, 85.81, 86.24, 86.16, 85.94, 86.45, 86.48, 86.61, 86.37, 86.37, 86.75, 86.53, 86.16, 86.69, 86.67, 85.81, 86.59, 86.4, 85.99, 86.16, 86.24, 86.61, 86.64, 85.94, 86.72, 86.61, 86.64, 86.56, 85.99, 86.67, 86.08, 86.69, 86.51, 86.83, 86.69, 86.24, 86.13, 86.69, 86.91, 86.18, 87.18, 86.67, 86.75]
fed_sync_lrsc_5 = [30.73, 41.37, 33.15, 57.5, 64.33, 68.87, 69.54, 67.5, 68.39, 68.6, 69.22, 69.52, 69.84, 69.78, 69.81, 69.97, 69.97, 70.03, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08, 70.08]
fed_sync_lrsc_10 = [15.89, 44.19, 36.91, 69.95, 52.2, 77.74, 61.48, 64.14, 58.9, 63.9, 66.53, 68.49, 69.6, 69.33, 68.79, 68.28, 68.12, 68.23, 68.25, 68.28, 68.28, 67.98, 67.96, 67.72, 67.61, 67.63, 67.72, 67.66, 67.63, 67.69, 67.69, 67.66, 67.63, 67.72, 67.72, 67.69, 67.72, 67.69, 67.63, 67.63, 67.63, 67.63, 67.63, 67.63, 67.63, 67.63, 67.63, 67.63, 67.66, 67.66, 67.66, 67.66, 67.66, 67.66, 67.66, 67.66, 67.66, 67.66, 67.66, 67.66, 67.66, 67.66, 67.66, 67.66, 67.66, 67.66, 67.66, 67.66, 67.66, 67.66, 67.66, 67.66, 67.66, 67.66, 67.66, 67.66, 67.66, 67.66, 67.66, 67.66]
fed_sync_lrsc_20 = [17.5, 43.12, 39.89, 45.62, 43.66, 58.74, 37.55, 60.27, 52.34, 41.29, 43.98, 53.06, 38.44, 59.81, 30.48, 63.28, 30.3, 67.9, 36.26, 38.47, 41.34, 51.29, 63.17, 68.76, 69.95, 70.3, 70.91, 71.61, 71.37, 71.26, 69.87, 68.84, 69.81, 69.57, 69.57, 69.38, 70.65, 70.94, 72.26, 72.34, 72.18, 72.07, 71.77, 71.8, 71.91, 71.75, 71.88, 71.8, 71.61, 71.67, 71.8, 71.72, 71.83, 71.8, 71.85, 71.88, 71.99, 71.8, 71.88, 71.91, 71.88, 71.88, 71.88, 71.88, 71.88, 71.88, 71.88, 71.88, 71.88, 71.88, 71.88, 71.88, 71.88, 71.88, 71.88, 71.88, 71.88, 71.91, 71.91, 71.91]

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_time_acc_lrsc("", fed_sync_lrsc_5, fed_sync_lrsc_10, fed_sync_lrsc_20, fed_sync, fed_avg, save_path, plot_size="L")
