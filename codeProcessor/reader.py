class CodeReader():
    rawCode = ""

    def readCode(self, code):
        isSafe = self.isSafeCode(code)
        if isSafe is False:
            return "print('unsafe code.')"
        else:
            return self.modifiedCode(code)

    def isSafeCode(self, code):
        return True

    def modifiedCode(self, code):
        prefixCode = """
import pandas
import json

rawDataDf = pandas.read_csv(filePath)
processedDf = rawDataDf
"""
        suffixCode = """
locals()['studioResults'] = processedDf
        """
        return prefixCode + code + suffixCode
