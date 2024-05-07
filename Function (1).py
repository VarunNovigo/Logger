import json
import re
import os
from datetime import datetime, timedelta
from heapq import nlargest
from collections import defaultdict

# User Login

import re
import json

class login:
    def __init__(self):
        pass

    # User Login (input - username and time)

    def main_search_user_time(self, username, dayss):
      json_file_path = "/content/drive/MyDrive/GPE/log.AUDIT-GSQL"
      json_data = load_json_file(json_file_path)
      regex_pattern = "login succeed"
      # username = "Varun"
      # dayss = 30
      matching_results = self.search_user_time(json_data, regex_pattern)
      if matching_results:
          # return "Matches found:"
          return self.search_user_timee(matching_results, username, dayss)
      else:
          return "No matches found."

    def search_user_time(self, data, pattern):
      matches = []
      for item in data:
        for key, value in item.items():
          if isinstance(value, str):
              match = re.search(pattern, value)
              if match:
                  matches.append(item)
      return matches

    def search_user_timee(self, data, username, dayss):
      ans = [()]
      matches = []
      date = datetime.now().date() - timedelta(days=int(dayss))
      for item in data:
        bool1 = False
        temp_val = {}
        for key, value in item.items():
          if isinstance(value, str):
              match = re.search("userName", key)
              if match:
                match = re.search(username, value)
                if match:
                  bool1 = True
                  temp_val = (key, value)
                  # print((key, value))
          if isinstance(value, str):
              match = re.search("timestamp", key)
              if match :
                datee = datetime.strptime(value[:10], "%Y-%m-%d").date()
                if datee > date and bool1:
                  ans.append(temp_val)
                  ans.append((key, value))
                  # print(temp_val)
                  # print((key, value))
      return ans

# User Login (input - time)

    def main_search_time(self, dayss):
      json_file_path = "/content/drive/MyDrive/GPE/log.AUDIT-GSQL"
      json_data = load_json_file(json_file_path)
      regex_pattern = "login"
      # username = "Varun"
      # dayss = 30
      matching_results = self.search_time(json_data, regex_pattern)
      if matching_results:
          # print("Matches found:")
          return self.search_timee(matching_results, dayss)
      else:
          return("No matches found.")

    def search_time(self,data, pattern):
      matches = []
      for item in data:
        for key, value in item.items():
          if isinstance(value, str):
              match = re.search(pattern, value)
              if match:
                  matches.append(item)
      return matches

    def search_timee(self,data, dayss):
      ans = [()]
      matches = []
      ans
      date = datetime.now().date() - timedelta(days=int(dayss))
      for item in data:
        bool1 = False
        temp_val = {}
        for key, value in item.items():
          if isinstance(value, str):
              match = re.search("userName", key)
              if match:
                # match = re.search(username, value)
                # if match:
                bool1 = True
                temp_val = (key, value)
                  # print((key, value))
          if isinstance(value, str):
              match = re.search("timestamp", key)
              if match :
                datee = datetime.strptime(value[:10], "%Y-%m-%d").date()
                if datee > date and bool1:
                  ans.append(temp_val)
                  ans.append((key, value))
                  # print(temp_val)
                  # print((key, value))
      return ans

# User Login Frequency

    def main_user_login(self, dayss):
      json_file_path = "/content/drive/MyDrive/GPE/log.AUDIT-GSQL"
      json_data = load_json_file(json_file_path)
      regex_pattern = "login succeed"
      matching_results = self.search_count_time(json_data, regex_pattern)
      if matching_results:
        return self.get_count(matching_results, dayss)
      else:
          return"No matches found."

    def search_count_time(self, data, pattern):
      matches = []
      for item in data:
        for key, value in item.items():
          if isinstance(value, str):
              match = re.search(pattern, value)
              if match:
                  matches.append(item)
                  # print(item)
      return matches

    def get_count(self, data, dayss):
      # matches = defaultdict(int)
      matches = {}
      date = datetime.now().date() - timedelta(days=int(dayss))

      for item in data:
        flag1 = False
        flag2 = False
        for key, value in item.items():
          match = re.search(key, "userName")
          if match:
            flag1 = True
            valuee = value
          match = re.search(key, "timestamp")
          if match:
            datee = datetime.strptime(value[:10], "%Y-%m-%d").date()
            if datee > date :
              flag2 = True
            if flag1 and flag2:
              matches[valuee] = matches.get(valuee, 0) + 1
          # print(valuee)
      return matches;
      

def load_json_file(file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data

# Query Latency

class query:
    def __init__(self):
      pass

    def main_query(self, dayss):
      ans_list = []
      json_file_path = "/content/drive/MyDrive/GPE/GUI#1.out"
      top10_latencies = self.get_top10_latencies(json_file_path, dayss)
      # print("Top 10 latencies:")
      for i, data in enumerate(top10_latencies, 1):
        # print(f"{i}. Username: {data['username']}, Query: {self.get_Query(data['path'])}, Latency: {data['latency']}")
        ans_list.append(f"{i}. Username: {data['username']}, Query: {self.get_Query(data['path'])}, Latency: {data['latency']}")
      return ans_list

    def get_top10_latencies(self, file_path, dayss):
      relevant_dicts = []
      with open(file_path, 'r') as file:
          date = datetime.now().date() - timedelta(days=int(dayss))
          for line in file:
              try:
                data = json.loads(line)
              except Exception:
                print()
              datee = datetime.strptime(data['ts'][:10], "%Y-%m-%d").date()
              if "username" in data.keys() and "/api/restpp/query/" in data['path'] and "latency" in data.keys() and datee >= date:
                  relevant_dicts.append(data)

      top10_latencies = nlargest(len(relevant_dicts), relevant_dicts, key=lambda x: int(x["latency"].split("ms")[0]))
      seen_values = set()

      filtered_dict = []
      for item in top10_latencies:
        value = self.get_Query(item['path'])
        if value not in seen_values:
            filtered_dict.append(item)
            seen_values.add(value)
      top10_latencies = nlargest(10, filtered_dict, key=lambda x: int(x["latency"].split("ms")[0]))
      return top10_latencies

    def get_Query(self, path_str):
      return path_str.split("/")[-1]


# CPU Utilization

class cpuUtilization:
    def __init__(self):
      pass

    def main_cpuUtilization(self, dayss, threshold):
      ans = []
      directory = "/content/drive/MyDrive/GPE/gse/log.INFO"
      data = self.topCpuUtil(directory, threshold)
      cnt = 0
      seen_dates = set()
      date = datetime.now().date() - timedelta(days=int(dayss))
      for key, val in data.items():
          if cnt < 10:
              date_string = key
              current_year = datetime.now().year
              date_time_obj = datetime.strptime(f"{current_year} {date_string}", "%Y %m%d %H:%M:%S")
              if date_time_obj.date() > date and date_time_obj.date() not in seen_dates:
                  # print(date_time_obj, ' - ', val, "\n")
                  ans.append(f"{date_time_obj} - {val}, \n")
                  cnt = cnt + 1
                  seen_dates.add(date_time_obj.date())
      return ans

    def topCpuUtil(self, directory, threshold):
      # for root, dirs, files in os.walk(directory):
      #   for file in files:
      #     file_path = os.path.join(root, file)
      #     filename = file_path.split("/")[-1]
      #     match = re.search("^INFO+", filename)
      #     match1 = re.search(".*INFO$", filename)
      #     if match or match1:
      #       try:
              # with open(file_path, "r") as file:
              #   lines = file.readlines()
              # cnt = 0
              # usages = {}
              # ans = {}
              # for item in lines:
              #   if item.find("System_GSystem|GSystemWatcher"):
              #     index = item.find("system CPU")
              #     if index != -1:
              #       usages[item[1:14]] = item[index : index + 19]
              # for key, val in usages.items():
              #   pattern = r"\d+\.\d+"
              #   match = re.search(pattern, val)
              #   if match and float(match.group()) > threshold:
              #     ans[key] = val
              # return ans
      with open(directory, "r") as file:
        lines = file.readlines()
      cnt = 0
      usages = {}
      ans = {}
      for item in lines:
        if item.find("System_GSystem|GSystemWatcher"):
          index = item.find("system CPU")
          if index != -1:
            usages[item[1:14]] = item[index : index + 19]
      for key, val in usages.items():
        pattern = r"\d+\.\d+"
        match = re.search(pattern, val)
        if match and float(match.group()) > threshold:
          ans[key] = val
              # except Exception as e:
              #   print(f"Error reading file {file_path}: {e}")
      return ans


#   Memory Utilization

class memUtilzation:
    def __init__(self):
      pass

    def main_memUtilization(self, dayss, threshold):
      ans = []
      json_file_path = "/content/drive/MyDrive/GPE/gse/log.INFO"
      data = self.topMemUtil(json_file_path, threshold)
      cnt = 0
      seen_dates = set()
      date = datetime.now().date() - timedelta(days=int(dayss))
      for key, val in data.items():
        if cnt < 10:
          date_string = key
          current_year = datetime.now().year
          date_time_obj = datetime.strptime(f"{current_year} {date_string}", "%Y %m%d %H:%M:%S")
          if date_time_obj.date() > date and str(date_time_obj.strftime("%Y-%m-%d")+val) not in seen_dates:
            # print(date_time_obj, ' - ', val, "\n")
            ans.append(f"{date_time_obj} - {val} \n")
            cnt = cnt + 1
            seen_dates.add(str(date_time_obj.strftime("%Y-%m-%d")+val))
      return ans

    def topMemUtil(self, data_file, threshold):
      with open(data_file, "r") as file:
        lines = file.readlines()
      cnt = 0
      usages = {}
      ans = {}
      idx = set()
      for item in lines:
        if item.find("System_GSystem|GSystemWatcher|Health|P") != -1:
          index = item.find("|FreePct|")
          if index != -1:
            usages[item[1:14]] = item[index : index + 11]
      for key, val in usages.items():
        pattern = r"\d+"
        match = re.search(pattern, val)
        value = match.group()
        #print(value)
        if int(value) < threshold:
          ans[key] = val
      return ans


#   User Action input - user and action.

class UserAction:
    def __inti__(self):
      pass

    def main_user_action(self, user, dayss, action):
      json_file_path = "/content/drive/MyDrive/GPE/log.AUDIT-GSQL"
      json_data = load_json_file(json_file_path)
      # user = "Varun"
      # action = "createQuery"
      ans = []
      matching_results = self.search_user_action(json_data, user, dayss, action)
      if matching_results:
          for i, data in enumerate(matching_results, 1):
            ans.append("{i}. Username: {data['userName']}, Timestamp: {data['timestamp']}, Action: {data['actionName']}, Message: {data['message']}")
              # print(f"{i}. Username: {data['userName']}, Timestamp: {data['timestamp']}, Action: {data['actionName']}, Message: {data['message']}")
      else:
          ans.append("No matches found.")
      return ans

    def search_user_action(self, data, pattern1, dayss, pattern2):
        matches = []
        match1 = 0
        match2 = 0
        date = datetime.now().date() - timedelta(days=int(dayss))
        for item in data:
          for key, value in item.items():
            if pattern1 == "All":
              match1 = 1
              break
            match1 = re.search(str(pattern1), str(value))
            if match1:
              break
          for key, value in item.items():
            if pattern2 == "All":
              match2 = 1
              break
            match2 = re.search(str(pattern2), str(value))
            if match2:
              break
          if match1 and match2:
            for key, value in item.items():
              if key == "timestamp" and datetime.strptime(value[:10], "%Y-%m-%d").date() > date:
                matches.append(item)
        return matches

# Top actions
    def most_search_text(self, dayss):
      json_file_path = "/content/drive/MyDrive/GPE/log.AUDIT-GSQL"
      json_data = load_json_file(json_file_path)
      matches = []
      date = datetime.now().date() - timedelta(days=int(dayss))
      for item in json_data:
        for key, value in item.items():
          if key == "timestamp" and datetime.strptime(value[:10], "%Y-%m-%d").date() > date:
            matches.append(item)
      return matches

    def most_user_actions(self, data):
      ans = []
      top5_actions = {}
      for item in data:
        for key, value in item.items():
          if key == "actionName":
            if value in top5_actions:
              top5_actions[value] += 1
            else:
              top5_actions[value] = 1
      cnt = 0
      sorted_dict = dict(sorted(top5_actions.items(), key=lambda item: item[1], reverse=True))
      for val in sorted_dict:
          if cnt >= 5:
            break
          # print(val, ' - ', sorted_dict[val], "\n")
          str = f"{val} - {sorted_dict[val]}"
          ans.append(str)
          cnt += 1
      return ans


# GSE Status

class gseStatus:
  def __init__(self):
    pass
  
  def main_gseStatus(self, dayss):
    directory = "/content/drive/MyDrive/GPE/gse"
    startPattern = "config.cpp:453] queue name:id_request_queue_query topic:Topic: id_requesQ_QUERY"
    stopPattern = " ids_launcher.cpp:93] SIGTERM received"
    return self.search_files(directory, startPattern, stopPattern, dayss)

  def search_files(self, directory, pattern, patternn, dayss):
    ans = {}
    date = datetime.now().date() - timedelta(days=int(dayss))
    for root, dirs, files in os.walk(directory):
      for file in files:
        # Construct the full file path
        file_path = os.path.join(root, file)
        filename = file_path.split("/")[-1]
        match = re.search("^GSE_1+", filename)
        if match:
          try:
            with open(file_path, "r") as file:
              lines = file.readlines()
            flag = False
            for item in lines:
              match = re.search(pattern, item)
              if match:
                flag = True
                break
            if flag:
              for item in lines:
                pattern1 = r"^I\d+"
                match = re.search(pattern1, item)
                if match:
                  current_year = datetime.now().year
                  date_time_obj = datetime.strptime(f"{current_year} {item[1:13]}", "%Y %m%d %H:%M:%S")
                  if not ans.get(date_time_obj.strftime("%m/%d/%Y, %H:%M:%S")) and date_time_obj.date() > date:
                    ans[date_time_obj.strftime("%m/%d/%Y, %H:%M:%S")] =  "started"
                    break
            else:
              for item in lines:
                match = re.search(patternn, item)
              if match:
                flag = True
                break
            if flag:
              for item in lines:
                pattern1 = r"^E\d+"
                match = re.search(pattern1, item)
                if match:
                  current_year = datetime.now().year
                  date_time_obj = datetime.strptime(f"{current_year} {item[1:13]}", "%Y %m%d %H:%M:%S")
                  if not ans.get(date_time_obj.strftime("%m/%d/%Y, %H:%M:%S")) and date_time_obj.date() > date:
                    ans[date_time_obj.strftime("%m/%d/%Y, %H:%M:%S")] =  "stopped"
                    break
          except Exception as e:
              print(f"Error reading file {file_path}: {e}")
    return ans
    # for key, val in ans.items():
    #    print(key, " : ", val, "\n")


# GPE Status

class gpeStatus:
    def __init__(self):
      pass
    
    def main_gpeStatus(self, dayss):
      directory = "/content/drive/MyDrive/GPE/gpe"
      startPattern = "MessageQueue|ZMQContext|Initialized"
      stopPattern = "gcleanup.cpp:169] System_GCleanUp|Finished"
      return self.search_gpe_files(directory, startPattern, stopPattern, dayss)

    def search_gpe_files(self, directory, pattern, patternn, dayss):
      anss = []
      ans = {}
      for root, dirs, files in os.walk(directory):
        for file in files:
          file_path = os.path.join(root, file)
          filename = file_path.split("/")[-1]
          match = re.search("^GPE_1+", filename)
          if match:
            try:
              with open(file_path, "r") as file:
                lines = file.readlines()
              flag = False
              for item in lines:
                match = re.search(pattern, item)
                if match:
                  flag = True
                  break
              if flag:
                for item in lines:
                  pattern1 = r"^I\d+"
                  match = re.search(pattern1, item)
                  if match:
                    current_year = datetime.now().year
                    date_time_obj = datetime.strptime(f"{current_year} {item[1:13]}", "%Y %m%d %H:%M:%S")
                    if not ans.get(date_time_obj):
                      ans[date_time_obj] =  "started"
                      break
              else:
                for item in lines:
                  match = re.search(patternn, item)
                if match:
                  flag = True
                  break
              if flag:
                for item in lines:
                  pattern1 = r"^E\d+"
                  match = re.search(pattern1, item)
                  if match:
                    current_year = datetime.now().year
                    date_time_obj = datetime.strptime(f"{current_year} {item[1:13]}", "%Y %m%d %H:%M:%S")
                    if not ans.get(date_time_obj):
                      ans[date_time_obj] =  "stopped"
                      break
            except Exception as e:
                print(f"Error reading file {file_path}: {e}")
      return ans
      # for key, val in ans.items():
      #   anss.append(f"{key} : {val}")
      #   # print(key, " : ", val, "\n")
      # return anss