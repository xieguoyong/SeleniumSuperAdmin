from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://uat-admin.dr-elephant.com")
driver.execute_script('sessionStorage.setItem("access_token", "Hfh2MOTud3oRiLlqZf_tES1_LfJJYKkhRiGxt9DU7zHYya8ZQQPA2QzH3q7-fNVMPTwjlpir005Sxw4tZ0QATJzePU__Xhjeolrmdy5JLeWpQroWv7eFpyVpuIt8knSj6sZ4baYfwPKTimhqoVe3UgEEnizYJGITSFrlobWrFm7LMJMqGPDqZSz93zubpbC7XqeMikvlju6JFfFTiLYZUWLTdQ52GyBzOL2VuYIuzjqIGWdSun7uBDSiCpcRC2hltQuV2q_e912GYhfbI9OVRX_1g3wVuGIuCpq7m-bO9I8fv3KOp_Rwm_KXBkkBywd-WDHarS2ci5-43zlHGo8nS4SR3x9YoSWG0AOeXABV6F_4KNnaQ46jK0n03eETVH7UyXrhV3Y1KWyPVLY6pJ6LTuQ4sPsMs_dDbLprGVusXekhlo780HpKYiCwvGpznvilPVIXr2MCySLG1r3zFG4Iz9-agHibHs4o4X--fqJnyD0_xOYLs3lvDkwmbm65WX0lkQAcSSnGE1ZmaODD2eBqZTjmJQNlpERQWpa97CHQ6EioCBhhTocgZFH55kKyN2OXKsaXZtVBQLBCqE1HdWj16w");')
driver.execute_script('sessionStorage.setItem("userName", "superadmin1001");')
driver.execute_script('sessionStorage.setItem("userId", "C7F23885-3442-411B-BF3D-4BC910D3E674");')
driver.execute_script('sessionStorage.setItem("roleName", "3");')

driver.get("https://uat-admin.dr-elephant.com/slide")
driver.refresh()
