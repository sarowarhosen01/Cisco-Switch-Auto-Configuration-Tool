import asyncio
import telnetlib3

async def main():
    reader, writer = await telnetlib3.open_connection("192.168.31.12",23)
    try:
        writer.write("admin\n")
        writer.write("cisco123\n")
        await asyncio.sleep(0.5)

        writer.write("en\n")
        await asyncio.sleep(0.5)

        writer.write("cisco123\n")
        await asyncio.sleep(0.5)

        writer.write("conf t\n")
        await asyncio.sleep(0.5)

        # BASIC CONFIGURATION

        writer.write("SW1\n")
        await asyncio.sleep(0.5)


        #  CREATE VLANs
        writer.write("vlan 10\n")
        await asyncio.sleep(0.5)

        writer.write("name MANAGEMENT\n")
        await asyncio.sleep(0.5)


        writer.write("vlan 20\n")
        await asyncio.sleep(0.5)

        writer.write("name USERS\n")
        await asyncio.sleep(0.5)


        writer.write("vlan 30\n")
        await asyncio.sleep(0.5)

        writer.write("name SERVERS\n")
        await asyncio.sleep(0.5)

        writer.write("vlan 40\n")
        await asyncio.sleep(0.5)

        writer.write("name VOICE\n")
        await asyncio.sleep(0.5)


        # ACCESS PORT CONFIG


        writer.write("interface range fastethernet 0/1 - 5\n")
        await asyncio.sleep(0.5)

        writer.write("switchport mode access\n")
        await asyncio.sleep(0.5)

        writer.write("switchport access vlan 10\n")
        await asyncio.sleep(0.5)

        writer.write("spanning-tree portfast\n")
        await asyncio.sleep(0.5)

        writer.write("spanning-tree bpduguard enable\n")



        writer.write("interface range fastethernet 0/6 - 10\n")
        await asyncio.sleep(0.5)

        writer.write("switchport mode access\n")
        await asyncio.sleep(0.5)

        writer.write("switchport access vlan 20\n")
        await asyncio.sleep(0.5)

        writer.write("spanning-tree portfast\n")
        await asyncio.sleep(0.5)

        writer.write("spanning-tree bpduguard enable\n")
        await asyncio.sleep(0.5)


        writer.write("interface range fastethernet 0/11 - 15\n")
        await asyncio.sleep(0.5)

        writer.write("switchport mode access\n")
        await asyncio.sleep(0.5)

        writer.write("switchport access vlan 30\n")
        await asyncio.sleep(0.5)

        writer.write("spanning-tree portfast\n")
        await asyncio.sleep(0.5)

        writer.write("spanning-tree bpduguard enable\n")
        await asyncio.sleep(0.5)


        writer.write("interface range fastethernet 0/16 - 20\n")
        await asyncio.sleep(0.5)

        writer.write("switchport mode access\n")
        await asyncio.sleep(0.5)

        writer.write("switchport access vlan 40\n")
        await asyncio.sleep(0.5)

        writer.write("spanning-tree portfast\n")
        await asyncio.sleep(0.5)

        writer.write("spanning-tree bpduguard enable\n")
        await asyncio.sleep(0.5)

        writer.write("Exit\n")
        await asyncio.sleep(0.5)




        # TRUNK PORT CONFIG

        writer.write("interface gigabitethernet 0/1\n")
        await asyncio.sleep(0.5)

        writer.write("switchport trunk encapsulation dot1q\n")
        await asyncio.sleep(0.5)

        writer.write("switchport mode trunk\n")
        await asyncio.sleep(0.5)

        writer.write("switchport trunk allowed vlan 10,20,30,40,99\n")
        await asyncio.sleep(0.5)


        writer.write("end\n")
        await asyncio.sleep(0.5)

        writer.write("exit\n")
        await asyncio.sleep(0.5)

        output = await reader.read()
        if output:
            print(output)



    except asyncio.TimeoutError:
        print("Timeout waiting for device response")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        writer.close()
        await writer.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
