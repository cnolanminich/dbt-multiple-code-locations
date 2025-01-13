from dagster import AssetExecutionContext, AutomationCondition
from dagster_dbt import DbtCliResource, dbt_assets, DagsterDbtTranslator
from typing import Any, Mapping, Optional

from .project import jaffle_shop_project

class CustomDagsterDbtTranslator(DagsterDbtTranslator):
    def get_automation_condition(
        self, dbt_resource_props: Mapping[str, Any]
    ) -> Optional[AutomationCondition]:
        return AutomationCondition.on_cron("* * * * *")
    
@dbt_assets(manifest=jaffle_shop_project.manifest_path,
            select="customers orders",
            dagster_dbt_translator=CustomDagsterDbtTranslator(),
            )
def jaffle_shop_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()
    