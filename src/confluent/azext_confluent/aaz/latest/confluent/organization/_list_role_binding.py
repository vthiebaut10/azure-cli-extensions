# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "confluent organization list-role-binding",
)
class ListRoleBinding(AAZCommand):
    """List all the role bindings within a Confluent organization.
    """

    _aaz_info = {
        "version": "2024-02-13",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.confluent/organizations/{}/access/default/listrolebindings", "2024-02-13"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.organization_name = AAZStrArg(
            options=["--organization-name"],
            help="Organization resource name",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "Body"

        _args_schema = cls._args_schema
        _args_schema.search_filters = AAZDictArg(
            options=["--search-filters"],
            arg_group="Body",
            help="Search filters for the request",
        )

        search_filters = cls._args_schema.search_filters
        search_filters.Element = AAZStrArg()
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.AccessListRoleBindings(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class AccessListRoleBindings(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Confluent/organizations/{organizationName}/access/default/listRoleBindings",
                **self.url_parameters
            )

        @property
        def method(self):
            return "POST"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "organizationName", self.ctx.args.organization_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2024-02-13",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("searchFilters", AAZDictType, ".search_filters")

            search_filters = _builder.get(".searchFilters")
            if search_filters is not None:
                search_filters.set_elements(AAZStrType, ".")

            return self.serialize_content(_content_value)

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.data = AAZListType()
            _schema_on_200.kind = AAZStrType()
            _schema_on_200.metadata = AAZObjectType()

            data = cls._schema_on_200.data
            data.Element = AAZObjectType()

            _element = cls._schema_on_200.data.Element
            _element.crn_pattern = AAZStrType()
            _element.id = AAZStrType()
            _element.kind = AAZStrType()
            _element.metadata = AAZObjectType()
            _element.principal = AAZStrType()
            _element.role_name = AAZStrType()

            metadata = cls._schema_on_200.data.Element.metadata
            metadata.created_at = AAZStrType()
            metadata.deleted_at = AAZStrType()
            metadata.resource_name = AAZStrType()
            metadata.self = AAZStrType()
            metadata.updated_at = AAZStrType()

            metadata = cls._schema_on_200.metadata
            metadata.first = AAZStrType()
            metadata.last = AAZStrType()
            metadata.next = AAZStrType()
            metadata.prev = AAZStrType()
            metadata.total_size = AAZIntType()

            return cls._schema_on_200


class _ListRoleBindingHelper:
    """Helper class for ListRoleBinding"""


__all__ = ["ListRoleBinding"]
