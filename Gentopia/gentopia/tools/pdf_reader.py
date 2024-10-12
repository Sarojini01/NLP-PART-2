from typing import AnyStr
from PyPDF2 import PdfReader
from gentopia.tools.basetool import *


class PDFReaderArgs(BaseModel):
    file_path: str = Field(..., description="Path to the PDF file to read")


class PDFReader(BaseTool):
    """Tool that reads and extracts text from a PDF file."""

    name = "pdf_reader"
    description = ("A tool for reading and extracting text from a PDF file."
                   "Input should be the path to the PDF file.")

    args_schema: Optional[Type[BaseModel]] = PDFReaderArgs

    def _run(self, file_path: AnyStr) -> str:
        try:
            # Open the PDF file
            reader = PdfReader(file_path)
            text = ""
            # Extract text from each page
            for page in reader.pages:
                text += page.extract_text()
            return text
        except Exception as e:
            return f"Error reading the PDF file: {e}"

    async def _arun(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError


if __name__ == "__main__":
    ans = PDFReader()._run("sample.pdf")
    print(ans)
