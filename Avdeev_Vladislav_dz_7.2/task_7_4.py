# Задание № 4


import os


def display_stats(base_dir: str) -> dict:
    points = {10 ** x: 0 for x in range(1, 5)}
    points[0] = 0

    for item in os.walk(top=base_dir):
        files = item[2]
        if files:
            folder = item[0]
            for file in files:
                size = os.stat(os.path.join(folder, file)).st_size

                for key in sorted(points.keys()):
                    if size > key:
                        continue
                    else:
                        points[key] += 1
                        break
        return {points: count for points, count in sorted(points.items()) if count}

if __name__ == '__main__':
    base_dir = 'some_data'
    print(display_stats(base_dir=base_dir))

