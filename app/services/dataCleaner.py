class DataCleaner:
    def __init__(self, data):
        self.data = data
        self.new_data = []

    def sanitize(self):

        lines = self.data.readlines()
        lines = lines[1:]
        for line in lines:
            line = line.replace("\n", '')
            line = line.split(" ")
            line = [elem for elem in line if elem != ""]
            check_cpf, line[0] = self._verify_cpf(line[0])
            check_private = self._verify_private(line[1])
            check_incomplete = self._verify_incomplete(line[2])
            line[-2] = self._verify_store_freq(line[-2])
            line[-1] = self._verify_last_store(line[-1])
            line[3] = self._verify_date(line[3])
            line[4] = self._verify_currency(line[4])
            line[5] = self._verify_currency(line[5])
            if check_cpf and check_private and check_incomplete:
                self.new_data.append(line)
            else:
                pass
        return self.new_data

    def _verify_cpf(self, cpf: str):
        for ch in ['.', ',', '-', '/']:
            cpf = cpf.replace(ch, '')
        if len(cpf) == 11:
            return True, cpf
        else:
            return False, cpf

    def _verify_private(self, private):
        if ("0" or "1") in private:
            return True
        else:
            return False

    def _verify_incomplete(self, incomplete):
        if ("0" or "1") in incomplete:
            return True
        else:
            return False

    def _verify_store_freq(self, data):
        for ch in ['.', ',', '-', '/']:
            data = data.replace(ch, '')
        return data

    def _verify_last_store(self, data):
        for ch in ['.', ',', '-', '/']:
            data = data.replace(ch, '')
        return data

    def _verify_date(self, data):
        data = data.replace("-", "")
        return data

    def _verify_currency(self, data):
        data = data.replace(",", ".")
        return data


