<!DOCTYPE html><html lang="en" class="js-focus-visible js" data-js-focus-visible=""><head>
    
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width,initial-scale=1">
      
        <meta name="description" content="Agent Framework / shim to use Pydantic with LLMs">
      
      
      
        <link rel="canonical" href="https://ai.pydantic.dev/examples/chat-app/">
      
      
        <link rel="prev" href="../stream-whales/">
      
      
        <link rel="next" href="../question-graph/">
      
      
      <link rel="icon" href="../../favicon.ico">
      <meta name="generator" content="mkdocs-1.6.1, mkdocs-material-9.6.5">
    
    
      
        <title>Chat App with FastAPI - PydanticAI</title>
      
    
    
      <link rel="stylesheet" href="../../assets/stylesheets/main.8608ea7d.min.css">
      
        
        <link rel="stylesheet" href="../../assets/stylesheets/palette.06af60db.min.css">
      
      


    
    
      
    
    
      
        
        
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,300i,400,400i,700,700i%7CRoboto+Mono:400,400i,700,700i&amp;display=fallback">
        <style>:root{--md-text-font:"Roboto";--md-code-font:"Roboto Mono"}</style>
      
    
    
      <link rel="stylesheet" href="../../assets/_mkdocstrings.css">
    
      <link rel="stylesheet" href="../../extra/tweaks.css">
    
    <script>__md_scope=new URL("../..",location),__md_hash=e=>[...e].reduce(((e,_)=>(e<<5)-e+_.charCodeAt(0)),0),__md_get=(e,_=localStorage,t=__md_scope)=>JSON.parse(_.getItem(t.pathname+"."+e)),__md_set=(e,_,t=localStorage,a=__md_scope)=>{try{t.setItem(a.pathname+"."+e,JSON.stringify(_))}catch(e){}}</script>
    
      

    
    
      
        <meta property="og:type" content="website">
      
        <meta property="og:title" content="Chat App with FastAPI - PydanticAI">
      
        <meta property="og:description" content="Agent Framework / shim to use Pydantic with LLMs">
      
        <meta property="og:image" content="https://ai.pydantic.dev/assets/images/social/examples/chat-app.png">
      
        <meta property="og:image:type" content="image/png">
      
        <meta property="og:image:width" content="1200">
      
        <meta property="og:image:height" content="630">
      
        <meta property="og:url" content="https://ai.pydantic.dev/examples/chat-app/">
      
        <meta name="twitter:card" content="summary_large_image">
      
        <meta name="twitter:title" content="Chat App with FastAPI - PydanticAI">
      
        <meta name="twitter:description" content="Agent Framework / shim to use Pydantic with LLMs">
      
        <meta name="twitter:image" content="https://ai.pydantic.dev/assets/images/social/examples/chat-app.png">
      
    
    
   <link href="../../assets/stylesheets/glightbox.min.css" rel="stylesheet"><style>
    html.glightbox-open { overflow: initial; height: 100%; }
    .gslide-title { margin-top: 0px; user-select: text; }
    .gslide-desc { color: #666; user-select: text; }
    .gslide-image img { background: white; }
    .gscrollbar-fixer { padding-right: 15px; }
    .gdesc-inner { font-size: 0.75rem; }
    body[data-md-color-scheme="slate"] .gdesc-inner { background: var(--md-default-bg-color);}
    body[data-md-color-scheme="slate"] .gslide-title { color: var(--md-default-fg-color);}
    body[data-md-color-scheme="slate"] .gslide-desc { color: var(--md-default-fg-color);}</style> <script src="../../assets/javascripts/glightbox.min.js"></script><meta name="theme-color" content="#e92063"><meta name="color-scheme" content="light"></head>
  
  
    
    
      
    
    
    
    
    <body dir="ltr" data-md-color-scheme="default" data-md-color-primary="pink" data-md-color-accent="pink" data-md-color-media="(prefers-color-scheme)">
  
    
    <input class="md-toggle" data-md-toggle="drawer" type="checkbox" id="__drawer" autocomplete="off">
    <input class="md-toggle" data-md-toggle="search" type="checkbox" id="__search" autocomplete="off">
    <label class="md-overlay" for="__drawer"></label>
    <div data-md-component="skip">
      
        
        <a href="#chat-app-with-fastapi" class="md-skip">
          Skip to content
        </a>
      
    </div>
    <div data-md-component="announce">
      
    </div>
    
    
      

  

<header class="md-header md-header--shadow" data-md-component="header">
  <nav class="md-header__inner md-grid" aria-label="Header">
    <a href="../.." title="PydanticAI" class="md-header__button md-logo" aria-label="PydanticAI" data-md-component="logo">
      
  <img src="../../img/logo-white.svg" alt="logo">

    </a>
    <label class="md-header__button md-icon" for="__drawer">
      
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M3 6h18v2H3zm0 5h18v2H3zm0 5h18v2H3z"></path></svg>
    </label>
    <div class="md-header__title" data-md-component="header-title">
      <div class="md-header__ellipsis">
        <div class="md-header__topic">
          <span class="md-ellipsis">
            PydanticAI
          </span>
        </div>
        <div class="md-header__topic" data-md-component="header-topic">
          <span class="md-ellipsis">
            
              Chat App with FastAPI
            
          </span>
        </div>
      </div>
    </div>
    
      
        <form class="md-header__option" data-md-component="palette">
  
    
    
    
    <input class="md-option" data-md-color-media="(prefers-color-scheme)" data-md-color-scheme="default" data-md-color-primary="pink" data-md-color-accent="pink" aria-label="Switch to light mode" type="radio" name="__palette" id="__palette_0">
    
      <label class="md-header__button md-icon" title="Switch to light mode" for="__palette_1">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 2a7 7 0 0 0-7 7c0 2.38 1.19 4.47 3 5.74V17a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1v-2.26c1.81-1.27 3-3.36 3-5.74a7 7 0 0 0-7-7M9 21a1 1 0 0 0 1 1h4a1 1 0 0 0 1-1v-1H9z"></path></svg>
      </label>
    
  
    
    
    
    <input class="md-option" data-md-color-media="(prefers-color-scheme: light)" data-md-color-scheme="default" data-md-color-primary="pink" data-md-color-accent="pink" aria-label="Switch to dark mode" type="radio" name="__palette" id="__palette_1">
    
      <label class="md-header__button md-icon" title="Switch to dark mode" for="__palette_2" hidden="">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 2a7 7 0 0 1 7 7c0 2.38-1.19 4.47-3 5.74V17a1 1 0 0 1-1 1H9a1 1 0 0 1-1-1v-2.26C6.19 13.47 5 11.38 5 9a7 7 0 0 1 7-7M9 21v-1h6v1a1 1 0 0 1-1 1h-4a1 1 0 0 1-1-1m3-17a5 5 0 0 0-5 5c0 2.05 1.23 3.81 3 4.58V16h4v-2.42c1.77-.77 3-2.53 3-4.58a5 5 0 0 0-5-5"></path></svg>
      </label>
    
  
    
    
    
    <input class="md-option" data-md-color-media="(prefers-color-scheme: dark)" data-md-color-scheme="slate" data-md-color-primary="pink" data-md-color-accent="pink" aria-label="Switch to system preference" type="radio" name="__palette" id="__palette_2">
    
      <label class="md-header__button md-icon" title="Switch to system preference" for="__palette_0" hidden="">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M9 2c3.87 0 7 3.13 7 7 0 2.38-1.19 4.47-3 5.74V17c0 .55-.45 1-1 1H6c-.55 0-1-.45-1-1v-2.26C3.19 13.47 2 11.38 2 9c0-3.87 3.13-7 7-7M6 21v-1h6v1c0 .55-.45 1-1 1H7c-.55 0-1-.45-1-1M9 4C6.24 4 4 6.24 4 9c0 2.05 1.23 3.81 3 4.58V16h4v-2.42c1.77-.77 3-2.53 3-4.58 0-2.76-2.24-5-5-5m10 9h-2l-3.2 9h1.9l.7-2h3.2l.7 2h1.9zm-2.15 5.65L18 15l1.15 3.65z"></path></svg>
      </label>
    
  
</form>
      
    
    
      <script>var palette=__md_get("__palette");if(palette&&palette.color){if("(prefers-color-scheme)"===palette.color.media){var media=matchMedia("(prefers-color-scheme: light)"),input=document.querySelector(media.matches?"[data-md-color-media='(prefers-color-scheme: light)']":"[data-md-color-media='(prefers-color-scheme: dark)']");palette.color.media=input.getAttribute("data-md-color-media"),palette.color.scheme=input.getAttribute("data-md-color-scheme"),palette.color.primary=input.getAttribute("data-md-color-primary"),palette.color.accent=input.getAttribute("data-md-color-accent")}for(var[key,value]of Object.entries(palette.color))document.body.setAttribute("data-md-color-"+key,value)}</script>
    
    
    
      <label class="md-header__button md-icon" for="__search">
        
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M9.5 3A6.5 6.5 0 0 1 16 9.5c0 1.61-.59 3.09-1.56 4.23l.27.27h.79l5 5-1.5 1.5-5-5v-.79l-.27-.27A6.52 6.52 0 0 1 9.5 16 6.5 6.5 0 0 1 3 9.5 6.5 6.5 0 0 1 9.5 3m0 2C7 5 5 7 5 9.5S7 14 9.5 14 14 12 14 9.5 12 5 9.5 5"></path></svg>
      </label>
      <div class="md-search" role="dialog">
  <label class="md-search__overlay" for="__search"></label>
  <div class="md-search__inner" role="search">
    <form class="md-search__form" name="search">
      <input type="text" id="searchbox" class="md-search__input" name="query" aria-label="Search" placeholder="Search" autocapitalize="off" autocorrect="off" autocomplete="off" spellcheck="false" required="">
      <label class="md-search__icon md-icon" for="__search">

        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M9.5 3A6.5 6.5 0 0 1 16 9.5c0 1.61-.59 3.09-1.56 4.23l.27.27h.79l5 5-1.5 1.5-5-5v-.79l-.27-.27A6.516 6.516 0 0 1 9.5 16 6.5 6.5 0 0 1 3 9.5 6.5 6.5 0 0 1 9.5 3m0 2C7 5 5 7 5 9.5S7 14 9.5 14 14 12 14 9.5 12 5 9.5 5Z"></path></svg>

        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M20 11v2H8l5.5 5.5-1.42 1.42L4.16 12l7.92-7.92L13.5 5.5 8 11h12Z"></path></svg>
      </label>
      <nav class="md-search__options" aria-label="Search">

        <button id="searchbox-clear" type="reset" class="md-search__icon md-icon" title="Clear" aria-label="Clear" tabindex="-1">

          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M19 6.41 17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12 19 6.41Z"></path></svg>
        </button>
      </nav>

        <div class="md-search__suggest"></div>

    </form>
    <div class="md-search__output">
      <div class="md-search__scrollwrap" tabindex="0">
        <div class="md-search-result">
          <div class="md-search-result__meta" id="type-to-start-searching">Type to start searching</div>
          <ol class="md-search-result__list" id="hits" role="presentation" hidden=""></ol>
        </div>
      </div>
    </div>
  </div>
</div>
    
    
      <div class="md-header__source">
        <a href="https://github.com/pydantic/pydantic-ai" title="Go to repository" class="md-source" data-md-component="source">
  <div class="md-source__icon md-icon">
    
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><!--! Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) Copyright 2024 Fonticons, Inc.--><path d="M439.55 236.05 244 40.45a28.87 28.87 0 0 0-40.81 0l-40.66 40.63 51.52 51.52c27.06-9.14 52.68 16.77 43.39 43.68l49.66 49.66c34.23-11.8 61.18 31 35.47 56.69-26.49 26.49-70.21-2.87-56-37.34L240.22 199v121.85c25.3 12.54 22.26 41.85 9.08 55a34.34 34.34 0 0 1-48.55 0c-17.57-17.6-11.07-46.91 11.25-56v-123c-20.8-8.51-24.6-30.74-18.64-45L142.57 101 8.45 235.14a28.86 28.86 0 0 0 0 40.81l195.61 195.6a28.86 28.86 0 0 0 40.8 0l194.69-194.69a28.86 28.86 0 0 0 0-40.81"></path></svg>
  </div>
  <div class="md-source__repository md-source__repository--active">
    pydantic/pydantic-ai
  <ul class="md-source__facts"><li class="md-source__fact md-source__fact--version">v0.0.50</li><li class="md-source__fact md-source__fact--stars">8k</li><li class="md-source__fact md-source__fact--forks">687</li></ul></div>
</a>
      </div>
    
  </nav>
  
</header>
    
    <div class="md-container" data-md-component="container">
      
      
        
          
        
      
      <main class="md-main" data-md-component="main">
        <div class="md-main__inner md-grid">
          
            
              
              <div class="md-sidebar md-sidebar--primary" data-md-component="sidebar" data-md-type="navigation">
                <div class="md-sidebar__scrollwrap">
                  <div class="md-sidebar__inner">
                    



<nav class="md-nav md-nav--primary" aria-label="Navigation" data-md-level="0">
  <label class="md-nav__title" for="__drawer">
    <a href="../.." title="PydanticAI" class="md-nav__button md-logo" aria-label="PydanticAI" data-md-component="logo">
      
  <img src="../../img/logo-white.svg" alt="logo">

    </a>
    PydanticAI
  </label>
  
    <div class="md-nav__source">
      <a href="https://github.com/pydantic/pydantic-ai" title="Go to repository" class="md-source" data-md-component="source">
  <div class="md-source__icon md-icon">
    
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><!--! Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) Copyright 2024 Fonticons, Inc.--><path d="M439.55 236.05 244 40.45a28.87 28.87 0 0 0-40.81 0l-40.66 40.63 51.52 51.52c27.06-9.14 52.68 16.77 43.39 43.68l49.66 49.66c34.23-11.8 61.18 31 35.47 56.69-26.49 26.49-70.21-2.87-56-37.34L240.22 199v121.85c25.3 12.54 22.26 41.85 9.08 55a34.34 34.34 0 0 1-48.55 0c-17.57-17.6-11.07-46.91 11.25-56v-123c-20.8-8.51-24.6-30.74-18.64-45L142.57 101 8.45 235.14a28.86 28.86 0 0 0 0 40.81l195.61 195.6a28.86 28.86 0 0 0 40.8 0l194.69-194.69a28.86 28.86 0 0 0 0-40.81"></path></svg>
  </div>
  <div class="md-source__repository md-source__repository--active">
    pydantic/pydantic-ai
  <ul class="md-source__facts"><li class="md-source__fact md-source__fact--version">v0.0.50</li><li class="md-source__fact md-source__fact--stars">8k</li><li class="md-source__fact md-source__fact--forks">687</li></ul></div>
</a>
    </div>
  
  <ul class="md-nav__list">
    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../.." class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Introduction
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../../install/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Installation
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../../help/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Getting Help
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../../contributing/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Contributing
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../../troubleshooting/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Troubleshooting
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    
    
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
    
    
      
        
        
      
    
    
    <li class="md-nav__item md-nav__item--section md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_6">
        
          
          <label class="md-nav__link" for="__nav_6" id="__nav_6_label" tabindex="">
            
  
  <span class="md-ellipsis">
    Documentation
    
  </span>
  

            <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_6_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_6">
            <span class="md-nav__icon md-icon"></span>
            Documentation
          </label>
          <ul class="md-nav__list">
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../agents/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Agents
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Models
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../dependencies/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Dependencies
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Function Tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../common-tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Common Tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../results/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Results
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../message-history/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Messages and chat history
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../testing/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Unit testing
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../logfire/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Debugging and Monitoring
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../multi-agent-applications/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Multi-agent Applications
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../graph/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Graphs
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../evals/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Evals
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../input/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Image, Audio &amp; Document Input
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    
    
      
        
          
        
      
        
      
        
      
        
      
    
    
      
    
    
    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_6_14">
        
          
          
          <div class="md-nav__link md-nav__container">
            <a href="../../mcp/" class="md-nav__link ">
              
  
  <span class="md-ellipsis">
    MCP
    
  </span>
  

            </a>
            
              
              <label class="md-nav__link " for="__nav_6_14" id="__nav_6_14_label" tabindex="0">
                <span class="md-nav__icon md-icon"></span>
              </label>
            
          </div>
        
        <nav class="md-nav" data-md-level="2" aria-labelledby="__nav_6_14_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_6_14">
            <span class="md-nav__icon md-icon"></span>
            MCP
          </label>
          <ul class="md-nav__list">
            
              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../mcp/client/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Client
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../mcp/server/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Server
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../mcp/run-python/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    MCP Run Python
    
  </span>
  

      </a>
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../cli/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Command Line Interface (CLI)
    
  </span>
  

      </a>
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

    
      
      
  
  
    
  
  
  
    
    
      
        
          
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
    
    
      
        
        
      
    
    
    <li class="md-nav__item md-nav__item--active md-nav__item--section md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_7" checked="">
        
          
          
          <div class="md-nav__link md-nav__container">
            <a href="../" class="md-nav__link ">
              
  
  <span class="md-ellipsis">
    Examples
    
  </span>
  

            </a>
            
              
              <label class="md-nav__link " for="__nav_7" id="__nav_7_label" tabindex="">
                <span class="md-nav__icon md-icon"></span>
              </label>
            
          </div>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_7_label" aria-expanded="true">
          <label class="md-nav__title" for="__nav_7">
            <span class="md-nav__icon md-icon"></span>
            Examples
          </label>
          <ul class="md-nav__list">
            
              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../pydantic-model/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Pydantic Model
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../weather-agent/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Weather agent
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../bank-support/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Bank support
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../sql-gen/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    SQL Generation
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../flight-booking/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Flight booking
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../rag/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    RAG
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../stream-markdown/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Stream markdown
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../stream-whales/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Stream whales
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
    
  
  
  
    <li class="md-nav__item md-nav__item--active">
      
      <input class="md-nav__toggle md-toggle" type="checkbox" id="__toc">
      
      
        
      
      
        <label class="md-nav__link md-nav__link--active" for="__toc">
          
  
  <span class="md-ellipsis">
    Chat App with FastAPI
    
  </span>
  

          <span class="md-nav__icon md-icon"></span>
        </label>
      
      <a href="./" class="md-nav__link md-nav__link--active">
        
  
  <span class="md-ellipsis">
    Chat App with FastAPI
    
  </span>
  

      </a>
      
        

<nav class="md-nav md-nav--secondary" aria-label="Table of contents">
  
  
  
    
  
  
    <label class="md-nav__title" for="__toc">
      <span class="md-nav__icon md-icon"></span>
      Table of contents
    </label>
    <ul class="md-nav__list" data-md-component="toc">
      
        <li class="md-nav__item">
  <a href="#running-the-example" class="md-nav__link">
    <span class="md-ellipsis">
      Running the Example
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#example-code" class="md-nav__link">
    <span class="md-ellipsis">
      Example Code
    </span>
  </a>
  
</li>
      
    </ul>
  
</nav>
      
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../question-graph/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Question Graph
    
  </span>
  

      </a>
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

    
      
      
  
  
  
  
    
    
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
    
    
      
        
        
      
    
    
    <li class="md-nav__item md-nav__item--section md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_8">
        
          
          <label class="md-nav__link" for="__nav_8" id="__nav_8_label" tabindex="">
            
  
  <span class="md-ellipsis">
    API Reference
    
  </span>
  

            <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_8_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_8">
            <span class="md-nav__icon md-icon"></span>
            API Reference
          </label>
          <ul class="md-nav__list">
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/agent/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.agent
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/common_tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.common_tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/result/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.result
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/messages/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.messages
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/exceptions/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.exceptions
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/settings/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.settings
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/usage/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.usage
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/mcp/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.mcp
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/format_as_xml/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.format_as_xml
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/models/base/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/models/openai/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.openai
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/models/anthropic/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.anthropic
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/models/bedrock/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.bedrock
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/models/cohere/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.cohere
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/models/gemini/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.gemini
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/models/groq/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.groq
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/models/instrumented/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.instrumented
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/models/mistral/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.mistral
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/models/test/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.test
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/models/function/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.function
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/models/fallback/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.fallback
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/models/wrapper/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.wrapper
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/providers/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.providers
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/pydantic_graph/graph/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/pydantic_graph/nodes/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.nodes
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/pydantic_graph/persistence/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.persistence
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/pydantic_graph/mermaid/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.mermaid
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/pydantic_graph/exceptions/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.exceptions
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/pydantic_evals/dataset/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.dataset
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/pydantic_evals/evaluators/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.evaluators
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/pydantic_evals/reporting/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.reporting
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/pydantic_evals/otel/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.otel
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/pydantic_evals/generation/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.generation
    
  </span>
  

      </a>
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

    
  </ul>
</nav>
                  </div>
                </div>
              </div>
            
            
              
              <div class="md-sidebar md-sidebar--secondary" data-md-component="sidebar" data-md-type="toc" style="top: 48px;">
                <div class="md-sidebar__scrollwrap" style="height: 474px;">
                  <div class="md-sidebar__inner">
                    

<nav class="md-nav md-nav--secondary" aria-label="Table of contents">
  
  
  
    
  
  
    <label class="md-nav__title" for="__toc">
      <span class="md-nav__icon md-icon"></span>
      Table of contents
    </label>
    <ul class="md-nav__list" data-md-component="toc">
      
        <li class="md-nav__item">
  <a href="#running-the-example" class="md-nav__link">
    <span class="md-ellipsis">
      Running the Example
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#example-code" class="md-nav__link">
    <span class="md-ellipsis">
      Example Code
    </span>
  </a>
  
</li>
      
    </ul>
  
</nav>
                  </div>
                </div>
              </div>
            
          
          
            <div class="md-content" data-md-component="content">
              <article class="md-content__inner md-typeset">
                
                  


  
  


<h1 id="chat-app-with-fastapi">Chat App with FastAPI</h1>
<p>Simple chat app example build with FastAPI.</p>
<p>Demonstrates:</p>
<ul>
<li><a href="../../message-history/">reusing chat history</a></li>
<li><a href="../../message-history/#accessing-messages-from-results">serializing messages</a></li>
<li><a href="../../results/#streamed-results">streaming responses</a></li>
</ul>
<p>This demonstrates storing chat history between requests and using it to give the model context for new responses.</p>
<p>Most of the complex logic here is between <code>chat_app.py</code> which streams the response to the browser,
and <code>chat_app.ts</code> which renders messages in the browser.</p>
<h2 id="running-the-example">Running the Example</h2>
<p>With <a href="../#usage">dependencies installed and environment variables set</a>, run:</p>
<div class="tabbed-set tabbed-alternate" data-tabs="1:2" style="--md-indicator-x: 0px; --md-indicator-width: 50px;"><input checked="checked" id="__tabbed_1_1" name="__tabbed_1" type="radio"><input id="__tabbed_1_2" name="__tabbed_1" type="radio"><div class="tabbed-labels tabbed-labels--linked"><label for="__tabbed_1_1"><a href="#__tabbed_1_1" tabindex="-1">pip</a></label><label for="__tabbed_1_2"><a href="#__tabbed_1_2" tabindex="-1">uv</a></label></div>
<div class="tabbed-content">
<div class="tabbed-block">
<div class="language-bash highlight"><pre id="__code_0"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_0 > code"></button><code>python<span class="w"> </span>-m<span class="w"> </span>pydantic_ai_examples.chat_app
</code></pre></div>
</div>
<div class="tabbed-block">
<div class="language-bash highlight"><pre id="__code_1"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_1 > code"></button><code>uv<span class="w"> </span>run<span class="w"> </span>-m<span class="w"> </span>pydantic_ai_examples.chat_app
</code></pre></div>
</div>
</div>
<div class="tabbed-control tabbed-control--prev" hidden=""><button class="tabbed-button" tabindex="-1" aria-hidden="true"></button></div><div class="tabbed-control tabbed-control--next" hidden=""><button class="tabbed-button" tabindex="-1" aria-hidden="true"></button></div></div>
<p>Then open the app at <a href="http://localhost:8000">localhost:8000</a>.</p>
<p><a class="glightbox" href="../../img/chat-app-example.png" data-type="image" data-width="auto" data-height="auto" data-desc-position="bottom"><img alt="Example conversation" src="../../img/chat-app-example.png" width="2880" height="1416"></a></p>
<h2 id="example-code">Example Code</h2>
<p>Python code that runs the chat app:</p>
<div class="language-python highlight"><span class="filename">chat_app.py</span><pre id="__code_2"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_2 > code"></button><code tabindex="0"><span class="kn">from</span><span class="w"> </span><span class="nn">__future__</span><span class="w"> </span><span class="kn">import</span> <span class="n">annotations</span> <span class="k">as</span> <span class="n">_annotations</span>

<span class="kn">import</span><span class="w"> </span><span class="nn">asyncio</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">json</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">sqlite3</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">collections.abc</span><span class="w"> </span><span class="kn">import</span> <span class="n">AsyncIterator</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">concurrent.futures.thread</span><span class="w"> </span><span class="kn">import</span> <span class="n">ThreadPoolExecutor</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">contextlib</span><span class="w"> </span><span class="kn">import</span> <span class="n">asynccontextmanager</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">dataclasses</span><span class="w"> </span><span class="kn">import</span> <span class="n">dataclass</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">datetime</span><span class="w"> </span><span class="kn">import</span> <span class="n">datetime</span><span class="p">,</span> <span class="n">timezone</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">functools</span><span class="w"> </span><span class="kn">import</span> <span class="n">partial</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pathlib</span><span class="w"> </span><span class="kn">import</span> <span class="n">Path</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">typing</span><span class="w"> </span><span class="kn">import</span> <span class="n">Annotated</span><span class="p">,</span> <span class="n">Any</span><span class="p">,</span> <span class="n">Callable</span><span class="p">,</span> <span class="n">Literal</span><span class="p">,</span> <span class="n">TypeVar</span>

<span class="kn">import</span><span class="w"> </span><span class="nn">fastapi</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">logfire</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">fastapi</span><span class="w"> </span><span class="kn">import</span> <span class="n">Depends</span><span class="p">,</span> <span class="n">Request</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">fastapi.responses</span><span class="w"> </span><span class="kn">import</span> <span class="n">FileResponse</span><span class="p">,</span> <span class="n">Response</span><span class="p">,</span> <span class="n">StreamingResponse</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">typing_extensions</span><span class="w"> </span><span class="kn">import</span> <span class="n">LiteralString</span><span class="p">,</span> <span class="n">ParamSpec</span><span class="p">,</span> <span class="n">TypedDict</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.exceptions</span><span class="w"> </span><span class="kn">import</span> <span class="n">UnexpectedModelBehavior</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.messages</span><span class="w"> </span><span class="kn">import</span> <span class="p">(</span>
    <span class="n">ModelMessage</span><span class="p">,</span>
    <span class="n">ModelMessagesTypeAdapter</span><span class="p">,</span>
    <span class="n">ModelRequest</span><span class="p">,</span>
    <span class="n">ModelResponse</span><span class="p">,</span>
    <span class="n">TextPart</span><span class="p">,</span>
    <span class="n">UserPromptPart</span><span class="p">,</span>
<span class="p">)</span>

<span class="c1"># 'if-token-present' means nothing will be sent (and the example will work) if you don't have logfire configured</span>
<span class="n">logfire</span><span class="o">.</span><span class="n">configure</span><span class="p">(</span><span class="n">send_to_logfire</span><span class="o">=</span><span class="s1">'if-token-present'</span><span class="p">)</span>

<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="s1">'openai:gpt-4o'</span><span class="p">,</span> <span class="n">instrument</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">THIS_DIR</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="vm">__file__</span><span class="p">)</span><span class="o">.</span><span class="n">parent</span>


<span class="nd">@asynccontextmanager</span>
<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">lifespan</span><span class="p">(</span><span class="n">_app</span><span class="p">:</span> <span class="n">fastapi</span><span class="o">.</span><span class="n">FastAPI</span><span class="p">):</span>
    <span class="k">async</span> <span class="k">with</span> <span class="n">Database</span><span class="o">.</span><span class="n">connect</span><span class="p">()</span> <span class="k">as</span> <span class="n">db</span><span class="p">:</span>
        <span class="k">yield</span> <span class="p">{</span><span class="s1">'db'</span><span class="p">:</span> <span class="n">db</span><span class="p">}</span>


<span class="n">app</span> <span class="o">=</span> <span class="n">fastapi</span><span class="o">.</span><span class="n">FastAPI</span><span class="p">(</span><span class="n">lifespan</span><span class="o">=</span><span class="n">lifespan</span><span class="p">)</span>
<span class="n">logfire</span><span class="o">.</span><span class="n">instrument_fastapi</span><span class="p">(</span><span class="n">app</span><span class="p">)</span>


<span class="nd">@app</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'/'</span><span class="p">)</span>
<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">index</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="n">FileResponse</span><span class="p">:</span>
    <span class="k">return</span> <span class="n">FileResponse</span><span class="p">((</span><span class="n">THIS_DIR</span> <span class="o">/</span> <span class="s1">'chat_app.html'</span><span class="p">),</span> <span class="n">media_type</span><span class="o">=</span><span class="s1">'text/html'</span><span class="p">)</span>


<span class="nd">@app</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'/chat_app.ts'</span><span class="p">)</span>
<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">main_ts</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="n">FileResponse</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Get the raw typescript code, it's compiled in the browser, forgive me."""</span>
    <span class="k">return</span> <span class="n">FileResponse</span><span class="p">((</span><span class="n">THIS_DIR</span> <span class="o">/</span> <span class="s1">'chat_app.ts'</span><span class="p">),</span> <span class="n">media_type</span><span class="o">=</span><span class="s1">'text/plain'</span><span class="p">)</span>


<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">get_db</span><span class="p">(</span><span class="n">request</span><span class="p">:</span> <span class="n">Request</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Database</span><span class="p">:</span>
    <span class="k">return</span> <span class="n">request</span><span class="o">.</span><span class="n">state</span><span class="o">.</span><span class="n">db</span>


<span class="nd">@app</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'/chat/'</span><span class="p">)</span>
<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">get_chat</span><span class="p">(</span><span class="n">database</span><span class="p">:</span> <span class="n">Database</span> <span class="o">=</span> <span class="n">Depends</span><span class="p">(</span><span class="n">get_db</span><span class="p">))</span> <span class="o">-&gt;</span> <span class="n">Response</span><span class="p">:</span>
    <span class="n">msgs</span> <span class="o">=</span> <span class="k">await</span> <span class="n">database</span><span class="o">.</span><span class="n">get_messages</span><span class="p">()</span>
    <span class="k">return</span> <span class="n">Response</span><span class="p">(</span>
        <span class="sa">b</span><span class="s1">'</span><span class="se">\n</span><span class="s1">'</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">to_chat_message</span><span class="p">(</span><span class="n">m</span><span class="p">))</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="s1">'utf-8'</span><span class="p">)</span> <span class="k">for</span> <span class="n">m</span> <span class="ow">in</span> <span class="n">msgs</span><span class="p">),</span>
        <span class="n">media_type</span><span class="o">=</span><span class="s1">'text/plain'</span><span class="p">,</span>
    <span class="p">)</span>


<span class="k">class</span><span class="w"> </span><span class="nc">ChatMessage</span><span class="p">(</span><span class="n">TypedDict</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Format of messages sent to the browser."""</span>

    <span class="n">role</span><span class="p">:</span> <span class="n">Literal</span><span class="p">[</span><span class="s1">'user'</span><span class="p">,</span> <span class="s1">'model'</span><span class="p">]</span>
    <span class="n">timestamp</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">content</span><span class="p">:</span> <span class="nb">str</span>


<span class="k">def</span><span class="w"> </span><span class="nf">to_chat_message</span><span class="p">(</span><span class="n">m</span><span class="p">:</span> <span class="n">ModelMessage</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ChatMessage</span><span class="p">:</span>
    <span class="n">first_part</span> <span class="o">=</span> <span class="n">m</span><span class="o">.</span><span class="n">parts</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">m</span><span class="p">,</span> <span class="n">ModelRequest</span><span class="p">):</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">first_part</span><span class="p">,</span> <span class="n">UserPromptPart</span><span class="p">):</span>
            <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">first_part</span><span class="o">.</span><span class="n">content</span><span class="p">,</span> <span class="nb">str</span><span class="p">)</span>
            <span class="k">return</span> <span class="p">{</span>
                <span class="s1">'role'</span><span class="p">:</span> <span class="s1">'user'</span><span class="p">,</span>
                <span class="s1">'timestamp'</span><span class="p">:</span> <span class="n">first_part</span><span class="o">.</span><span class="n">timestamp</span><span class="o">.</span><span class="n">isoformat</span><span class="p">(),</span>
                <span class="s1">'content'</span><span class="p">:</span> <span class="n">first_part</span><span class="o">.</span><span class="n">content</span><span class="p">,</span>
            <span class="p">}</span>
    <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">m</span><span class="p">,</span> <span class="n">ModelResponse</span><span class="p">):</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">first_part</span><span class="p">,</span> <span class="n">TextPart</span><span class="p">):</span>
            <span class="k">return</span> <span class="p">{</span>
                <span class="s1">'role'</span><span class="p">:</span> <span class="s1">'model'</span><span class="p">,</span>
                <span class="s1">'timestamp'</span><span class="p">:</span> <span class="n">m</span><span class="o">.</span><span class="n">timestamp</span><span class="o">.</span><span class="n">isoformat</span><span class="p">(),</span>
                <span class="s1">'content'</span><span class="p">:</span> <span class="n">first_part</span><span class="o">.</span><span class="n">content</span><span class="p">,</span>
            <span class="p">}</span>
    <span class="k">raise</span> <span class="n">UnexpectedModelBehavior</span><span class="p">(</span><span class="sa">f</span><span class="s1">'Unexpected message type for chat app: </span><span class="si">{</span><span class="n">m</span><span class="si">}</span><span class="s1">'</span><span class="p">)</span>


<span class="nd">@app</span><span class="o">.</span><span class="n">post</span><span class="p">(</span><span class="s1">'/chat/'</span><span class="p">)</span>
<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">post_chat</span><span class="p">(</span>
    <span class="n">prompt</span><span class="p">:</span> <span class="n">Annotated</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">fastapi</span><span class="o">.</span><span class="n">Form</span><span class="p">()],</span> <span class="n">database</span><span class="p">:</span> <span class="n">Database</span> <span class="o">=</span> <span class="n">Depends</span><span class="p">(</span><span class="n">get_db</span><span class="p">)</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">StreamingResponse</span><span class="p">:</span>
    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">stream_messages</span><span class="p">():</span>
<span class="w">        </span><span class="sd">"""Streams new line delimited JSON `Message`s to the client."""</span>
        <span class="c1"># stream the user prompt so that can be displayed straight away</span>
        <span class="k">yield</span> <span class="p">(</span>
            <span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span>
                <span class="p">{</span>
                    <span class="s1">'role'</span><span class="p">:</span> <span class="s1">'user'</span><span class="p">,</span>
                    <span class="s1">'timestamp'</span><span class="p">:</span> <span class="n">datetime</span><span class="o">.</span><span class="n">now</span><span class="p">(</span><span class="n">tz</span><span class="o">=</span><span class="n">timezone</span><span class="o">.</span><span class="n">utc</span><span class="p">)</span><span class="o">.</span><span class="n">isoformat</span><span class="p">(),</span>
                    <span class="s1">'content'</span><span class="p">:</span> <span class="n">prompt</span><span class="p">,</span>
                <span class="p">}</span>
            <span class="p">)</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="s1">'utf-8'</span><span class="p">)</span>
            <span class="o">+</span> <span class="sa">b</span><span class="s1">'</span><span class="se">\n</span><span class="s1">'</span>
        <span class="p">)</span>
        <span class="c1"># get the chat history so far to pass as context to the agent</span>
        <span class="n">messages</span> <span class="o">=</span> <span class="k">await</span> <span class="n">database</span><span class="o">.</span><span class="n">get_messages</span><span class="p">()</span>
        <span class="c1"># run the agent with the user prompt and the chat history</span>
        <span class="k">async</span> <span class="k">with</span> <span class="n">agent</span><span class="o">.</span><span class="n">run_stream</span><span class="p">(</span><span class="n">prompt</span><span class="p">,</span> <span class="n">message_history</span><span class="o">=</span><span class="n">messages</span><span class="p">)</span> <span class="k">as</span> <span class="n">result</span><span class="p">:</span>
            <span class="k">async</span> <span class="k">for</span> <span class="n">text</span> <span class="ow">in</span> <span class="n">result</span><span class="o">.</span><span class="n">stream</span><span class="p">(</span><span class="n">debounce_by</span><span class="o">=</span><span class="mf">0.01</span><span class="p">):</span>
                <span class="c1"># text here is a `str` and the frontend wants</span>
                <span class="c1"># JSON encoded ModelResponse, so we create one</span>
                <span class="n">m</span> <span class="o">=</span> <span class="n">ModelResponse</span><span class="p">(</span><span class="n">parts</span><span class="o">=</span><span class="p">[</span><span class="n">TextPart</span><span class="p">(</span><span class="n">text</span><span class="p">)],</span> <span class="n">timestamp</span><span class="o">=</span><span class="n">result</span><span class="o">.</span><span class="n">timestamp</span><span class="p">())</span>
                <span class="k">yield</span> <span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">to_chat_message</span><span class="p">(</span><span class="n">m</span><span class="p">))</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="s1">'utf-8'</span><span class="p">)</span> <span class="o">+</span> <span class="sa">b</span><span class="s1">'</span><span class="se">\n</span><span class="s1">'</span>

        <span class="c1"># add new messages (e.g. the user prompt and the agent response in this case) to the database</span>
        <span class="k">await</span> <span class="n">database</span><span class="o">.</span><span class="n">add_messages</span><span class="p">(</span><span class="n">result</span><span class="o">.</span><span class="n">new_messages_json</span><span class="p">())</span>

    <span class="k">return</span> <span class="n">StreamingResponse</span><span class="p">(</span><span class="n">stream_messages</span><span class="p">(),</span> <span class="n">media_type</span><span class="o">=</span><span class="s1">'text/plain'</span><span class="p">)</span>


<span class="n">P</span> <span class="o">=</span> <span class="n">ParamSpec</span><span class="p">(</span><span class="s1">'P'</span><span class="p">)</span>
<span class="n">R</span> <span class="o">=</span> <span class="n">TypeVar</span><span class="p">(</span><span class="s1">'R'</span><span class="p">)</span>


<span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">Database</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Rudimentary database to store chat messages in SQLite.</span>

<span class="sd">    The SQLite standard library package is synchronous, so we</span>
<span class="sd">    use a thread pool executor to run queries asynchronously.</span>
<span class="sd">    """</span>

    <span class="n">con</span><span class="p">:</span> <span class="n">sqlite3</span><span class="o">.</span><span class="n">Connection</span>
    <span class="n">_loop</span><span class="p">:</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">AbstractEventLoop</span>
    <span class="n">_executor</span><span class="p">:</span> <span class="n">ThreadPoolExecutor</span>

    <span class="nd">@classmethod</span>
    <span class="nd">@asynccontextmanager</span>
    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">connect</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span> <span class="n">file</span><span class="p">:</span> <span class="n">Path</span> <span class="o">=</span> <span class="n">THIS_DIR</span> <span class="o">/</span> <span class="s1">'.chat_app_messages.sqlite'</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AsyncIterator</span><span class="p">[</span><span class="n">Database</span><span class="p">]:</span>
        <span class="k">with</span> <span class="n">logfire</span><span class="o">.</span><span class="n">span</span><span class="p">(</span><span class="s1">'connect to DB'</span><span class="p">):</span>
            <span class="n">loop</span> <span class="o">=</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">get_event_loop</span><span class="p">()</span>
            <span class="n">executor</span> <span class="o">=</span> <span class="n">ThreadPoolExecutor</span><span class="p">(</span><span class="n">max_workers</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
            <span class="n">con</span> <span class="o">=</span> <span class="k">await</span> <span class="n">loop</span><span class="o">.</span><span class="n">run_in_executor</span><span class="p">(</span><span class="n">executor</span><span class="p">,</span> <span class="bp">cls</span><span class="o">.</span><span class="n">_connect</span><span class="p">,</span> <span class="n">file</span><span class="p">)</span>
            <span class="n">slf</span> <span class="o">=</span> <span class="bp">cls</span><span class="p">(</span><span class="n">con</span><span class="p">,</span> <span class="n">loop</span><span class="p">,</span> <span class="n">executor</span><span class="p">)</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="k">yield</span> <span class="n">slf</span>
        <span class="k">finally</span><span class="p">:</span>
            <span class="k">await</span> <span class="n">slf</span><span class="o">.</span><span class="n">_asyncify</span><span class="p">(</span><span class="n">con</span><span class="o">.</span><span class="n">close</span><span class="p">)</span>

    <span class="nd">@staticmethod</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">_connect</span><span class="p">(</span><span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">sqlite3</span><span class="o">.</span><span class="n">Connection</span><span class="p">:</span>
        <span class="n">con</span> <span class="o">=</span> <span class="n">sqlite3</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">file</span><span class="p">))</span>
        <span class="n">con</span> <span class="o">=</span> <span class="n">logfire</span><span class="o">.</span><span class="n">instrument_sqlite3</span><span class="p">(</span><span class="n">con</span><span class="p">)</span>
        <span class="n">cur</span> <span class="o">=</span> <span class="n">con</span><span class="o">.</span><span class="n">cursor</span><span class="p">()</span>
        <span class="n">cur</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span>
            <span class="s1">'CREATE TABLE IF NOT EXISTS messages (id INT PRIMARY KEY, message_list TEXT);'</span>
        <span class="p">)</span>
        <span class="n">con</span><span class="o">.</span><span class="n">commit</span><span class="p">()</span>
        <span class="k">return</span> <span class="n">con</span>

    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">add_messages</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">messages</span><span class="p">:</span> <span class="nb">bytes</span><span class="p">):</span>
        <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_asyncify</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_execute</span><span class="p">,</span>
            <span class="s1">'INSERT INTO messages (message_list) VALUES (?);'</span><span class="p">,</span>
            <span class="n">messages</span><span class="p">,</span>
            <span class="n">commit</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_asyncify</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">con</span><span class="o">.</span><span class="n">commit</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">get_messages</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">list</span><span class="p">[</span><span class="n">ModelMessage</span><span class="p">]:</span>
        <span class="n">c</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_asyncify</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_execute</span><span class="p">,</span> <span class="s1">'SELECT message_list FROM messages order by id'</span>
        <span class="p">)</span>
        <span class="n">rows</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_asyncify</span><span class="p">(</span><span class="n">c</span><span class="o">.</span><span class="n">fetchall</span><span class="p">)</span>
        <span class="n">messages</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">ModelMessage</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">row</span> <span class="ow">in</span> <span class="n">rows</span><span class="p">:</span>
            <span class="n">messages</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">ModelMessagesTypeAdapter</span><span class="o">.</span><span class="n">validate_json</span><span class="p">(</span><span class="n">row</span><span class="p">[</span><span class="mi">0</span><span class="p">]))</span>
        <span class="k">return</span> <span class="n">messages</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">_execute</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">sql</span><span class="p">:</span> <span class="n">LiteralString</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">commit</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">sqlite3</span><span class="o">.</span><span class="n">Cursor</span><span class="p">:</span>
        <span class="n">cur</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">con</span><span class="o">.</span><span class="n">cursor</span><span class="p">()</span>
        <span class="n">cur</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span><span class="n">sql</span><span class="p">,</span> <span class="n">args</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">commit</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">con</span><span class="o">.</span><span class="n">commit</span><span class="p">()</span>
        <span class="k">return</span> <span class="n">cur</span>

    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">_asyncify</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">func</span><span class="p">:</span> <span class="n">Callable</span><span class="p">[</span><span class="n">P</span><span class="p">,</span> <span class="n">R</span><span class="p">],</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">P</span><span class="o">.</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">P</span><span class="o">.</span><span class="n">kwargs</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">R</span><span class="p">:</span>
        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">run_in_executor</span><span class="p">(</span>  <span class="c1"># type: ignore</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_executor</span><span class="p">,</span>
            <span class="n">partial</span><span class="p">(</span><span class="n">func</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">),</span>
            <span class="o">*</span><span class="n">args</span><span class="p">,</span>  <span class="c1"># type: ignore</span>
        <span class="p">)</span>


<span class="k">if</span> <span class="vm">__name__</span> <span class="o">==</span> <span class="s1">'__main__'</span><span class="p">:</span>
    <span class="kn">import</span><span class="w"> </span><span class="nn">uvicorn</span>

    <span class="n">uvicorn</span><span class="o">.</span><span class="n">run</span><span class="p">(</span>
        <span class="s1">'pydantic_ai_examples.chat_app:app'</span><span class="p">,</span> <span class="n">reload</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">reload_dirs</span><span class="o">=</span><span class="p">[</span><span class="nb">str</span><span class="p">(</span><span class="n">THIS_DIR</span><span class="p">)]</span>
    <span class="p">)</span>
</code></pre></div>
<p>Simple HTML page to render the app:</p>
<div class="language-html highlight"><span class="filename">chat_app.html</span><pre id="__code_3"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_3 > code"></button><code tabindex="0"><span class="cp">&lt;!DOCTYPE html&gt;</span>
<span class="p">&lt;</span><span class="nt">html</span> <span class="na">lang</span><span class="o">=</span><span class="s">"en"</span><span class="p">&gt;</span>
<span class="p">&lt;</span><span class="nt">head</span><span class="p">&gt;</span>
  <span class="p">&lt;</span><span class="nt">meta</span> <span class="na">charset</span><span class="o">=</span><span class="s">"UTF-8"</span><span class="p">&gt;</span>
  <span class="p">&lt;</span><span class="nt">meta</span> <span class="na">name</span><span class="o">=</span><span class="s">"viewport"</span> <span class="na">content</span><span class="o">=</span><span class="s">"width=device-width, initial-scale=1.0"</span><span class="p">&gt;</span>
  <span class="p">&lt;</span><span class="nt">title</span><span class="p">&gt;</span>Chat App<span class="p">&lt;/</span><span class="nt">title</span><span class="p">&gt;</span>
  <span class="p">&lt;</span><span class="nt">link</span> <span class="na">href</span><span class="o">=</span><span class="s">"https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"</span> <span class="na">rel</span><span class="o">=</span><span class="s">"stylesheet"</span><span class="p">&gt;</span>
  <span class="p">&lt;</span><span class="nt">style</span><span class="p">&gt;</span>
<span class="w">    </span><span class="nt">main</span><span class="w"> </span><span class="p">{</span>
<span class="w">      </span><span class="k">max-width</span><span class="p">:</span><span class="w"> </span><span class="mi">700</span><span class="kt">px</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>
<span class="w">    </span><span class="p">#</span><span class="nn">conversation</span><span class="w"> </span><span class="p">.</span><span class="nc">user</span><span class="p">::</span><span class="nd">before</span><span class="w"> </span><span class="p">{</span>
<span class="w">      </span><span class="k">content</span><span class="p">:</span><span class="w"> </span><span class="s1">'You asked: '</span><span class="p">;</span>
<span class="w">      </span><span class="k">font-weight</span><span class="p">:</span><span class="w"> </span><span class="kc">bold</span><span class="p">;</span>
<span class="w">      </span><span class="k">display</span><span class="p">:</span><span class="w"> </span><span class="kc">block</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>
<span class="w">    </span><span class="p">#</span><span class="nn">conversation</span><span class="w"> </span><span class="p">.</span><span class="nc">model</span><span class="p">::</span><span class="nd">before</span><span class="w"> </span><span class="p">{</span>
<span class="w">      </span><span class="k">content</span><span class="p">:</span><span class="w"> </span><span class="s1">'AI Response: '</span><span class="p">;</span>
<span class="w">      </span><span class="k">font-weight</span><span class="p">:</span><span class="w"> </span><span class="kc">bold</span><span class="p">;</span>
<span class="w">      </span><span class="k">display</span><span class="p">:</span><span class="w"> </span><span class="kc">block</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>
<span class="w">    </span><span class="p">#</span><span class="nn">spinner</span><span class="w"> </span><span class="p">{</span>
<span class="w">      </span><span class="k">opacity</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="w">      </span><span class="k">transition</span><span class="p">:</span><span class="w"> </span><span class="k">opacity</span><span class="w"> </span><span class="mi">500</span><span class="kt">ms</span><span class="w"> </span><span class="kc">ease-in</span><span class="p">;</span>
<span class="w">      </span><span class="k">width</span><span class="p">:</span><span class="w"> </span><span class="mi">30</span><span class="kt">px</span><span class="p">;</span>
<span class="w">      </span><span class="k">height</span><span class="p">:</span><span class="w"> </span><span class="mi">30</span><span class="kt">px</span><span class="p">;</span>
<span class="w">      </span><span class="k">border</span><span class="p">:</span><span class="w"> </span><span class="mi">3</span><span class="kt">px</span><span class="w"> </span><span class="kc">solid</span><span class="w"> </span><span class="mh">#222</span><span class="p">;</span>
<span class="w">      </span><span class="k">border-bottom-color</span><span class="p">:</span><span class="w"> </span><span class="kc">transparent</span><span class="p">;</span>
<span class="w">      </span><span class="k">border-radius</span><span class="p">:</span><span class="w"> </span><span class="mi">50</span><span class="kt">%</span><span class="p">;</span>
<span class="w">      </span><span class="k">animation</span><span class="p">:</span><span class="w"> </span><span class="n">rotation</span><span class="w"> </span><span class="mi">1</span><span class="kt">s</span><span class="w"> </span><span class="kc">linear</span><span class="w"> </span><span class="kc">infinite</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>
<span class="w">    </span><span class="p">@</span><span class="k">keyframes</span><span class="w"> </span><span class="nt">rotation</span><span class="w"> </span><span class="p">{</span>
<span class="w">      </span><span class="nt">0</span><span class="o">%</span><span class="w"> </span><span class="p">{</span><span class="w"> </span><span class="k">transform</span><span class="p">:</span><span class="w"> </span><span class="nb">rotate</span><span class="p">(</span><span class="mi">0</span><span class="kt">deg</span><span class="p">);</span><span class="w"> </span><span class="p">}</span>
<span class="w">      </span><span class="nt">100</span><span class="o">%</span><span class="w"> </span><span class="p">{</span><span class="w"> </span><span class="k">transform</span><span class="p">:</span><span class="w"> </span><span class="nb">rotate</span><span class="p">(</span><span class="mi">360</span><span class="kt">deg</span><span class="p">);</span><span class="w"> </span><span class="p">}</span>
<span class="w">    </span><span class="p">}</span>
<span class="w">    </span><span class="p">#</span><span class="nn">spinner</span><span class="p">.</span><span class="nc">active</span><span class="w"> </span><span class="p">{</span>
<span class="w">      </span><span class="k">opacity</span><span class="p">:</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>
<span class="w">  </span><span class="p">&lt;/</span><span class="nt">style</span><span class="p">&gt;</span>
<span class="p">&lt;/</span><span class="nt">head</span><span class="p">&gt;</span>
<span class="p">&lt;</span><span class="nt">body</span><span class="p">&gt;</span>
  <span class="p">&lt;</span><span class="nt">main</span> <span class="na">class</span><span class="o">=</span><span class="s">"border rounded mx-auto my-5 p-4"</span><span class="p">&gt;</span>
    <span class="p">&lt;</span><span class="nt">h1</span><span class="p">&gt;</span>Chat App<span class="p">&lt;/</span><span class="nt">h1</span><span class="p">&gt;</span>
    <span class="p">&lt;</span><span class="nt">p</span><span class="p">&gt;</span>Ask me anything...<span class="p">&lt;/</span><span class="nt">p</span><span class="p">&gt;</span>
    <span class="p">&lt;</span><span class="nt">div</span> <span class="na">id</span><span class="o">=</span><span class="s">"conversation"</span> <span class="na">class</span><span class="o">=</span><span class="s">"px-2"</span><span class="p">&gt;&lt;/</span><span class="nt">div</span><span class="p">&gt;</span>
    <span class="p">&lt;</span><span class="nt">div</span> <span class="na">class</span><span class="o">=</span><span class="s">"d-flex justify-content-center mb-3"</span><span class="p">&gt;</span>
      <span class="p">&lt;</span><span class="nt">div</span> <span class="na">id</span><span class="o">=</span><span class="s">"spinner"</span><span class="p">&gt;&lt;/</span><span class="nt">div</span><span class="p">&gt;</span>
    <span class="p">&lt;/</span><span class="nt">div</span><span class="p">&gt;</span>
    <span class="p">&lt;</span><span class="nt">form</span> <span class="na">method</span><span class="o">=</span><span class="s">"post"</span><span class="p">&gt;</span>
      <span class="p">&lt;</span><span class="nt">input</span> <span class="na">id</span><span class="o">=</span><span class="s">"prompt-input"</span> <span class="na">name</span><span class="o">=</span><span class="s">"prompt"</span> <span class="na">class</span><span class="o">=</span><span class="s">"form-control"</span><span class="p">/&gt;</span>
      <span class="p">&lt;</span><span class="nt">div</span> <span class="na">class</span><span class="o">=</span><span class="s">"d-flex justify-content-end"</span><span class="p">&gt;</span>
        <span class="p">&lt;</span><span class="nt">button</span> <span class="na">class</span><span class="o">=</span><span class="s">"btn btn-primary mt-2"</span><span class="p">&gt;</span>Send<span class="p">&lt;/</span><span class="nt">button</span><span class="p">&gt;</span>
      <span class="p">&lt;/</span><span class="nt">div</span><span class="p">&gt;</span>
    <span class="p">&lt;/</span><span class="nt">form</span><span class="p">&gt;</span>
    <span class="p">&lt;</span><span class="nt">div</span> <span class="na">id</span><span class="o">=</span><span class="s">"error"</span> <span class="na">class</span><span class="o">=</span><span class="s">"d-none text-danger"</span><span class="p">&gt;</span>
      Error occurred, check the browser developer console for more information.
    <span class="p">&lt;/</span><span class="nt">div</span><span class="p">&gt;</span>
  <span class="p">&lt;/</span><span class="nt">main</span><span class="p">&gt;</span>
<span class="p">&lt;/</span><span class="nt">body</span><span class="p">&gt;</span>
<span class="p">&lt;/</span><span class="nt">html</span><span class="p">&gt;</span>
<span class="p">&lt;</span><span class="nt">script</span> <span class="na">src</span><span class="o">=</span><span class="s">"https://cdnjs.cloudflare.com/ajax/libs/typescript/5.6.3/typescript.min.js"</span> <span class="na">crossorigin</span><span class="o">=</span><span class="s">"anonymous"</span> <span class="na">referrerpolicy</span><span class="o">=</span><span class="s">"no-referrer"</span><span class="p">&gt;&lt;/</span><span class="nt">script</span><span class="p">&gt;</span>
<span class="p">&lt;</span><span class="nt">script</span> <span class="na">type</span><span class="o">=</span><span class="s">"module"</span><span class="p">&gt;</span>
<span class="w">  </span><span class="c1">// to let me write TypeScript, without adding the burden of npm we do a dirty, non-production-ready hack</span>
<span class="w">  </span><span class="c1">// and transpile the TypeScript code in the browser</span>
<span class="w">  </span><span class="c1">// this is (arguably) A neat demo trick, but not suitable for production!</span>
<span class="w">  </span><span class="k">async</span><span class="w"> </span><span class="kd">function</span><span class="w"> </span><span class="nx">loadTs</span><span class="p">()</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="kd">const</span><span class="w"> </span><span class="nx">response</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">await</span><span class="w"> </span><span class="nx">fetch</span><span class="p">(</span><span class="s1">'/chat_app.ts'</span><span class="p">);</span>
<span class="w">    </span><span class="kd">const</span><span class="w"> </span><span class="nx">tsCode</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">await</span><span class="w"> </span><span class="nx">response</span><span class="p">.</span><span class="nx">text</span><span class="p">();</span>
<span class="w">    </span><span class="kd">const</span><span class="w"> </span><span class="nx">jsCode</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="nb">window</span><span class="p">.</span><span class="nx">ts</span><span class="p">.</span><span class="nx">transpile</span><span class="p">(</span><span class="nx">tsCode</span><span class="p">,</span><span class="w"> </span><span class="p">{</span><span class="w"> </span><span class="nx">target</span><span class="o">:</span><span class="w"> </span><span class="s2">"es2015"</span><span class="w"> </span><span class="p">});</span>
<span class="w">    </span><span class="kd">let</span><span class="w"> </span><span class="nx">script</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="nb">document</span><span class="p">.</span><span class="nx">createElement</span><span class="p">(</span><span class="s1">'script'</span><span class="p">);</span>
<span class="w">    </span><span class="nx">script</span><span class="p">.</span><span class="nx">type</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s1">'module'</span><span class="p">;</span>
<span class="w">    </span><span class="nx">script</span><span class="p">.</span><span class="nx">text</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="nx">jsCode</span><span class="p">;</span>
<span class="w">    </span><span class="nb">document</span><span class="p">.</span><span class="nx">body</span><span class="p">.</span><span class="nx">appendChild</span><span class="p">(</span><span class="nx">script</span><span class="p">);</span>
<span class="w">  </span><span class="p">}</span>

<span class="w">  </span><span class="nx">loadTs</span><span class="p">().</span><span class="k">catch</span><span class="p">((</span><span class="nx">e</span><span class="p">)</span><span class="w"> </span><span class="p">=&gt;</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="nx">console</span><span class="p">.</span><span class="nx">error</span><span class="p">(</span><span class="nx">e</span><span class="p">);</span>
<span class="w">    </span><span class="nb">document</span><span class="p">.</span><span class="nx">getElementById</span><span class="p">(</span><span class="s1">'error'</span><span class="p">).</span><span class="nx">classList</span><span class="p">.</span><span class="nx">remove</span><span class="p">(</span><span class="s1">'d-none'</span><span class="p">);</span>
<span class="w">    </span><span class="nb">document</span><span class="p">.</span><span class="nx">getElementById</span><span class="p">(</span><span class="s1">'spinner'</span><span class="p">).</span><span class="nx">classList</span><span class="p">.</span><span class="nx">remove</span><span class="p">(</span><span class="s1">'active'</span><span class="p">);</span>
<span class="w">  </span><span class="p">});</span>
<span class="p">&lt;/</span><span class="nt">script</span><span class="p">&gt;</span>
</code></pre></div>
<p>TypeScript to handle rendering the messages, to keep this simple (and at the risk of offending frontend developers) the typescript code is passed to the browser as plain text and transpiled in the browser.</p>
<div class="language-ts highlight"><span class="filename">chat_app.ts</span><pre id="__code_4"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_4 > code"></button><code tabindex="0"><span class="c1">// BIG FAT WARNING: to avoid the complexity of npm, this typescript is compiled in the browser</span>
<span class="c1">// there's currently no static type checking</span>

<span class="k">import</span><span class="w"> </span><span class="p">{</span><span class="w"> </span><span class="nx">marked</span><span class="w"> </span><span class="p">}</span><span class="w"> </span><span class="kr">from</span><span class="w"> </span><span class="s1">'https://cdnjs.cloudflare.com/ajax/libs/marked/15.0.0/lib/marked.esm.js'</span>
<span class="kd">const</span><span class="w"> </span><span class="nx">convElement</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="nb">document</span><span class="p">.</span><span class="nx">getElementById</span><span class="p">(</span><span class="s1">'conversation'</span><span class="p">)</span>

<span class="kd">const</span><span class="w"> </span><span class="nx">promptInput</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="nb">document</span><span class="p">.</span><span class="nx">getElementById</span><span class="p">(</span><span class="s1">'prompt-input'</span><span class="p">)</span><span class="w"> </span><span class="kr">as</span><span class="w"> </span><span class="nx">HTMLInputElement</span>
<span class="kd">const</span><span class="w"> </span><span class="nx">spinner</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="nb">document</span><span class="p">.</span><span class="nx">getElementById</span><span class="p">(</span><span class="s1">'spinner'</span><span class="p">)</span>

<span class="c1">// stream the response and render messages as each chunk is received</span>
<span class="c1">// data is sent as newline-delimited JSON</span>
<span class="k">async</span><span class="w"> </span><span class="kd">function</span><span class="w"> </span><span class="nx">onFetchResponse</span><span class="p">(</span><span class="nx">response</span><span class="o">:</span><span class="w"> </span><span class="kt">Response</span><span class="p">)</span><span class="o">:</span><span class="w"> </span><span class="nb">Promise</span><span class="o">&lt;</span><span class="ow">void</span><span class="o">&gt;</span><span class="w"> </span><span class="p">{</span>
<span class="w">  </span><span class="kd">let</span><span class="w"> </span><span class="nx">text</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s1">''</span>
<span class="w">  </span><span class="kd">let</span><span class="w"> </span><span class="nx">decoder</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="ow">new</span><span class="w"> </span><span class="nx">TextDecoder</span><span class="p">()</span>
<span class="w">  </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="nx">response</span><span class="p">.</span><span class="nx">ok</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="kd">const</span><span class="w"> </span><span class="nx">reader</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="nx">response</span><span class="p">.</span><span class="nx">body</span><span class="p">.</span><span class="nx">getReader</span><span class="p">()</span>
<span class="w">    </span><span class="k">while</span><span class="w"> </span><span class="p">(</span><span class="kc">true</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">      </span><span class="kd">const</span><span class="w"> </span><span class="p">{</span><span class="nx">done</span><span class="p">,</span><span class="w"> </span><span class="nx">value</span><span class="p">}</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">await</span><span class="w"> </span><span class="nx">reader</span><span class="p">.</span><span class="nx">read</span><span class="p">()</span>
<span class="w">      </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="nx">done</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="k">break</span>
<span class="w">      </span><span class="p">}</span>
<span class="w">      </span><span class="nx">text</span><span class="w"> </span><span class="o">+=</span><span class="w"> </span><span class="nx">decoder</span><span class="p">.</span><span class="nx">decode</span><span class="p">(</span><span class="nx">value</span><span class="p">)</span>
<span class="w">      </span><span class="nx">addMessages</span><span class="p">(</span><span class="nx">text</span><span class="p">)</span>
<span class="w">      </span><span class="nx">spinner</span><span class="p">.</span><span class="nx">classList</span><span class="p">.</span><span class="nx">remove</span><span class="p">(</span><span class="s1">'active'</span><span class="p">)</span>
<span class="w">    </span><span class="p">}</span>
<span class="w">    </span><span class="nx">addMessages</span><span class="p">(</span><span class="nx">text</span><span class="p">)</span>
<span class="w">    </span><span class="nx">promptInput</span><span class="p">.</span><span class="nx">disabled</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="kc">false</span>
<span class="w">    </span><span class="nx">promptInput</span><span class="p">.</span><span class="nx">focus</span><span class="p">()</span>
<span class="w">  </span><span class="p">}</span><span class="w"> </span><span class="k">else</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="kd">const</span><span class="w"> </span><span class="nx">text</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">await</span><span class="w"> </span><span class="nx">response</span><span class="p">.</span><span class="nx">text</span><span class="p">()</span>
<span class="w">    </span><span class="nx">console</span><span class="p">.</span><span class="nx">error</span><span class="p">(</span><span class="sb">`Unexpected response: </span><span class="si">${</span><span class="nx">response</span><span class="p">.</span><span class="nx">status</span><span class="si">}</span><span class="sb">`</span><span class="p">,</span><span class="w"> </span><span class="p">{</span><span class="nx">response</span><span class="p">,</span><span class="w"> </span><span class="nx">text</span><span class="p">})</span>
<span class="w">    </span><span class="k">throw</span><span class="w"> </span><span class="ow">new</span><span class="w"> </span><span class="ne">Error</span><span class="p">(</span><span class="sb">`Unexpected response: </span><span class="si">${</span><span class="nx">response</span><span class="p">.</span><span class="nx">status</span><span class="si">}</span><span class="sb">`</span><span class="p">)</span>
<span class="w">  </span><span class="p">}</span>
<span class="p">}</span>

<span class="c1">// The format of messages, this matches pydantic-ai both for brevity and understanding</span>
<span class="c1">// in production, you might not want to keep this format all the way to the frontend</span>
<span class="kd">interface</span><span class="w"> </span><span class="nx">Message</span><span class="w"> </span><span class="p">{</span>
<span class="w">  </span><span class="nx">role</span><span class="o">:</span><span class="w"> </span><span class="kt">string</span>
<span class="w">  </span><span class="nx">content</span><span class="o">:</span><span class="w"> </span><span class="kt">string</span>
<span class="w">  </span><span class="nx">timestamp</span><span class="o">:</span><span class="w"> </span><span class="kt">string</span>
<span class="p">}</span>

<span class="c1">// take raw response text and render messages into the `#conversation` element</span>
<span class="c1">// Message timestamp is assumed to be a unique identifier of a message, and is used to deduplicate</span>
<span class="c1">// hence you can send data about the same message multiple times, and it will be updated</span>
<span class="c1">// instead of creating a new message elements</span>
<span class="kd">function</span><span class="w"> </span><span class="nx">addMessages</span><span class="p">(</span><span class="nx">responseText</span><span class="o">:</span><span class="w"> </span><span class="kt">string</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">  </span><span class="kd">const</span><span class="w"> </span><span class="nx">lines</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="nx">responseText</span><span class="p">.</span><span class="nx">split</span><span class="p">(</span><span class="s1">'\n'</span><span class="p">)</span>
<span class="w">  </span><span class="kd">const</span><span class="w"> </span><span class="nx">messages</span><span class="o">:</span><span class="w"> </span><span class="kt">Message</span><span class="p">[]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="nx">lines</span><span class="p">.</span><span class="nx">filter</span><span class="p">(</span><span class="nx">line</span><span class="w"> </span><span class="p">=&gt;</span><span class="w"> </span><span class="nx">line</span><span class="p">.</span><span class="nx">length</span><span class="w"> </span><span class="o">&gt;</span><span class="w"> </span><span class="mf">1</span><span class="p">).</span><span class="nx">map</span><span class="p">(</span><span class="nx">j</span><span class="w"> </span><span class="p">=&gt;</span><span class="w"> </span><span class="nb">JSON</span><span class="p">.</span><span class="nx">parse</span><span class="p">(</span><span class="nx">j</span><span class="p">))</span>
<span class="w">  </span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="kd">const</span><span class="w"> </span><span class="nx">message</span><span class="w"> </span><span class="k">of</span><span class="w"> </span><span class="nx">messages</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="c1">// we use the timestamp as a crude element id</span>
<span class="w">    </span><span class="kd">const</span><span class="w"> </span><span class="p">{</span><span class="nx">timestamp</span><span class="p">,</span><span class="w"> </span><span class="nx">role</span><span class="p">,</span><span class="w"> </span><span class="nx">content</span><span class="p">}</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="nx">message</span>
<span class="w">    </span><span class="kd">const</span><span class="w"> </span><span class="nx">id</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="sb">`msg-</span><span class="si">${</span><span class="nx">timestamp</span><span class="si">}</span><span class="sb">`</span>
<span class="w">    </span><span class="kd">let</span><span class="w"> </span><span class="nx">msgDiv</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="nb">document</span><span class="p">.</span><span class="nx">getElementById</span><span class="p">(</span><span class="nx">id</span><span class="p">)</span>
<span class="w">    </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="o">!</span><span class="nx">msgDiv</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">      </span><span class="nx">msgDiv</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="nb">document</span><span class="p">.</span><span class="nx">createElement</span><span class="p">(</span><span class="s1">'div'</span><span class="p">)</span>
<span class="w">      </span><span class="nx">msgDiv</span><span class="p">.</span><span class="nx">id</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="nx">id</span>
<span class="w">      </span><span class="nx">msgDiv</span><span class="p">.</span><span class="nx">title</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="sb">`</span><span class="si">${</span><span class="nx">role</span><span class="si">}</span><span class="sb"> at </span><span class="si">${</span><span class="nx">timestamp</span><span class="si">}</span><span class="sb">`</span>
<span class="w">      </span><span class="nx">msgDiv</span><span class="p">.</span><span class="nx">classList</span><span class="p">.</span><span class="nx">add</span><span class="p">(</span><span class="s1">'border-top'</span><span class="p">,</span><span class="w"> </span><span class="s1">'pt-2'</span><span class="p">,</span><span class="w"> </span><span class="nx">role</span><span class="p">)</span>
<span class="w">      </span><span class="nx">convElement</span><span class="p">.</span><span class="nx">appendChild</span><span class="p">(</span><span class="nx">msgDiv</span><span class="p">)</span>
<span class="w">    </span><span class="p">}</span>
<span class="w">    </span><span class="nx">msgDiv</span><span class="p">.</span><span class="nx">innerHTML</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="nx">marked</span><span class="p">.</span><span class="nx">parse</span><span class="p">(</span><span class="nx">content</span><span class="p">)</span>
<span class="w">  </span><span class="p">}</span>
<span class="w">  </span><span class="nb">window</span><span class="p">.</span><span class="nx">scrollTo</span><span class="p">({</span><span class="w"> </span><span class="nx">top</span><span class="o">:</span><span class="w"> </span><span class="kt">document.body.scrollHeight</span><span class="p">,</span><span class="w"> </span><span class="nx">behavior</span><span class="o">:</span><span class="w"> </span><span class="s1">'smooth'</span><span class="w"> </span><span class="p">})</span>
<span class="p">}</span>

<span class="kd">function</span><span class="w"> </span><span class="nx">onError</span><span class="p">(</span><span class="nx">error</span><span class="o">:</span><span class="w"> </span><span class="kt">any</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">  </span><span class="nx">console</span><span class="p">.</span><span class="nx">error</span><span class="p">(</span><span class="nx">error</span><span class="p">)</span>
<span class="w">  </span><span class="nb">document</span><span class="p">.</span><span class="nx">getElementById</span><span class="p">(</span><span class="s1">'error'</span><span class="p">).</span><span class="nx">classList</span><span class="p">.</span><span class="nx">remove</span><span class="p">(</span><span class="s1">'d-none'</span><span class="p">)</span>
<span class="w">  </span><span class="nb">document</span><span class="p">.</span><span class="nx">getElementById</span><span class="p">(</span><span class="s1">'spinner'</span><span class="p">).</span><span class="nx">classList</span><span class="p">.</span><span class="nx">remove</span><span class="p">(</span><span class="s1">'active'</span><span class="p">)</span>
<span class="p">}</span>

<span class="k">async</span><span class="w"> </span><span class="kd">function</span><span class="w"> </span><span class="nx">onSubmit</span><span class="p">(</span><span class="nx">e</span><span class="o">:</span><span class="w"> </span><span class="kt">SubmitEvent</span><span class="p">)</span><span class="o">:</span><span class="w"> </span><span class="nb">Promise</span><span class="o">&lt;</span><span class="ow">void</span><span class="o">&gt;</span><span class="w"> </span><span class="p">{</span>
<span class="w">  </span><span class="nx">e</span><span class="p">.</span><span class="nx">preventDefault</span><span class="p">()</span>
<span class="w">  </span><span class="nx">spinner</span><span class="p">.</span><span class="nx">classList</span><span class="p">.</span><span class="nx">add</span><span class="p">(</span><span class="s1">'active'</span><span class="p">)</span>
<span class="w">  </span><span class="kd">const</span><span class="w"> </span><span class="nx">body</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="ow">new</span><span class="w"> </span><span class="nx">FormData</span><span class="p">(</span><span class="nx">e</span><span class="p">.</span><span class="nx">target</span><span class="w"> </span><span class="kr">as</span><span class="w"> </span><span class="nx">HTMLFormElement</span><span class="p">)</span>

<span class="w">  </span><span class="nx">promptInput</span><span class="p">.</span><span class="nx">value</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s1">''</span>
<span class="w">  </span><span class="nx">promptInput</span><span class="p">.</span><span class="nx">disabled</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="kc">true</span>

<span class="w">  </span><span class="kd">const</span><span class="w"> </span><span class="nx">response</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">await</span><span class="w"> </span><span class="nx">fetch</span><span class="p">(</span><span class="s1">'/chat/'</span><span class="p">,</span><span class="w"> </span><span class="p">{</span><span class="nx">method</span><span class="o">:</span><span class="w"> </span><span class="s1">'POST'</span><span class="p">,</span><span class="w"> </span><span class="nx">body</span><span class="p">})</span>
<span class="w">  </span><span class="k">await</span><span class="w"> </span><span class="nx">onFetchResponse</span><span class="p">(</span><span class="nx">response</span><span class="p">)</span>
<span class="p">}</span>

<span class="c1">// call onSubmit when the form is submitted (e.g. user clicks the send button or hits Enter)</span>
<span class="nb">document</span><span class="p">.</span><span class="nx">querySelector</span><span class="p">(</span><span class="s1">'form'</span><span class="p">).</span><span class="nx">addEventListener</span><span class="p">(</span><span class="s1">'submit'</span><span class="p">,</span><span class="w"> </span><span class="p">(</span><span class="nx">e</span><span class="p">)</span><span class="w"> </span><span class="p">=&gt;</span><span class="w"> </span><span class="nx">onSubmit</span><span class="p">(</span><span class="nx">e</span><span class="p">).</span><span class="k">catch</span><span class="p">(</span><span class="nx">onError</span><span class="p">))</span>

<span class="c1">// load messages on page load</span>
<span class="nx">fetch</span><span class="p">(</span><span class="s1">'/chat/'</span><span class="p">).</span><span class="nx">then</span><span class="p">(</span><span class="nx">onFetchResponse</span><span class="p">).</span><span class="k">catch</span><span class="p">(</span><span class="nx">onError</span><span class="p">)</span>
</code></pre></div>







  
  






                
              </article>
            </div>
          
          
  <script>var tabs=__md_get("__tabs");if(Array.isArray(tabs))e:for(var set of document.querySelectorAll(".tabbed-set")){var labels=set.querySelector(".tabbed-labels");for(var tab of tabs)for(var label of labels.getElementsByTagName("label"))if(label.innerText.trim()===tab){var input=document.getElementById(label.htmlFor);input.checked=!0;continue e}}</script>

<script>var target=document.getElementById(location.hash.slice(1));target&&target.name&&(target.checked=target.name.startsWith("__tabbed_"))</script>
        </div>
        
      </main>
      
        <footer class="md-footer">
  
  <div class="md-footer-meta md-typeset">
    <div class="md-footer-meta__inner md-grid">
      <div class="md-copyright">
  
    <div class="md-copyright__highlight">
      © Pydantic Services Inc. 2024 to present
    </div>
  
  
</div>
      
    </div>
  </div>
</footer>
      
    </div>
    <div class="md-dialog" data-md-component="dialog">
      <div class="md-dialog__inner md-typeset"></div>
    </div>
    
    
    <script id="__config" type="application/json">{"base": "../..", "features": ["search.suggest", "search.highlight", "content.tabs.link", "content.code.annotate", "content.code.copy", "content.code.select", "navigation.path", "navigation.indexes", "navigation.sections", "navigation.tracking", "toc.follow"], "search": "../../assets/javascripts/workers/search.f8cc74c7.min.js", "translations": {"clipboard.copied": "Copied to clipboard", "clipboard.copy": "Copy to clipboard", "search.result.more.one": "1 more on this page", "search.result.more.other": "# more on this page", "search.result.none": "No matching documents", "search.result.one": "1 matching document", "search.result.other": "# matching documents", "search.result.placeholder": "Type to start searching", "search.result.term.missing": "Missing", "select.version": "Select version"}}</script>
    
    
      <script src="../../assets/javascripts/bundle.f1b6f286.min.js"></script>
      
        <script src="/flarelytics/client.js"></script>
      
        <script src="https://cdn.jsdelivr.net/npm/algoliasearch@5.20.0/dist/lite/builds/browser.umd.js"></script>
      
        <script src="https://cdn.jsdelivr.net/npm/instantsearch.js@4.77.3/dist/instantsearch.production.min.js"></script>
      
        <script src="/javascripts/algolia-search.js"></script>
      
    
  <script id="init-glightbox">const lightbox = GLightbox({"touchNavigation": true, "loop": false, "zoomable": true, "draggable": true, "openEffect": "zoom", "closeEffect": "zoom", "slideEffect": "slide"});
document$.subscribe(() => { lightbox.reload() });
</script>
</body></html>