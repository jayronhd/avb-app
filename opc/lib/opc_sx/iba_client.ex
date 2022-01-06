defmodule OpcSx.IbaClient do
  use Agent

  alias OpcUA.{NodeId, Client}

  @pid :opc_sx_iba_client_pid

  @config %{ns: 3, s: "V:0.3."}

  defp set_config!(path), do:
    [security_mode: 2, certificate: File.read! path]

  defp cert_config!, do: :opc_sx
    |> Application.app_dir("priv/certificates/iba-client-cert.der")
    |> set_config!

  def start_link(_args) do
    {:ok, pid} = Client.start_link
    :ok = Client.set_config_with_certs pid, cert_config!()
    :ok = Client.connect_by_url pid, url: System.get_env("AVB_IBA_OPC_ADDRESS")
    Process.register pid, @pid
    {:ok, pid}
  end

  defp set_node(id), do:
    NodeId.new ns_index: @config.ns,
      identifier_type: "string",
      identifier: @config.s <> id

  defp read_node_value!(node_id), do:
    Client.read_node_value @pid, node_id

  def read(id) when is_binary(id), do:
    id |> set_node! |> read_node_value!

end