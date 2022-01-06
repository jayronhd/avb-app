defmodule OpcSx.PimsClient do
  use Agent

  alias OpcUA.Client

  @pid :opc_sx_pims_client_pid

  def start_link(_args) do
    {:ok, pid} = Client.start_link
    :ok = Client.set_config pid
    :ok = Client.connect_by_url pid, url: System.get_env("AVB_PIMS_OPC_ADDRESS")
    Process.register pid, @pid
    {:ok, pid}
  end

  defp set_node!(id), do:
    NodeId.new identifier_type: "string", identifier: id

  defp read_node_value!(node_id), do:
    Client.read_node_value @pid, id

  def read(id) when is_binary(id), do:
    id |> set_node! |> read_node_value!

end
