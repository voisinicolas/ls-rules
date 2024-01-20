def collapse_array(data):
    collapsed = []
    address_keys = ["remote-addresses", "remote-hosts", "remote"]

    for index, item in enumerate(data):
        try:
            address_key_found = None
            for address_key in address_keys:
                if address_key in item:
                    address_key_found = address_key
                    break

            direction = item.get("direction")
            ports = item.get("ports")
            action = item.get("action")
            process = item.get("process")
            protocol = item.get("protocol")
            key = (action, ports, direction, process, protocol, address_key_found)

            # Check if address_key_found exists in the item
            if address_key_found:
                remote_addresses = item.get(address_key_found)
                if remote_addresses is not None:
                    # Remove duplicates from remote_addresses
                    unique_remote_addresses = list(set(remote_addresses))
                    if key not in collapsed:
                        collapsed.append(key)
                        # Initialize with the first unique address
                        collapsed.append(item.copy())
                        collapsed[-1][address_key_found] = [unique_remote_addresses[0]]
                    else:
                        if address_key_found not in collapsed[-1]:
                            collapsed[-1][address_key_found] = []
                            # Append unique remote addresses
                            collapsed[-1][address_key_found].extend(
                                unique_remote_addresses
                            )
        except KeyError as e:
            print(f"Error occurred at rule index: {index}")
            print(f"Rule causing error: {item}")
            raise e

    return [dict(zip(collapsed[::2], collapsed[1::2]))]
