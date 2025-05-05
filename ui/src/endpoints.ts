export const serverRoot = "http://localhost:8080"
export const bookListEndpoint = serverRoot+"/books"
export const bookDetails = (bookUrl: string) => `${serverRoot}+${bookUrl}`