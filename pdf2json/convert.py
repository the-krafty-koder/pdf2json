import logging

from bs4 import BeautifulSoup
from algoliasearch.search_client import SearchClient
from  functools import wraps
from PyPDF2 import PdfFileReader



def sendtoalgolia(app_id, api):

    """Accepts algolia user parameters and sends contents of pdf file into an index as json"""
    logging.basicConfig(level=logging.WARNING)

    @ConvertToJson.to_json
    def send(index_name, generate_ids, pdf_doc):
        client = SearchClient.create(app_id, api)
        index = client.init_index(index_name)
        try:
            index.save_objects(pdf_doc, {'autoGenerateObjectIDIfNotExist': generate_ids}) if isinstance(pdf_doc,type([])) \
                else logging.error("PDF was not converted to JSON, unable to send to Algolia")  # make sure pdf is converted
        except Exception as e:
            return logging.error("Error occurred " + e.__str__())
        return "Index record sent as json"
    return send


class ConvertToJson:
    logging.basicConfig(level=logging.WARNING)

    @staticmethod
    def convert(pdf):

        """Converts a pdf file into plain text"""
        converted_pdf= PdfFileReader(pdf)
        return converted_pdf

    @staticmethod
    def view_plain(self, pdf):
        """Returns plain text pdf in readable form"""

        return BeautifulSoup(self.convert(pdf).get('content'), "html.parser")

    @classmethod
    def to_json(cls, func):

        def get_doc(pdf):

            """Converts text into json"""
            converted = cls.convert(pdf)
            json_doc = [{"page_no":page,"content":converted.getPage(page).extractText()} for page in range(converted.numPages)]
            return json_doc

        @wraps(func)
        def wrapper(*args):

            try:
                f = func(args[0], args[1],get_doc(args[2]))
                return f
            except IndexError:
                return logging.error("Incorrect number of arguments")
            except socket.gaierror:
                return logging.error("Make sure you are connected to the internet")
            except Exception as e:
                return logging.error("Error occured!" + e.__str__())

        return wrapper
