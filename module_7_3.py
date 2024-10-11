

class WordsFinder:
    def __init__(self,*file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {} # словарь для хранения слов из файлов

        for file_name in self.file_names:
            with open(file_name,'r',encoding= 'utf8') as file:# читаем файл
                text = file.read().lower()# приводим к нижнему регисртру
                punctation = [',','.','=','!','?',':',':','-']
                for punct in punctation:
                    text = text.replace(punct,'')# убираем пунктацию
                words = text.split()
                all_words[file_name] = words# записываем в словарь
        return all_words

# a = WordsFinder('products.txt')
# print(a.get_all_words())

    def find(self,word):
        word = word.lower()# приводим искомое слово к нижнему регистру
        result = {} #словарь для хранения результатов
        all_words = self.get_all_words()# получаем все слова из файлов

        for file_name,words in all_words.items():
            if word in words:
                position = words.index(word)+1# находим позицию первого вхождения слов счет с 1
                result[file_name] = position
        return result

# a = WordsFinder('test.txt')
# print(a.find('спасибо'))

    def count(self,word):
        word = word.lower()#приводим найденое слово в нижний регистр
        result = {}# словарь для хранения кол-ва вхождения
        all_words = self.get_all_words() # получаем все слова из файлов
        for file_name,words in all_words.items():
            count = words.count(word) #считаем кол-во вхождений
            if count > 0:
             result[file_name] = count
        return result
# A=WordsFinder('test.txt')
# print(A.count('спасибо'))

finder2 = WordsFinder('test.txt','products.txt')
print(finder2.get_all_words())
print(finder2.find('СПАСИБО'))
print(finder2.count('СПАсибо'))
print(finder2.find('Vegetables'))
print(finder2.count('potATO'))