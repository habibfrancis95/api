from exceptions.responseCodes import ResponseCodes

class ResponseMessages:
    english = {
        ResponseCodes.success : "Success !!",
        ResponseCodes.generalError : "Unexpected error occured",
        ResponseCodes.categoryIdInvalid : "Empty or invalid category id",
        ResponseCodes.itemIdInvalid : "Empty or invalid item id",
        ResponseCodes.itemPriceInvalid : "Empty or invalid price",
        ResponseCodes.itemNameInvalid : "Empty or invalid name",
        ResponseCodes.categoryNotFound : "Category not found",
        ResponseCodes.itemNotFound : "Item not found",
        ResponseCodes.pageNumberInvalid : "Empty or invalid page number",
        ResponseCodes.pageSizeInvalid : "Empty or invalid page size"

    }