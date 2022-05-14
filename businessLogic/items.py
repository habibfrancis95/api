from helpers.generalHelper import GeneralHelper
from exceptions.responseCodes import ResponseCodes
from exceptions.businessException import BusinessException
from wrappers.generalWrapper import GeneralWrapper
from exceptions.responseMessages import ResponseMessages
from dataAccess.items import ItemsDA
from dataAccess.categories import CategoriesDA
from models.item import Item

class Items:
    @staticmethod
    def addItem(name, price, categoryId):
        try:
            GeneralHelper.checkString(name, ResponseCodes.itemNameInvalid)
            GeneralHelper.checkNumber(price, ResponseCodes.itemPriceInvalid, False)
            GeneralHelper.checkId(categoryId, ResponseCodes.categoryIdInvalid)
            CategoriesDA.get(categoryId)
            insertedId = ItemsDA.add(name, price, categoryId)
            newItem = ItemsDA.get(insertedId)
            return GeneralWrapper.successResult(Item(id=newItem[0], categoryId=newItem[1], name=newItem[2], price=newItem[3]))
        except BusinessException as e:
            return GeneralWrapper.errorResult(e.code, e.message)
        except Exception as e:
            print (e)
            return GeneralWrapper.errorResult(ResponseCodes.generalError, ResponseMessages.english[ResponseCodes.generalError])

    @staticmethod
    def updateItem(id, name, price, categoryId):
        try:
            GeneralHelper.checkString(name, ResponseCodes.itemNameInvalid)
            GeneralHelper.checkNumber(price, ResponseCodes.itemPriceInvalid, False)
            GeneralHelper.checkId(id, ResponseCodes.itemIdInvalid)
            GeneralHelper.checkId(categoryId, ResponseCodes.categoryIdInvalid)
            ItemsDA.get(id)
            CategoriesDA.get(categoryId)
            ItemsDA.update(id, name, price, categoryId)
            updatedItem = ItemsDA.get(id)
            return GeneralWrapper.successResult(Item(id=updatedItem[0], categoryId=updatedItem[1], name=updatedItem[2], price=updatedItem[3]))
        except BusinessException as e:
            return GeneralWrapper.errorResult(e.code, e.message)
        except Exception as e:
            print (e)
            return GeneralWrapper.errorResult(ResponseCodes.generalError, ResponseMessages.english[ResponseCodes.generalError])

    @staticmethod
    def deleteItem(id):
        try:
            GeneralHelper.checkId(id, ResponseCodes.itemIdInvalid)
            ItemsDA.get(id)
            ItemsDA.delete(id)
            return GeneralWrapper.successResult({})
        except BusinessException as e:
            return GeneralWrapper.errorResult(e.code, e.message)
        except Exception as e:
            print (e)
            return GeneralWrapper.errorResult(ResponseCodes.generalError, ResponseMessages.english[ResponseCodes.generalError])

    @staticmethod
    def getItem(id):
        try:
            GeneralHelper.checkId(id, ResponseCodes.itemIdInvalid)
            existedItem = ItemsDA.get(id)
            return GeneralWrapper.successResult(Item(id=existedItem[0], categoryId=existedItem[1], name=existedItem[2], price=existedItem[3]))
        except BusinessException as e:
            return GeneralWrapper.errorResult(e.code, e.message)
        except Exception as e:
            print (e)
            return GeneralWrapper.errorResult(ResponseCodes.generalError, ResponseMessages.english[ResponseCodes.generalError])

    @staticmethod
    def getList(pageSize, pageNumber):
        try:
            GeneralHelper.checkId(pageSize, ResponseCodes.pageSizeInvalid)
            GeneralHelper.checkId(pageNumber, ResponseCodes.pageNumberInvalid)
            resultList = []
            rows = ItemsDA.getList(pageNumber, pageSize)
            if not (rows is None):
                for row in rows:
                    item = Item(id=row[0], categoryId=row[1], name=row[2], price=row[3])
                    resultList.append(item)
            return GeneralWrapper.successResult(resultList)
        except BusinessException as e:
            return GeneralWrapper.errorResult(e.code, e.message)
        except Exception as e:
            print (e)
            return GeneralWrapper.errorResult(ResponseCodes.generalError, ResponseMessages.english[ResponseCodes.generalError])
        


