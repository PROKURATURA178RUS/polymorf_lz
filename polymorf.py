import pandas as pd

class DataProcessor:
    def __init__(self, data):
        self.data = data
    

    def split_by_payment_type(self):  #Разделяет датасет на два по признаку 'Вид расчета' и сохраняет как отдельные файлы       
        cash_data = self.data[self.data['Вид расчета'] == 'наличный']
        cashless_data = self.data[self.data['Вид расчета'] == 'безналичный']
        
        cash_data.to_csv('cash_payments.csv')
        cashless_data.to_csv('cashless_payments.csv')
        
        return cash_data, cashless_data
     

    def __invert__(self):    #Унарный оператор ~ для удаления дубликатов и вывода количества удаленных записей
        initial_rows = len(self.data)
        cleaned_data = self.data.drop_duplicates()
        removed = initial_rows - len(cleaned_data)
        duplicate_counts = self.data.duplicated().sum()
        print(f"Количество повторяющихся строк в исходном наборе данных: {duplicate_counts}")
        print(f"Количество удаленных дубликатов: {removed}")
        return DataProcessor(cleaned_data)


def main():
       # Загрузка данных
    data = pd.read_csv('var4.csv')
   
       # Создание экземпляра класса и обработка данных
    processor = DataProcessor(data)

      # Разделение данных по виду расчета
    cash_data, cashless_data = processor.split_by_payment_type()
    print("Данные успешно разделены и сохранены в 'cash_payments.csv' и 'cashless_payments.csv'.")

       # Удаление дубликатов с помощью унарного оператора (~)
    cleaned_processor = ~processor
    
if __name__ == "__main__":
    main()
    