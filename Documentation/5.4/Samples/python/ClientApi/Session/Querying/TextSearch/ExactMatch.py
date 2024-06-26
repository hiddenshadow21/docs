from typing import Union, TypeVar

from ravendb import WhereParams, DocumentQuery, MethodCall

from examples_base import ExampleBase, Employee, Order

_T = TypeVar("_T")


class ExactMatch(ExampleBase):
    def setUp(self):
        super().setUp()

    def test_example(self):
        with self.embedded_server.get_document_store("ExactMatch") as store:
            with store.open_session() as session:
                # region exact_1
                employees = list(
                    session.
                    # Make a query on 'Employees' collection
                    query(object_type=Employee)
                    # Query for all documents where 'FirstName' equals 'Robert'
                    # Pass 'exact=True' for a case-sensitive match
                    .where_equals("FirstName", "Robert", exact=True)
                )
                # endregion

            with store.open_session() as session:
                # region exact_4
                orders = list(
                    session
                    # Make a query on 'Orders' collection
                    .query(object_type=Order)
                    # Query for documents that contain at least one order line with 'Teatime Chocolate Biscuits'
                    .where_equals(
                        "Lines[].ProductName",
                        "Teatime Chocolate Biscuits",
                        # Pass 'exact=True' for a case-sensitive match
                        exact=True,
                    )
                )
                # endregion

    class Foo:
        # region syntax
        def where_equals(
            self, field_name: str, value_or_method: Union[object, MethodCall], exact: Optional[bool] = None
        ) -> DocumentQuery[_T]: ...

        # endregion
