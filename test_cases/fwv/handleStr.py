
class handleString:
    def get_words(str):
            result = []
            words = list(str)

            for word in words:
                if word not in ['a','k']:
                    result.append(word)
            return result.sort()

# if __name__ == "__main__":
#     str = 'abcd'
#     print(list(str))


