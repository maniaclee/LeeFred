ShardTables = {

    'mopay': [{"ip": "192.168.8.44", "role": "alpha", "port": "3306", "table": "mopay"},
              {"ip": "10.66.7.32", "role": "qa", "port": "3306", "table": "mopay"},
              {"ip": "10.2.2.15", "role": "prelease", "port": "3306", "table": "mopay"},
              {"ip": "10.1.110.121", "role": "product", "port": "3306", "table": "mopay"},
              {"ip": "10.1.110.168", "role": "product", "port": "3306", "table": "mopay"}]
    ,
    'huiorder': [{"ip": "192.168.7.106", "role": "alpha", "port": "3306", "table": "HuiOrder0"},
                 {"ip": "10.1.77.106", "role": "qa", "port": "3306", "table": "HuiOrder0"},
                 {"ip": "10.2.15.17", "role": "prelease", "port": "3306", "table": "HuiOrder0"},
                 {"ip": "10.3.10.111", "role": "product", "port": "3306", "table": "HuiOrder0"},
                 {"ip": "10.3.10.113", "role": "product", "port": "3306", "table": "HuiOrder0"},
                 {"ip": "192.168.7.106", "role": "alpha", "port": "3306", "table": "HuiOrder1"},
                 {"ip": "10.1.77.106", "role": "qa", "port": "3306", "table": "HuiOrder1"},
                 {"ip": "10.2.15.17", "role": "prelease", "port": "3306", "table": "HuiOrder1"},
                 {"ip": "10.3.10.114", "role": "product", "port": "3306", "table": "HuiOrder1"},
                 {"ip": "10.3.10.116", "role": "product", "port": "3306", "table": "HuiOrder1"},
                 {"ip": "192.168.7.106", "role": "alpha", "port": "3306", "table": "HuiOrder2"},
                 {"ip": "10.1.77.106", "role": "qa", "port": "3306", "table": "HuiOrder2"},
                 {"ip": "10.2.15.17", "role": "prelease", "port": "3306", "table": "HuiOrder2"},
                 {"ip": "10.3.10.111", "role": "product", "port": "3306", "table": "HuiOrder2"},
                 {"ip": "10.3.10.113", "role": "product", "port": "3306", "table": "HuiOrder2"},
                 {"ip": "192.168.7.105", "role": "alpha", "port": "3306", "table": "HuiOrder3"},
                 {"ip": "10.1.77.106", "role": "qa", "port": "3306", "table": "HuiOrder3"},
                 {"ip": "10.2.15.15", "role": "prelease", "port": "3306", "table": "HuiOrder3"},
                 {"ip": "10.3.10.114", "role": "product", "port": "3306", "table": "HuiOrder3"},
                 {"ip": "10.3.10.116", "role": "product", "port": "3306", "table": "HuiOrder3"},
                 {"ip": "192.168.7.105", "role": "alpha", "port": "3306", "table": "HuiOrder4"},
                 {"ip": "10.1.77.106", "role": "qa", "port": "3306", "table": "HuiOrder4"},
                 {"ip": "10.2.15.15", "role": "prelease", "port": "3306", "table": "HuiOrder4"},
                 {"ip": "10.3.10.111", "role": "product", "port": "3306", "table": "HuiOrder4"},
                 {"ip": "10.3.10.113", "role": "product", "port": "3306", "table": "HuiOrder4"},
                 {"ip": "192.168.7.105", "role": "alpha", "port": "3306", "table": "HuiOrder5"},
                 {"ip": "10.1.77.106", "role": "qa", "port": "3306", "table": "HuiOrder5"},
                 {"ip": "10.2.15.15", "role": "prelease", "port": "3306", "table": "HuiOrder5"},
                 {"ip": "10.3.10.114", "role": "product", "port": "3306", "table": "HuiOrder5"},
                 {"ip": "10.3.10.116", "role": "product", "port": "3306", "table": "HuiOrder5"},
                 {"ip": "192.168.7.105", "role": "alpha", "port": "3306", "table": "HuiOrder6"},
                 {"ip": "10.1.77.106", "role": "qa", "port": "3306", "table": "HuiOrder6"},
                 {"ip": "10.2.15.15", "role": "prelease", "port": "3306", "table": "HuiOrder6"},
                 {"ip": "10.3.10.111", "role": "product", "port": "3306", "table": "HuiOrder6"},
                 {"ip": "10.3.10.113", "role": "product", "port": "3306", "table": "HuiOrder6"},
                 {"ip": "192.168.7.105", "role": "alpha", "port": "3306", "table": "HuiOrder7"},
                 {"ip": "10.1.77.106", "role": "qa", "port": "3306", "table": "HuiOrder7"},
                 {"ip": "10.2.15.15", "role": "prelease", "port": "3306", "table": "HuiOrder7"},
                 {"ip": "10.3.10.114", "role": "product", "port": "3306", "table": "HuiOrder7"},
                 {"ip": "10.3.10.116", "role": "product", "port": "3306", "table": "HuiOrder7"},
                 {"ip": "192.168.7.105", "role": "alpha", "port": "3306", "table": "HuiOrder8"},
                 {"ip": "10.1.77.106", "role": "qa", "port": "3306", "table": "HuiOrder8"},
                 {"ip": "10.2.15.15", "role": "prelease", "port": "3306", "table": "HuiOrder8"},
                 {"ip": "10.3.10.111", "role": "product", "port": "3306", "table": "HuiOrder8"},
                 {"ip": "10.3.10.113", "role": "product", "port": "3306", "table": "HuiOrder8"},
                 {"ip": "192.168.7.105", "role": "alpha", "port": "3306", "table": "HuiOrder9"},
                 {"ip": "10.1.77.106", "role": "qa", "port": "3306", "table": "HuiOrder9"},
                 {"ip": "10.2.15.15", "role": "prelease", "port": "3306", "table": "HuiOrder9"},
                 {"ip": "10.3.10.114", "role": "product", "port": "3306", "table": "HuiOrder9"},
                 {"ip": "10.3.10.116", "role": "product", "port": "3306", "table": "HuiOrder9"},
                 {"ip": "192.168.7.105", "role": "alpha", "port": "3306", "table": "HuiOrder10"},
                 {"ip": "10.1.77.106", "role": "qa", "port": "3306", "table": "HuiOrder10"},
                 {"ip": "10.2.2.14", "role": "prelease", "port": "3306", "table": "HuiOrder10"},
                 {"ip": "10.3.10.111", "role": "product", "port": "3306", "table": "HuiOrder10"},
                 {"ip": "10.3.10.113", "role": "product", "port": "3306", "table": "HuiOrder10"},
                 {"ip": "192.168.7.105", "role": "alpha", "port": "3306", "table": "HuiOrder11"},
                 {"ip": "10.1.77.106", "role": "qa", "port": "3306", "table": "HuiOrder11"},
                 {"ip": "10.2.2.14", "role": "prelease", "port": "3306", "table": "HuiOrder11"},
                 {"ip": "10.3.10.114", "role": "product", "port": "3306", "table": "HuiOrder11"},
                 {"ip": "10.3.10.116", "role": "product", "port": "3306", "table": "HuiOrder11"},
                 {"ip": "192.168.7.105", "role": "alpha", "port": "3306", "table": "HuiOrder12"},
                 {"ip": "10.1.77.106", "role": "qa", "port": "3306", "table": "HuiOrder12"},
                 {"ip": "10.2.2.14", "role": "prelease", "port": "3306", "table": "HuiOrder12"},
                 {"ip": "10.3.10.111", "role": "product", "port": "3306", "table": "HuiOrder12"},
                 {"ip": "10.3.10.113", "role": "product", "port": "3306", "table": "HuiOrder12"},
                 {"ip": "192.168.7.105", "role": "alpha", "port": "3306", "table": "HuiOrder13"},
                 {"ip": "10.1.77.106", "role": "qa", "port": "3306", "table": "HuiOrder13"},
                 {"ip": "10.2.2.14", "role": "prelease", "port": "3306", "table": "HuiOrder13"},
                 {"ip": "10.3.10.114", "role": "product", "port": "3306", "table": "HuiOrder13"},
                 {"ip": "10.3.10.116", "role": "product", "port": "3306", "table": "HuiOrder13"},
                 {"ip": "192.168.7.105", "role": "alpha", "port": "3306", "table": "HuiOrder14"},
                 {"ip": "10.1.77.106", "role": "qa", "port": "3306", "table": "HuiOrder14"},
                 {"ip": "10.2.2.14", "role": "prelease", "port": "3306", "table": "HuiOrder14"},
                 {"ip": "10.3.10.111", "role": "product", "port": "3306", "table": "HuiOrder14"},
                 {"ip": "10.3.10.113", "role": "product", "port": "3306", "table": "HuiOrder14"},
                 {"ip": "192.168.7.105", "role": "alpha", "port": "3306", "table": "HuiOrder15"},
                 {"ip": "10.1.77.106", "role": "qa", "port": "3306", "table": "HuiOrder15"},
                 {"ip": "10.2.2.14", "role": "prelease", "port": "3306", "table": "HuiOrder15"},
                 {"ip": "10.3.10.114", "role": "product", "port": "3306", "table": "HuiOrder15"},
                 {"ip": "10.3.10.116", "role": "product", "port": "3306", "table": "HuiOrder15"},
                 {"ip": "192.168.7.105", "role": "alpha", "port": "3306", "table": "HuiOrder16"},
                 {"ip": "10.1.77.106", "role": "qa", "port": "3306", "table": "HuiOrder16"},
                 {"ip": "10.2.2.14", "role": "prelease", "port": "3306", "table": "HuiOrder16"},
                 {"ip": "10.3.10.111", "role": "product", "port": "3306", "table": "HuiOrder16"},
                 {"ip": "10.3.10.113", "role": "product", "port": "3306", "table": "HuiOrder16"},
                 {"ip": "192.168.7.105", "role": "alpha", "port": "3306", "table": "HuiOrder17"},
                 {"ip": "10.1.77.106", "role": "qa", "port": "3306", "table": "HuiOrder17"},
                 {"ip": "10.2.2.14", "role": "prelease", "port": "3306", "table": "HuiOrder17"},
                 {"ip": "10.3.10.114", "role": "product", "port": "3306", "table": "HuiOrder17"},
                 {"ip": "10.3.10.116", "role": "product", "port": "3306", "table": "HuiOrder17"}],

    'huiorderextra': [{"ip": "10.1.77.106", "role": "qa", "port": "3306", "table": "HuiOrderExtra0"},
                      {"ip": "10.1.77.106", "role": "qa", "port": "3306", "table": "HuiOrderExtra1"},
                      {"ip": "10.1.77.106", "role": "qa", "port": "3306", "table": "HuiOrderExtra2"},
                      {"ip": "10.1.77.106", "role": "qa", "port": "3306", "table": "HuiOrderExtra3"},
                      {"ip": "10.1.77.106", "role": "qa", "port": "3306", "table": "HuiOrderExtra4"},
                      {"ip": "10.1.77.106", "role": "qa", "port": "3306", "table": "HuiOrderExtra5"},
                      {"ip": "10.1.77.106", "role": "qa", "port": "3306", "table": "HuiOrderExtra6"},
                      {"ip": "10.1.77.106", "role": "qa", "port": "3306", "table": "HuiOrderExtra7"},
                      {"ip": "10.1.77.106", "role": "qa", "port": "3306", "table": "HuiOrderExtra8"},
                      {"ip": "10.1.77.106", "role": "qa", "port": "3306", "table": "HuiOrderExtra9"},
                      {"ip": "10.1.77.106", "role": "qa", "port": "3306", "table": "HuiOrderExtra10"},
                      {"ip": "10.1.77.106", "role": "qa", "port": "3306", "table": "HuiOrderExtra11"},
                      {"ip": "10.1.77.106", "role": "qa", "port": "3306", "table": "HuiOrderExtra12"},
                      {"ip": "10.1.77.106", "role": "qa", "port": "3306", "table": "HuiOrderExtra13"},
                      {"ip": "10.1.77.106", "role": "qa", "port": "3306", "table": "HuiOrderExtra14"},
                      {"ip": "10.1.77.106", "role": "qa", "port": "3306", "table": "HuiOrderExtra15"},
                      {"ip": "10.1.77.69", "role": "qa", "port": "3306", "table": "HuiOrderExtra16"},
                      {"ip": "10.1.77.69", "role": "qa", "port": "3306", "table": "HuiOrderExtra17"},
                      {"ip": "10.1.77.69", "role": "qa", "port": "3306", "table": "HuiOrderExtra18"},
                      {"ip": "10.1.77.69", "role": "qa", "port": "3306", "table": "HuiOrderExtra19"},
                      {"ip": "10.1.77.69", "role": "qa", "port": "3306", "table": "HuiOrderExtra20"},
                      {"ip": "10.1.77.69", "role": "qa", "port": "3306", "table": "HuiOrderExtra21"},
                      {"ip": "10.1.77.69", "role": "qa", "port": "3306", "table": "HuiOrderExtra22"},
                      {"ip": "10.1.77.69", "role": "qa", "port": "3306", "table": "HuiOrderExtra23"},
                      {"ip": "10.1.77.69", "role": "qa", "port": "3306", "table": "HuiOrderExtra24"},
                      {"ip": "10.1.77.69", "role": "qa", "port": "3306", "table": "HuiOrderExtra25"},
                      {"ip": "10.1.77.69", "role": "qa", "port": "3306", "table": "HuiOrderExtra26"},
                      {"ip": "10.1.77.69", "role": "qa", "port": "3306", "table": "HuiOrderExtra27"},
                      {"ip": "10.1.77.69", "role": "qa", "port": "3306", "table": "HuiOrderExtra28"},
                      {"ip": "10.1.77.69", "role": "qa", "port": "3306", "table": "HuiOrderExtra29"},
                      {"ip": "10.1.77.69", "role": "qa", "port": "3306", "table": "HuiOrderExtra30"},
                      {"ip": "10.1.77.69", "role": "qa", "port": "3306", "table": "HuiOrderExtra31"}]
}
