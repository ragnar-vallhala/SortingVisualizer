class Sorting:
    
    def __init__(self, update):
        self.callback = update
        
    
    def bubble_sort(self, arr):
       
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                self.callback(arr)
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    
    def selection_sort(self, arr):
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                self.callback(arr)
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            
    
    def merge_sort(self, arr):
 
        current_size = 1

        while current_size < len(arr) - 1:

            left = 0
            while left < len(arr) - 1:
                self.callback(arr)
                mid = min((left + current_size - 1), (len(arr) - 1))
                right = ((2 * current_size + left - 1, len(arr) - 1)[2 * current_size + left - 1 > len(arr) - 1])

                self.merge(arr, left, mid, right)
                left = left + current_size * 2

            current_size = 2 * current_size
            


    def merge(self, arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m

        L = [0] * n1
        R = [0] * n2


        for i in range(0, n1):
            L[i] = arr[l + i]
        for j in range(0, n2):
            R[j] = arr[m + 1 + j]


        i = j = 0
        k = l

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1

        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1
    
    def quick_sort(self, arr):
        self._quick_sort(arr, 0, len(arr) - 1)

    def _quick_sort(self, arr, low, high):
        if low < high:
            pivot_index = self.partition(arr, low, high)
            self._quick_sort(arr, low, pivot_index - 1)
            self._quick_sort(arr, pivot_index + 1, high)
            self.callback(arr)

    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def radix_sort(self, arr):
        # Find the maximum number to determine the number of digits
        max_num = max(arr)
        exp = 1

        # Perform counting sort for each digit, starting from the least significant digit
        while max_num // exp > 0:
            self.counting_sort(arr, exp)
            exp *= 10
            self.callback(arr)
            

    def counting_sort(self, arr, exp):
        n = len(arr)
        output = [0] * n
        count = [0] * 10

        # Count occurrences of each digit in the current place value
        for num in arr:
            index = (num // exp) % 10
            count[index] += 1

        # Calculate cumulative count
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Build the output array in sorted order
        i = n - 1
        while i >= 0:
            index = (arr[i] // exp) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1
            i -= 1
            

        # Update the original array
        for i in range(n):
            arr[i] = output[i]
        
        