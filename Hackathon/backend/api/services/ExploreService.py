class OperationStrategy:
    """
    This class represents a strategy for performing operations on a data source.
    """
    def __init__(self, data_source: DataSource, session: Session):
        self.data_source = data_source
        self.session = session

    def operate(self, specification: Specification) -> List[Book]:
        query = self.session.query(Book)
        return self.data_source.search(specification, query)

class BrowseStrategy(OperationStrategy):
    def operate(self, specification: Specification) -> List[Book]:
        query = self.session.query(Book)
        return self.data_source.browse(specification, query)