import random
import time
import math
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
def selection_sort(arr):
    global cambios
    n = len(arr)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                cambios[2]+=1
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        cambios[2]+=1
def bubble_sort(arr):
    global cambios
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                cambios[0]+=1
def insert_sort(arr):
    global cambios
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
            cambios[1]+=1
        arr[j+1] = key
        cambios[1]+=1

def merge_sort(arr):
    global cambios
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            cambios[4]+=1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            cambios[4]+=1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            cambios[4]+=1

    return arr

def quick_sort(arr):
    global cambios
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for x in arr[1:]:
            if x < pivot:
                left.append(x)
            else:
                right.append(x)
            cambios[5]+=1
        return quick_sort(left) + [pivot] + quick_sort(right)
def heap_sort(arr):
    global cambios
    def sift_down(start, end):
        root = start
        while True:
            child = root * 2 + 1
            if child > end:
                break
            if child + 1 <= end and arr[child] < arr[child + 1]:
                child += 1
            if arr[root] < arr[child]:
                arr[root], arr[child] = arr[child], arr[root]
                root = child
                cambios[6]+=1
            else:
                break
    # Heapify
    for start in range((len(arr) - 2) // 2, -1, -1):
        sift_down(start, len(arr) - 1)
    # Sort
    for end in range(len(arr) - 1, 0, -1):
        arr[end], arr[0] = arr[0], arr[end]
        sift_down(0, end - 1)
        cambios[6]+=1
    return arr

def counting_sort(arr):
    max_value = max(arr)
    min_value = min(arr)
    range_of_elements = max_value - min_value + 1
    count_arr = [0] * range_of_elements
    output_arr = [0] * len(arr)

    for i in range(len(arr)):
        count_arr[arr[i] - min_value] += 1

    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        output_arr[count_arr[arr[i] - min_value] - 1] = arr[i]
        count_arr[arr[i] - min_value] -= 1

    for i in range(len(arr)):
        arr[i] = output_arr[i]
def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output_arr = [0] * n
    count_arr = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count_arr[index % 10] += 1

    for i in range(1, 10):
        count_arr[i] += count_arr[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output_arr[count_arr[index % 10] - 1] = arr[i]
        count_arr[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output_arr[i]

def radix_sort(arr):
    max_value = max(arr)
    exp = 1
    while max_value // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10


def insertion_sortb(bucket):
    for i in range(1, len(bucket)):
        item_to_insert = bucket[i]
        j = i - 1
        while j >= 0 and item_to_insert < bucket[j]:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = item_to_insert

def bucket_sort(arr):
    num_buckets = 10
    max_value = max(arr)
    min_value = min(arr)
    bucket_range = (max_value - min_value) / num_buckets

    buckets = [[] for _ in range(num_buckets)]

    for num in arr:
        index = math.floor((num - min_value) / bucket_range)
        if index >= num_buckets:
            index = num_buckets - 1
        buckets[index].append(num)

    for bucket in buckets:
        insertion_sortb(bucket)

    sorted_arr = [num for bucket in buckets for num in bucket]
    return sorted_arr



def generate_random_array(size):
    return [random.randint(1, 100) for _ in range(size)]

def cn2(arr):
    return
def cn(arr):
    return

def nlog(arr):
    return

args = [bubble_sort, insert_sort, selection_sort, merge_sort, quick_sort, heap_sort, counting_sort, radix_sort, bucket_sort, cn, cn2, nlog]
tiempos = [[] for _ in range(len(args))]
datos_procesados = []
n = 10
det = bool(1)
cambios = [0 for _ in range(len(args))]
def plot_graph():
    global fig, ax, canvas, n, datos_procesados, tiempos, args, root, cambios, datos_a_procesar
    datos_procesados.append(n)
    n+=50
    arr = generate_random_array(n)
    arr1 = arr.copy()
    for i, fun in enumerate(args):
        if fun.__name__ == 'cn':
            arr = arr1.copy()
            tiempos[i].append(n * 0.00001)
        elif fun.__name__ == 'cn2':
            arr = arr1.copy()
            tiempos[i].append((n * n) * 0.0000001)
        elif fun.__name__ == 'nlog':
            arr = arr1.copy()
            tiempos[i].append((n * math.log(n)) * 0.0000001)
        else:
            start_time = time.time()
            fun(arr)
            end_time = time.time()
            arr = arr1.copy()
            tiempos[i].append(end_time - start_time)
    ax.clear()
    for i, fun in enumerate(args):
        if checkboxes[i].get():
            ax.plot(datos_procesados, tiempos[i], label=fun.__name__+"\nCambios: "+str(cambios[i]))
    ax.set_xlabel('Cantidad de datos')
    ax.set_ylabel('Tiempo (segundos)')
    ax.set_title('Tiempo de ejecución de algoritmos de ordenamiento')
    ax.legend()
    canvas.draw()
    if n <= datos_a_procesar and det:
        root.after(100, plot_graph)

root = tk.Tk()
root.title('Metodos de Ordenamiento - Grafica de Comparación')
root.geometry('800x500')

graph_frame = tk.Frame(root)
graph_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

options_frame = tk.Frame(root)
options_frame.pack(side=tk.LEFT, padx=10)

btn_frame = tk.Frame(root)
btn_frame.pack(side=tk.LEFT, expand=True)

fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111)

canvas = FigureCanvasTkAgg(fig, master=graph_frame)
canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
def start_graph():
    global button, bottonc, buttond,bottonr, n, det, tiempos, datos_procesados, cambios, aproxtime, datos_a_procesar
    if num_entry.get() != "":
        aproxtime.config(text="")
        datos_a_procesar = int(num_entry.get())
        button.config(state=tk.DISABLED)
        buttonc.config(state=tk.DISABLED)
        buttond.config(state=tk.NORMAL)
        buttonr.config(state=tk.NORMAL)
        tiempos = [[] for _ in range(len(args))]
        cambios = [0 for _ in range(len(args))]
        datos_procesados = []
        n = 10
        det = 1
        plot_graph()
    else:
        aproxtime.config(text="Ingrese Valor")

def stop_graph():
    global root, det, buttonc, buttond
    buttonc.config(state=tk.NORMAL)
    buttond.config(state=tk.DISABLED)
    det = 0
def con_graph():
    global root, det, buttonc, buttond
    buttonc.config(state=tk.DISABLED)
    buttond.config(state=tk.NORMAL)
    det = 1
    plot_graph()
def rei_graph():
    global ax, det, buttonc, buttond, button, buttonr, datos_procesados, tiempos, cambios
    tiempos = [[] for _ in range(len(args))]
    cambios = [0 for _ in range(len(args))]
    datos_procesados = []
    det = 0
    ax.clear()
    button.config(state=tk.NORMAL)
    buttonc.config(state=tk.DISABLED)
    buttond.config(state=tk.DISABLED)
    buttonr.config(state=tk.DISABLED)

checkboxes = []
for i, fun in enumerate(args):
    var = tk.BooleanVar()
    checkbox = tk.Checkbutton(options_frame, text=fun.__name__, variable=var)
    checkbox.pack()
    checkboxes.append(var)

etiqueta = tk.Label(btn_frame, text="DATOS A PROCESAR:")
etiqueta.pack()
num_entry = tk.Entry(btn_frame)
num_entry.pack()
aproxtime = tk.Label(btn_frame, text="")
aproxtime.pack()
button = tk.Button(btn_frame, text='Iniciar', command=start_graph)
button.pack()
buttond = tk.Button(btn_frame, text='Detener', command=stop_graph)
buttond.config(state=tk.DISABLED)
buttond.pack()
buttonc = tk.Button(btn_frame, text='Continuar', command=con_graph)
buttonc.config(state=tk.DISABLED)
buttonc.pack()
buttonr = tk.Button(btn_frame, text='Reiniciar', command=rei_graph)
buttonr.config(state=tk.DISABLED)
buttonr.pack()

root.mainloop()