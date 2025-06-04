"""
File:    the_internet.py
Author:  Vidal Bickersteth
Date:    12/10/2024
Description: This program simulates the internet server. 
"""

def convert(dict, ip_dict, server):
    """    A function to convert a server into it's ip. vise visa.
            :param dict: The entire internet.
            :param ip_dict: A dictionaries of only ips.
            :param server: The current server.
            :return: The name of the server or it's ip address.
    """   

    if server in dict:
        return server
    elif server in ip_dict:
        return ip_dict[server]
    else:
        return 

def create_server(user_input, dict, ip_dict):
    """    A function to create a brand new server through the use of 2D dictionaries.
            :param user_input: The user's input command.
            :param dict: The entire internet.
            :param ip_dict: A dictionaries of only ips.
            :return: NONE
    """   
    list = user_input.split()
    server = convert(dict, ip_dict, list[2])
    if(server not in dict):
        dict[list[1]] = {"ip":list[2], "Connections":[], "Time":[]}
        ip_dict[list[2]] = list[1]
        print(f"Success: A server with name {list[1]} was created at ip {list[2]}")
    else:
        print("Please try again.")
    

def create_connection(user_input, dict):
    """    A function to create connections between two functions.
            :param user_input: The user's input command.
            :param dict: The entire internet.
            :return: NONE 
    """   
    list = user_input.split()
    if(list[1] in dict and list[2] in dict):
        if(list[1] not in dict[list[2]]["Connections"] and list[2] not in dict[list[1]]["Connections"]):
            dict[list[1]]["Connections"].append(list[2])
            dict[list[1]]["Time"].append(list[3])
            dict[list[2]]["Connections"].append(list[1])
            dict[list[2]]["Time"].append(list[3])
            print(f"Success: A server with the name {list[1]} is now connected to {list[2]}")
        else:
            print("Sorry the servers are already connected.")
    else:
        print("Sorry. one or both of the servers does not exist.")

def set_server(user_input, dict, ip_dict):
    """    A function to set our current place to our server if it exists.
            :param user_input: The user's input command.
            :param dict: The entire internet.
            :param ip_dict: A dictionaries of only ips.
            :return: the server
    """   
    list = user_input.split()
    server = convert(dict, ip_dict, list[1])

    if(server in dict):
        print("Server",server, "selected.")
        return server
    else:
        print("The server does not exist. please try again")
                    

def recursion(dict, server, destination, visited):
    """    A function to display the gameboard, place the frog onto the road, 
                and determine if the frog been hit by a car or not.
            :param dict: The entire internet.
            :param server: the set server that will reach to the destination.
            :param destination: The server or ip address that we want to reach.
            :param visited: the dictionary that is visited. 
            :return: The path that leads to the destination if it exists as well as the time spent.
    """   
    path = [] 
    if server == destination:  
        return [destination], 0

    visited[server] = True
    index = -1
    for next_place in dict[server]['Connections']:
        index += 1
        if not visited[next_place]:
            time = int(dict[server]["Time"][index])
            path, total_time = recursion(dict, next_place, destination, visited)
            if path:
                return [server] + path, total_time + time

    visited[server] = False
    return path, 0

def find(dict, server, destination):
    """    A function to display the gameboard, place the frog onto the road, 
                and determine if the frog been hit by a car or not.
            :param dict: The entire internet.
            :param server: the set server that will reach to the destination.
            :param destination: The server or ip address that we want to reach.
            :return: The actual showcase of the path towards to the destination.
    """   
    visited = {}
    for place in dict:
        visited[place] = False
   
    return recursion(dict, server, destination, visited)

    

def ping(dict, ip_dict, server_, destination_):
    """    A function to print out the time that is needed to reach to the destination.
            :param dict: The entire internet.
            :param ip_dict: A dictionaries of only ips.
            :param server_: the set server that will reach to the destination.
            :param destination_: The server or ip address that we want to reach.
            :return: NONE
    """   
    server = convert(dict, ip_dict, server_)

    destination = convert(dict,ip_dict, destination_)

    if server in dict:
        if destination in dict:
            path, time = find(dict, server, destination)
            if path:
                print(f"Reply from {dict[destination]["ip"]} time = {time} ms")
            else:
                print("Error. There's no connection. Try again!")


def traceroute(dict, server_, ip_dict, destination_):
    """ A function to display the servers as well as the time it takes for the server to get to it's destination.
            :param dict: The entire internet.
            :param server_: the set server that will reach to the destination.
            :param ip_dict: A dictionaries of only ips.
            :param destination_: The server or ip address that we want to reach.
            :return: NONE
    """   
    server = convert(dict, ip_dict, server_)
    destination = convert(dict,ip_dict, destination_)
    time = 0
    if server in dict:
        if destination in dict:
            path, timed = find(dict, server, destination)
            if path:
                print(f"Tracing route to {destination} [{destination_}]")
                hops = 0
                for i in range(len(path)):
                    current_server = path[i]
                    if i == 0:
                        time = 0
                    else:
                        previous = path[i-1]
                        connect = dict[previous]["Connections"]
                        times = dict[previous]["Time"]
                        time -= 1
                        for j in range(len(connect)):
                            if connect[j] == current_server:
                                time = int(times[j])
                    print(f"\t{hops}   {time}   [{dict[current_server]["ip"]}]   {current_server}")
                    hops += 1
                print("Trace complete.")
            else:
                print("Unable to route to target system name", destination)

def config(server, dict):
    """    A function to display our current server and ip address.
            :param dict: The entire internet.
            :param server: The current server.
            :return: NONE
    """   
    for keys in dict.keys():
        if keys == server:
            print(f"{server}   {dict[server]["ip"]}")
        
def display_servers(dict):
    """    A function to display the whole internet, the servers, the servers' connections, and times.
            :param dict: The entire internet as a dictionary.
            :return: NONE
    """   
    for keys in dict:
        print(f"    {keys}     {dict[keys]["ip"]}")
        if("Connections" in dict[keys]):
            for i in range(len(dict[keys]["Connections"])):
                connected_server = dict[keys]["Connections"][i]
                connected_time = dict[keys]["Time"][i]
                print(f"        {connected_server}    {dict[connected_server]["ip"]}   {connected_time}")

def run_the_internet():
    # Ask user's input and based on their inputs, the whole internet, servers, connections, and etc will be created.
    the_internet_server = {}
    ip_dict = {}
    user_input = ""
    server = ""
    while(user_input != "quit"):
        user_input = str(input(">>>"))
        if("create-server" in user_input):
            create_server(user_input, the_internet_server, ip_dict)
        elif("set-server" in user_input):
            server = set_server(user_input, the_internet_server, ip_dict)
        elif("create-connection" in user_input):
            create_connection(user_input, the_internet_server)
        elif("ping" in user_input):
            list = user_input.split()
            ping(the_internet_server, ip_dict, server, list[1])
        elif("traceroute" in user_input or "tracert" in user_input):
            list = user_input.split()
            traceroute(the_internet_server, server, ip_dict, list[1])
        elif("ip-config" == user_input):
            config(server, the_internet_server)
        elif("display-servers" == user_input):
            display_servers(the_internet_server)
            
if __name__ == '__main__':
    # The simulation of running the internet.
    run_the_internet()



