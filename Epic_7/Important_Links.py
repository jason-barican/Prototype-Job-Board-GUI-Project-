#Software Engineering Course Project Important Links Module
#Group 3
#Cooper Poole
#Christian Chow Quan 
#Jason Barican
#Jian Gong

import tkinter as tk

class CopyrightNoticeFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Create label for the copyright notice
        tk.Label(self, text="Copyright © 2023 Group 3 SE. All rights reserved.\n\n"
                            "This program and its accompanying materials are protected under the copyright laws of United States of America and other countries. \nUnauthorized reproduction, distribution, or modification of this program, or any portion of it, may result in severe civil and criminal penalties, \nand will be prosecuted to the maximum extent possible under the law.\n\n"
                            "INCOLLEGE is a trademark of Group 3 SE. Any use of this trademark without express written permission from Group 3 SE is strictly prohibited.").grid(column=0,row=0)

        # Create back button
        backButton = tk.Button(self, text="Back", command=lambda: controller.show_frame("MainMenu"))
        backButton.grid(row=1,column=0)

class InCollegeAboutFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        tk.Label(self, text="InCollege Features").grid(column=0,row=0)
        tk.Label(self, text="InCollege is a social networking platform designed specifically for college students, alumni, and faculty members. \nWith InCollege, users can create a professional profile, connect with classmates and colleagues, join interest groups, and\n explore career opportunities.").grid(column=0,row=1)
        tk.Label(self, text="One of the main features of InCollege is the ability to connect with other users based on shared interests or career\n aspirations. Users can join or create interest groups focused on specific industries, job functions, or hobbies, making\n it easy to find and connect with like-minded individuals.").grid(column=0,row=2)
        tk.Label(self, text="InCollege also provides a job search feature, where users can search for job opportunities and internships based on \ntheir field of study, location, or career interests. Employers can also use the platform to post job listings and connect\n with potential candidates.").grid(column=0,row=3)
        tk.Label(self, text="Overall, InCollege is a powerful tool for college students and alumni who are looking to expand their professional\n networks and explore career opportunities. Whether you're a recent graduate looking for your first job, or an established\n professional looking to connect with others in your field, InCollege has something to offer.").grid(column=0,row=4)
        
        back_button = tk.Button(self, text="Back", command=lambda: controller.show_frame("MainMenu"))
        back_button.grid(column=0,row=5)

class AccessibilityNoticeFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        tk.Label(self, text="""Accessibility Notice:\n\n
                                InCollege is committed to making our software accessible to all users, regardless of their abilities or disabilities. 
                                Our team has taken great care to ensure that our application is designed to be as user-friendly as possible for all individuals.\n\n
                                Our software provides a range of accessibility features to ensure that users with disabilities can use it easily and effectively. 
                                Some of these features include adjustable font sizes, high contrast modes, support for screen readers, and keyboard shortcuts.\n\n
                                If you have any questions or suggestions for how we can further improve the accessibility of our application, please don't hesitate to contact us. 
                                We welcome your feedback and are committed to ensuring that our software is accessible to all users.""").grid(column=0,row=0)
        
        backButton = tk.Button(self, text="Back", command=lambda: controller.show_frame("MainMenu"))
        backButton.grid(column=0,row=1)
    


class UserAgreementFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        tk.Label(self, text=("""InCollege User Agreement\n
                                Please read this User Agreement carefully before using the InCollege application (the "Application"). By using the Application, 
                                you agree to be bound by the terms and conditions of this Agreement.\n
                                Use of the Application\n
                                The InCollege Application is designed to help users create a professional network and explore career opportunities.
                                By using the Application, you agree to use it only for lawful purposes and in accordance with this Agreement.\n
                                User Conduct\n
                                You agree to use the Application in a responsible manner and to comply with all applicable laws and regulations. You may not 
                                use the Application to engage in any conduct that is prohibited by law or that interferes with the rights of others.\n
                                User Content\n
                                You are solely responsible for any content that you submit to the Application, including your user profile and any comments, messages, or other content 
                                that you post. You agree that you will not post or transmit any content that is unlawful, offensive, defamatory, or otherwise inappropriate.\n
                                Intellectual Property Rights\n
                                All content and materials on the Application, including trademarks, logos, and copyrights, are owned or licensed by InCollege or its affiliates. You 
                                agree not to copy, distribute, or use any of the content or materials on the Application without the prior written consent of InCollege.\n
                                Termination\n
                                InCollege may terminate this Agreement at any time and for any reason, without notice to you. In the event of termination, you must immediately cease 
                                using the Application and delete all copies of the Application from your computer or mobile device.\n
                                Disclaimer of Warranties\n
                                THE APPLICATION IS PROVIDED "AS IS" AND WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, WARRANTIES
                                OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NON-INFRINGEMENT. INCOLLEGE DOES NOT WARRANT THAT THE APPLICATION WILL BE
                                UNINTERRUPTED OR ERROR-FREE, OR THAT ANY DEFECTS WILL BE CORRECTED.
                                Limitation of Liability\n
                                IN NO EVENT WILL INCOLLEGE BE LIABLE TO YOU FOR ANY INDIRECT, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES ARISING OUT OF OR IN 
                                CONNECTION WITH THE APPLICATION, INCLUDING, BUT NOT LIMITED TO, LOST PROFITS, LOSS OF USE, OR DATA LOSS, WHETHER IN AN ACTION IN 
                                CONTRACT, TORT (INCLUDING NEGLIGENCE), OR OTHERWISE, EVEN IF INCOLLEGE HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.
                                Governing Law\n
                                This Agreement shall be governed by and construed in accordance with the laws of the jurisdiction in which InCollege is located, 
                                without regard to its conflict of laws principles.\n
                                Entire Agreement\n\
                                This Agreement constitutes the entire agreement between you and InCollege and supersedes all prior agreements and understandings, whether written or oral.\n
                                By using the InCollege Application, you acknowledge that you have read and understand this User Agreement and agree to be bound by its terms and conditions.""")).grid(column=0,row=0)
        
        backButton = tk.Button(self, text="Back", command=lambda: controller.show_frame("MainMenu"))
        backButton.grid(column=0,row=1)
    


class PrivacyPolicyFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        tk.Label(self, text="""InCollege Privacy Policy\n\nAt InCollege, we take your privacy very seriously. 
                                This Privacy Policy explains how we collect, use, and protect your personal information when you use the InCollege application (the "Application").\n\n
                                1. Collection of Personal Information\n
                                We collect personal information that you voluntarily provide to us when you use the Application, such as your name, email address, and other contact information. 
                                We may also collect information about your use of the Application, such as your browsing history, search queries, and other usage data.\n\n
                                2. Use of Personal Information\n
                                We use your personal information to provide you with the services and features of the Application, 
                                such as creating a professional profile and connecting with other users. We may also use your information to send you promotional and marketing materials, 
                                to improve the Application, and to customize your user experience.\n\n
                                3. Disclosure of Personal Information\n
                                We do not sell, trade, or rent your personal information to third parties. However, we may share your information with our affiliates and service providers, 
                                such as hosting and data processing vendors, for the purpose of operating and improving the Application.\n\n
                                4. Security of Personal Information\n
                                We take reasonable measures to protect your personal information from unauthorized access, disclosure, alteration, or destruction. 
                                We use industry-standard security technologies and procedures to help protect your personal information.\n\n
                                5. Cookies and Similar Technologies\n
                                We may use cookies, web beacons, and other similar technologies to collect information about your use of the Application. 
                                These technologies help us to analyze user behavior and provide a better user experience.\n\n
                                6. Children's Privacy\n
                                The Application is not intended for use by children under the age of 13. We do not knowingly collect personal information from children under the age of 13. 
                                If we become aware that we have collected personal information from a child under the age of 13, we will take steps to delete that information.\n\n
                                7. Changes to this Privacy Policy\n
                                We may update this Privacy Policy from time to time. We will post any changes on this page and indicate the date of the last update. 
                                Your continued use of the Application after any changes to this Privacy Policy will indicate your acceptance of the changes.\n\n
                                8. Contact Us\n
                                If you have any questions or concerns about this Privacy Policy, please contact us at [contact information].\n\n
                                By using the InCollege Application, you acknowledge that you have read and understand this Privacy Policy and agree to our collection, use, 
                                and disclosure of your personal information as described herein.""").pack(padx=10, pady=10)

        GuestControlsButton = tk.Button(self, text="Guest Controls", command=lambda: controller.show_frame("GuestControlsFrame"))
        GuestControlsButton.pack(padx=10, pady=10)

        backButton = tk.Button(self, text="Back", command=lambda: controller.show_frame("MainMenu"))
        backButton.pack(padx=10, pady=10)



class CookiePolicyFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        tk.Label(self, text="""InCollege Cookie Policy\n\n
                                This Cookie Policy explains how InCollege "we" or "us" uses cookies on the InCollege website (the "Website"). 
                                By using the Website, you consent to the use of cookies in accordance with this policy.\n\n
                                What are cookies?\n
                                Cookies are small text files that are placed on your device when you visit the Website. 
                                They allow the Website to remember your preferences and enhance your user experience.\n\n
                                Types of cookies we use\n
                                We use the following types of cookies on the Website:\n\n
                                1. Essential cookies - These cookies are necessary for the Website to function properly. They enable you to navigate the Website and use its features.\n\n
                                2. Performance cookies - These cookies collect information about how you use the Website, such as which pages you visit most often. 
                                They help us to improve the performance of the Website.\n\n
                                3. Functionality cookies - These cookies remember your preferences and enable us to personalize your experience on the Website.\n\n
                                4. Advertising cookies - These cookies are used to deliver personalized advertisements to you based on your interests.\n\n
                                How we use cookies\nWe use cookies to:\n- Remember your preferences and personalize your experience on the Website\n
                                - Improve the performance of the Website\n
                                - Deliver personalized advertisements to you based on your interests\n\n
                                Third-party cookies\n
                                We may allow third-party service providers to place cookies on the Website for the purposes of delivering personalized advertisements to you based on your interests. 
                                These cookies are subject to the privacy policies of the third-party service providers.\n\n
                                Managing cookies\n
                                Most web browsers allow you to manage your cookie preferences. You can set your browser to refuse cookies, or to alert you when cookies are being sent. 
                                However, please note that disabling cookies may impact your ability to use the Website.\n\n
                                Changes to this policy\n
                                We may update this Cookie Policy from time to time. We will post any changes on this page and indicate the date of the last update. 
                                Your continued use of the Website after any changes to this Cookie Policy will indicate your acceptance of the changes.\n\n
                                Contact us\nIf you have any questions or concerns about this Cookie Policy, please contact us at [contact information].""").pack(padx=10, pady=10)
        
        backButton = tk.Button(self, text="Back", command=lambda: controller.show_frame("MainMenu"))
        backButton.pack(padx=10, pady=10)



class CopyrightPolicyFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        tk.Label(self, text="""InCollege Copyright Policy\n\n
                                All content included on the InCollege website, including but not limited to text, graphics, logos, images, 
                                audio clips, video clips, and software, is the property of InCollege or its content suppliers and is protected by United States and international copyright laws. 
                                The compilation of all content on this site is the exclusive property of InCollege and is protected by United States and international copyright laws. \n\n
                                InCollege reserves the right to terminate the accounts of users who infringe upon the intellectual property rights of others. 
                                If you believe that your work has been used on the InCollege website in a way that constitutes copyright infringement, 
                                please contact us at [contact information] with the following information:\n\n
                                - A physical or electronic signature of the person authorized to act on behalf of the owner of the copyright interest;\n
                                - A description of the copyrighted work that you claim has been infringed;\n
                                - A description of where the material that you claim is infringing is located on the site;\n
                                - Your address, telephone number, and email address;\n
                                - A statement by you that you have a good faith belief that the disputed use is not authorized by the copyright owner, its agent, or the law; and\n
                                - A statement by you, made under penalty of perjury, that the above information in your notice is accurate and that you are the copyright owner or 
                                authorized to act on the copyright owner's behalf.\n\n
                                InCollege may revise this Copyright Policy at any time without notice. By using this website, 
                                you are agreeing to be bound by the then-current version of this Copyright Policy.""", bd = 1, relief = "sunken").pack(pady=10)
        
        backButton = tk.Button(self, text="Back", command=lambda: controller.show_frame("MainMenu"))
        backButton.pack(padx=10, pady=10)



class BrandPolicyFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        tk.Label(self, text="""InCollege Brand Policy\n\n
                                1. Ownership of InCollege Brand\n
                                The InCollege brand, including but not limited to the InCollege name, logo, and any other trademarks or service marks used on the InCollege website or applications, 
                                are the property of InCollege. No use of the InCollege brand may be made without the prior written authorization of InCollege.\n\n
                                2. Permitted Use of InCollege Brand\n
                                InCollege allows the use of its brand for certain purposes, including but not limited to the promotion of the InCollege website or applications, 
                                provided that the use complies with the following guidelines:\n
                                - The InCollege brand may only be used in a manner that is consistent with the InCollege mission and values;\n
                                - The InCollege brand must be used in its entirety and may not be altered in any way;\n
                                - The InCollege brand may not be used in a manner that suggests InCollege endorses or is affiliated with any other product or service;\n
                                - The InCollege brand may not be used in a manner that is likely to cause confusion among users or the public;\n
                                - The InCollege brand may not be used in any way that is harmful, defamatory, or otherwise objectionable to InCollege;\n
                                - The InCollege brand may not be used by any third party without the prior written authorization of InCollege.\n\n
                                3. Prohibited Use of InCollege Brand\nThe following uses of the InCollege brand are strictly prohibited:\n
                                - Any use that violates applicable laws or regulations;\n- Any use that is misleading, deceptive, or fraudulent;\n
                                - Any use that is disparaging or damaging to the InCollege brand or its reputation;\n
                                - Any use that is for commercial purposes or in connection with the promotion of a product or service that is not affiliated with InCollege;\n
                                - Any use that is likely to cause confusion or mistake among users or the public.\n\n
                                4. Enforcement of InCollege Brand Policy\n
                                InCollege reserves the right to take legal action to enforce its rights in the InCollege brand, including seeking injunctive relief and damages. 
                                InCollege may also terminate any relationship or agreement with any third party that uses the InCollege brand in violation of this policy.\n\n
                                5. Changes to InCollege Brand Policy\n
                                InCollege may revise this Brand Policy at any time without notice. By using the InCollege brand, 
                                you are agreeing to be bound by the then-current version of this Brand Policy.""").pack(padx=10, pady=10)
        
        backButton = tk.Button(self, text="Back", command=lambda: controller.show_frame("MainMenu"))
        backButton.pack(padx=10, pady=10)
