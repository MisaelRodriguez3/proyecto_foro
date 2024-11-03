import createFormData from "./utils/create_formData.js";
import { post_petition, get_petition } from "./service/api.js";
import { warning_alert, error_alert } from "./utils/alerts.js";

let reziseTimeOut;
let width;
let currentTopic = "";
let currentSection = "";

const search_icon = document.getElementById("search-icon")
const search_container = document.querySelector(".search-container")
const logout = document.querySelector(".logout")

const topics = document.querySelectorAll(".topic")
const topics_links = document.querySelectorAll(".topic-link")
const section = document.querySelector(".section")
const section_items = document.querySelectorAll(".section-item")
const section_links = document.querySelectorAll(".section-item a");


window.addEventListener("resize", () => {
    clearTimeout(reziseTimeOut);
    reziseTimeOut = setTimeout(() => {
        width = window.innerWidth
        if(width > 768) {
            search_container.classList.remove("active")
        }
    }, 300)
})

search_icon.addEventListener("click", (e) => {
    width ? width : width = window.innerWidth
    if (width < 768) {
            search_container.classList.toggle("active")
        return
    }

})

topics_links.forEach(topic_link => {
    width ? width : width = window.innerWidth
    if (width < 768) {
        topic_link.addEventListener("click", (e) => {
            e.preventDefault();
    
            topics.forEach(topic => {
                topic.classList.remove("active")
            })
            topics.forEach(topic => {
                if(topic.contains(topic_link)) {
                    topic.classList.add("active")
                    currentTopic = topic_link.getAttribute("data-topic")
                }
            })
            section.classList.add("active")

            section_links.forEach(section_link => {
                section_link.addEventListener("click", () => {
                    currentSection = section_link.getAttribute("data-section");
                    section_link.setAttribute("href", `/${currentTopic}/${currentSection}`);

                });
            });
        })

    }
})

section_items.forEach(li => {
    li.addEventListener("click", () => {
        const link = li.querySelector("a")
        if(link) {
            link.click()
        }
        
    })
})

document.addEventListener("DOMContentLoaded", () => {
    if(logout) {
        logout.addEventListener("click", (e) => {
            e.preventDefault()
            post_petition("logout").then(res => {
                if(res.status !== 200) {
                    return warning_alert(res.message)
                }
                window.location.href = "/"
            }).catch(() => {
                error_alert()
            }) 
        })
    }
})

function setActiveItem() {
    section_items.forEach(li => {
        const link = li.querySelector('a');
        if (link) {
            const linkUrl = new URL(link.href);
            const currentUrl = new URL(window.location.href);
            
            const linkPathParts = linkUrl.pathname.split('/').filter(Boolean); 
            const currentPathParts = currentUrl.pathname.split('/').filter(Boolean);
            
            if (linkPathParts[0] === currentPathParts[0] && linkPathParts[1] === currentPathParts[1]) {
                li.classList.add('active');
            } else {
                li.classList.remove('active');
            }
        }
    });
}

setActiveItem();
