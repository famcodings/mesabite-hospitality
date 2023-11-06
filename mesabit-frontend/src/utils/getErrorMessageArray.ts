export const getErrorMessageArray = (errorBody: any) => {
    // In the case of an array, return it as it is.
    const ret: string[] = []
    if (Array.isArray(errorBody)) {
        for (const error of errorBody) {
            ret.push(error)
        }
        return ret
    }
    // For objects, concatenate the arrays of each key and return the result.
    for (const key in errorBody) {
        const messages: string[] = errorBody[key]
        for (const message of messages) {
            ret.push(message)
        }
    }
    return ret
}
