
    def encrypt(plain_text, key):
        output_text = []
        crypt_text = []

        upper_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


        for char in plain_text:
            if char in upper_case:
                index = upper_case.index(char)
                crypting = (index + key) % 26
                crypt_text.append(crypting)
                new_letter = upper_case[crypting]
                output_text.append(new_letter)
            elif char in lower_case:
                index = lower_case.index(char)
                crypting = (index + key) % 26
                crypt_text.append(crypting)
                new_letter = lower_case[crypting]
                output_text.append(new_letter)
        print(output_text)
        return output_text


    def decrypt(output_text, key):
        decrypt_output = []
        crypt_text = []

        upper_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        for char in output_text:
            if char in upper_case:
                index = upper_case.index(char)
                crypting = (index - key) % 26
                crypt_text.append(crypting)
                new_letter = upper_case[crypting]
                decrypt_output.append(new_letter)
            elif char in lower_case:
                index = lower_case.index(char)
                crypting = (index - key) % 26
                crypt_text.append(crypting)
                new_letter = lower_case[crypting]
                decrypt_output.append(new_letter)
        print(decrypt_output)
        return decrypt_output



