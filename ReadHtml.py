from requests import head
from Config import *

class ReadHtml(Variables):
    def __init__(self, firstPageUrl):
        Variables.__init__(self, firstPageUrl)


    def ReadHtmlOnlineBlocked(self, url) -> str:
        """
        This method is basically using the request module to get the HTML un-pure text
        From the url Provided in the arguments

        The needed arguments are as the following:
            1- URL --> The url of the page you want to read its html. 
        """

        head = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
        }
        # loop Var
        self.cfBool = True

        # Control Flow
        while self.cfBool:
            try:
                # Please delete that header next time you use ......[]
                self.pureHtml = REQ.get(url, headers=head, timeout= 10)
                if self.pureHtml.text == self.textHtml:
                    self.pureHtml = '<!DOCTYPE html> <html lang="en"> <head> <meta charset="UTF-8"> <meta http-equiv="X-UA-Compatible" content="IE=edge"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <title>Document</title> </head> <body> </body> </html>'
                    pass
                self.cfBool = False
                break
            except (ConnectionAbortedError, ConnectionError) as error:
                print(error)
                print("Connection Error Happened While trying to connect to the website | ReadHml Method")
                # self.cfBool = int(input("Please Enter 1 for Continuing the loop (Try again),\n or 0 for ending the loop and go on with the error: "))
                self.cfBool = 0
            except BaseException as error:
                print(error)
                print("Base Error Happened While trying to connect to the website | ReadHml Method")
                # self.cfBool = int(input("Please Enter 1 for Continuing the loop (Try again),\n or 0 for ending the loop and go on with the error: "))
                self.cfBool = 0

        # Return 
        return self.pureHtml

# /////////////////////////////////////NEW Method/////////////////////////////////////////////

    def ReadHtmlOnline(self, url,) -> str:
        """
        This method is basically using the request module to get the HTML un-pure text
        From the url Provided in the arguments

        The needed arguments are as the following:
            1- URL --> The url of the page you want to read its html. 
        """
        # loop Var
        self.cfBool = True

        # Control Flow
        while self.cfBool:
            try:
                self.pureHtml = REQ.get(url, timeout= 10)
                self.cfBool = False
                break
            except (ConnectionAbortedError, ConnectionError) as error:
                print(error)
                print("Connection Error Happened While trying to connect to the website | ReadHml Method")
                # self.cfBool = int(input("Please Enter 1 for Continuing the loop (Try again),\n or 0 for ending the loop and go on with the error: "))
                self.cfBool = 0
            except BaseException as error:
                print(error)
                print("Base Error Happened While trying to connect to the website | ReadHml Method")
                # self.cfBool = int(input("Please Enter 1 for Continuing the loop (Try again),\n or 0 for ending the loop and go on with the error: "))
                self.cfBool = 0

        # Return 
        return self.pureHtml

# /////////////////////////////////////NEW Method/////////////////////////////////////////////


    def htmlToText(self, pureHtml):
        """
        This loop is basically working on doing only one jop, which is 
        converting the un-pure read html from the ReadHtmlOnline method
        to text that we can parse / beautify later using Beautifulsoup

        The needed arguments are as the following:
            1- pureHtml --> The Read HTML from the requests module. 
        """
        
        # Loop Var
        self.cfBool = True

        # Control Flow 
        while self.cfBool:
            try:
                self.textHtml = pureHtml.text
                self.cfBool = False
                break
            except BaseException as error:
                print(error)
                print ("Base Error happened while trying to convert the Pure HTML to text | htmlToText Method ")
                # self.cfBool = int(input("Please Enter 1 for Continuing the loop (Try again),\n or 0 for ending the loop and go on with the error: "))
                self.cfBool = 0
        # Return
        return self.textHtml

# /////////////////////////////////////NEW Method/////////////////////////////////////////////

    def DirectHtmlToTextOnline(self, Url):
        """
        This method takes the url of the website and return back the text pure html text directly
        without passing through two methods.

        The needed arguments are as the following:
            1- URL --> The url of the page you want to read its html. 
        """

        # Loop Var
        self.cfBool = True
        while self.cfBool:
            try:
                self.textHtml = self.htmlToText(self.ReadHtmlOnline(Url))
                break
            except (ConnectionAbortedError, ConnectionError) as error:
                print(error)
                print("Connection Error Happened While trying to connect to the website | DirectHtmlToTextOnline Method")
                # self.cfBool = int(input("Please Enter 1 for Continuing the loop (Try again),\n or 0 for ending the loop and go on with the error: "))
                self.cfBool = 0
            except BaseException as error:
                print(error)
                print("Base Error Happened While trying to connect to the website | DirectHtmlToTextOnline Method")
                # self.cfBool = int(input("Please Enter 1 for Continuing the loop (Try again),\n or 0 for ending the loop and go on with the error: "))
                self.cfBool = 0
        
        # Return
        return self.textHtml


# /////////////////////////////////////NEW Method/////////////////////////////////////////////

    def HtmlParser(self, htmlText, readingMode) -> str:
        # Loop Var
        self.cfBool = True

        # Control Flow 
        while self.cfBool:
            try:
                self.parsedHtml = BS(htmlText, readingMode)
                self.cfBool = False
                break
            except BaseException as error:
                print(error)
                print ("Base Error happened while trying to convert the Pure HTML to text | htmlParser Method ")
                # self.cfBool = int(input("Please Enter 1 for Continuing the loop (Try again),\n or 0 for ending the loop and go on with the error: "))
                self.cfBool = 0
        # Return
        return self.parsedHtml

# /////////////////////////////////////NEW Method/////////////////////////////////////////////

    def DirectHtmlParser(self, Url, readingMode="html.parser"):
        """
        This method takes the url of the website and return back the parsed html directly
        without passing through 3 methods.

        The needed arguments are as the following:
            1- URL --> The url of the page you want to read its html. 
            2- readingMode --> reading mode for parsing html using beautiful soup
        """

        # Loop Var
        self.cfBool = True
        while self.cfBool:
            try:
                self.HtmlParser(self.htmlToText(self.ReadHtmlOnline(Url)), readingMode)
                break
            except (ConnectionAbortedError, ConnectionError) as error:
                print(error)
                print("Connection Error Happened While trying to connect to the website | DirectHtmlToTextOnline Method")
                self.cfBool = int(input("Please Enter 1 for Continuing the loop (Try again),\n or 0 for ending the loop and go on with the error: "))
            except BaseException as error:
                print(error)
                print("Base Error Happened While trying to connect to the website | DirectHtmlToTextOnline Method")
                self.cfBool = int(input("Please Enter 1 for Continuing the loop (Try again),\n or 0 for ending the loop and go on with the error: "))
                self.cfBool = 0

        # Return
        return self.parsedHtml
    
# /////////////////////////////////////NEW Method/////////////////////////////////////////////

    def DirectHtmlParseBlocked(self, Url, readingMode):
        """
        This method takes the url of the website and return back the parsed html directly
        without passing through 3 methods.

        The needed arguments are as the following:
            1- URL --> The url of the page you want to read its html. 
            2- readingMode --> reading mode for parsing html using beautiful soup
        """

        # Loop Var
        self.cfBool = True
        while self.cfBool:
            try:
                self.HtmlParser(self.htmlToText(self.ReadHtmlOnlineBlocked(Url)), readingMode)
                break
            except (ConnectionAbortedError, ConnectionError) as error:
                print(error)
                print("Connection Error Happened While trying to connect to the website | DirectHtmlToTextOnline Method")
                self.cfBool = int(input("Please Enter 1 for Continuing the loop (Try again),\n or 0 for ending the loop and go on with the error: "))
            except BaseException as error:
                print(error)
                print("Base Error Happened While trying to connect to the website | DirectHtmlToTextOnline Method")
                self.cfBool = int(input("Please Enter 1 for Continuing the loop (Try again),\n or 0 for ending the loop and go on with the error: "))
                self.cfBool = 0

        # Return
        return self.parsedHtml