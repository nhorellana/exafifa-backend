from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.views import Response, status

from exafifa.spreadsheet import spreadsheets_operations


class ExafifaViewSet(viewsets.GenericViewSet):
    """View set class for the scraper app."""

    @action(detail=False, methods=["GET"])
    def read_table(self, *args, **kwargs):
        """Reads all the cells in the spreadsheet's Liga page. This is mainly useed for populating the table in the frontend."""

        values = spreadsheets_operations("read", "Liga!A1:G1000")
        return Response({"msg": "Éxito!", "data": values}, status=status.HTTP_200_OK)

    @action(detail=False, methods=["POST"])
    def add_result_cells(self, request, *args, **kwargs):
        """Modifies the value of a cell in the spreadsheet's Resultados page."""

        past_results = spreadsheets_operations("read", "Resultados!A1:G1000")
        cell_position = request.data.get("cell_position")
        result = request.data.get("result")
        parsed_results = result.split(",")
        past_results.append(parsed_results)
        print(f"Resultados totales: {past_results}")

        spreadsheets_operations("write", f"Resultados!{cell_position}", past_results)
        return Response(
            {"msg": "Éxito!", "modified_cell": f"Resultados!{cell_position}", "new_value": past_results},
            status=status.HTTP_200_OK,
        )

