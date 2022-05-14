class ResponseCodes:
    #ok 200
    success = '200'

    #internal server error 500
    generalError = '500'

    #bad request 400
    categoryIdInvalid = '400-01'
    itemIdInvalid = '400-02'
    itemPriceInvalid = '400-03'
    itemNameInvalid = '400-04'
    pageNumberInvalid = '400-05'
    pageSizeInvalid = '400-06'
    
    #not found 404
    categoryNotFound = '404-01'
    itemNotFound = '404-02'
