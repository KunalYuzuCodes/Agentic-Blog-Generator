<!DOCTYPE html><html lang="en" class="js-focus-visible js" data-js-focus-visible=""><head>
    
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width,initial-scale=1">
      
        <meta name="description" content="Agent Framework / shim to use Pydantic with LLMs">
      
      
      
        <link rel="canonical" href="https://ai.pydantic.dev/api/messages/">
      
      
        <link rel="prev" href="../result/">
      
      
        <link rel="next" href="../exceptions/">
      
      
      <link rel="icon" href="../../favicon.ico">
      <meta name="generator" content="mkdocs-1.6.1, mkdocs-material-9.6.5">
    
    
      
        <title>pydantic_ai.messages - PydanticAI</title>
      
    
    
      <link rel="stylesheet" href="../../assets/stylesheets/main.8608ea7d.min.css">
      
        
        <link rel="stylesheet" href="../../assets/stylesheets/palette.06af60db.min.css">
      
      


    
    
      
    
    
      
        
        
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,300i,400,400i,700,700i%7CRoboto+Mono:400,400i,700,700i&amp;display=fallback">
        <style>:root{--md-text-font:"Roboto";--md-code-font:"Roboto Mono"}</style>
      
    
    
      <link rel="stylesheet" href="../../assets/_mkdocstrings.css">
    
      <link rel="stylesheet" href="../../extra/tweaks.css">
    
    <script>__md_scope=new URL("../..",location),__md_hash=e=>[...e].reduce(((e,_)=>(e<<5)-e+_.charCodeAt(0)),0),__md_get=(e,_=localStorage,t=__md_scope)=>JSON.parse(_.getItem(t.pathname+"."+e)),__md_set=(e,_,t=localStorage,a=__md_scope)=>{try{t.setItem(a.pathname+"."+e,JSON.stringify(_))}catch(e){}}</script>
    
      

    
    
      
        <meta property="og:type" content="website">
      
        <meta property="og:title" content="pydantic_ai.messages - PydanticAI">
      
        <meta property="og:description" content="Agent Framework / shim to use Pydantic with LLMs">
      
        <meta property="og:image" content="https://ai.pydantic.dev/assets/images/social/api/messages.png">
      
        <meta property="og:image:type" content="image/png">
      
        <meta property="og:image:width" content="1200">
      
        <meta property="og:image:height" content="630">
      
        <meta property="og:url" content="https://ai.pydantic.dev/api/messages/">
      
        <meta name="twitter:card" content="summary_large_image">
      
        <meta name="twitter:title" content="pydantic_ai.messages - PydanticAI">
      
        <meta name="twitter:description" content="Agent Framework / shim to use Pydantic with LLMs">
      
        <meta name="twitter:image" content="https://ai.pydantic.dev/assets/images/social/api/messages.png">
      
    
    
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
      
        
        <a href="#pydantic_aimessages" class="md-skip">
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
            
              pydantic_ai.messages
            
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
  

    
      
      
  
  
  
  
    
    
      
        
          
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
    
    
      
        
        
      
    
    
    <li class="md-nav__item md-nav__item--section md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_7">
        
          
          
          <div class="md-nav__link md-nav__container">
            <a href="../../examples/" class="md-nav__link ">
              
  
  <span class="md-ellipsis">
    Examples
    
  </span>
  

            </a>
            
              
              <label class="md-nav__link " for="__nav_7" id="__nav_7_label" tabindex="">
                <span class="md-nav__icon md-icon"></span>
              </label>
            
          </div>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_7_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_7">
            <span class="md-nav__icon md-icon"></span>
            Examples
          </label>
          <ul class="md-nav__list">
            
              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../examples/pydantic-model/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Pydantic Model
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../examples/weather-agent/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Weather agent
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../examples/bank-support/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Bank support
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../examples/sql-gen/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    SQL Generation
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../examples/flight-booking/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Flight booking
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../examples/rag/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    RAG
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../examples/stream-markdown/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Stream markdown
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../examples/stream-whales/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Stream whales
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../examples/chat-app/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Chat App with FastAPI
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../examples/question-graph/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Question Graph
    
  </span>
  

      </a>
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

    
      
      
  
  
    
  
  
  
    
    
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
    
    
      
        
        
      
    
    
    <li class="md-nav__item md-nav__item--active md-nav__item--section md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_8" checked="">
        
          
          <label class="md-nav__link" for="__nav_8" id="__nav_8_label" tabindex="">
            
  
  <span class="md-ellipsis">
    API Reference
    
  </span>
  

            <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_8_label" aria-expanded="true">
          <label class="md-nav__title" for="__nav_8">
            <span class="md-nav__icon md-icon"></span>
            API Reference
          </label>
          <ul class="md-nav__list">
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../agent/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.agent
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../common_tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.common_tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../result/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.result
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
    
  
  
  
    <li class="md-nav__item md-nav__item--active">
      
      <input class="md-nav__toggle md-toggle" type="checkbox" id="__toc">
      
      
        
      
      
        <label class="md-nav__link md-nav__link--active" for="__toc">
          
  
  <span class="md-ellipsis">
    pydantic_ai.messages
    
  </span>
  

          <span class="md-nav__icon md-icon"></span>
        </label>
      
      <a href="./" class="md-nav__link md-nav__link--active">
        
  
  <span class="md-ellipsis">
    pydantic_ai.messages
    
  </span>
  

      </a>
      
        

<nav class="md-nav md-nav--secondary" aria-label="Table of contents">
  
  
  
    
  
  
    <label class="md-nav__title" for="__toc">
      <span class="md-nav__icon md-icon"></span>
      Table of contents
    </label>
    <ul class="md-nav__list" data-md-component="toc">
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.messages" class="md-nav__link">
    <span class="md-ellipsis">
      messages
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.messages.SystemPromptPart" class="md-nav__link">
    <span class="md-ellipsis">
      SystemPromptPart
    </span>
  </a>
  
    <nav class="md-nav" aria-label="SystemPromptPart">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.SystemPromptPart.content" class="md-nav__link">
    <span class="md-ellipsis">
      content
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.SystemPromptPart.timestamp" class="md-nav__link">
    <span class="md-ellipsis">
      timestamp
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.SystemPromptPart.dynamic_ref" class="md-nav__link">
    <span class="md-ellipsis">
      dynamic_ref
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.SystemPromptPart.part_kind" class="md-nav__link">
    <span class="md-ellipsis">
      part_kind
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.messages.AudioUrl" class="md-nav__link">
    <span class="md-ellipsis">
      AudioUrl
    </span>
  </a>
  
    <nav class="md-nav" aria-label="AudioUrl">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.AudioUrl.url" class="md-nav__link">
    <span class="md-ellipsis">
      url
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.AudioUrl.kind" class="md-nav__link">
    <span class="md-ellipsis">
      kind
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.AudioUrl.media_type" class="md-nav__link">
    <span class="md-ellipsis">
      media_type
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ImageUrl" class="md-nav__link">
    <span class="md-ellipsis">
      ImageUrl
    </span>
  </a>
  
    <nav class="md-nav" aria-label="ImageUrl">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ImageUrl.url" class="md-nav__link">
    <span class="md-ellipsis">
      url
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ImageUrl.kind" class="md-nav__link">
    <span class="md-ellipsis">
      kind
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ImageUrl.media_type" class="md-nav__link">
    <span class="md-ellipsis">
      media_type
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ImageUrl.format" class="md-nav__link">
    <span class="md-ellipsis">
      format
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.messages.DocumentUrl" class="md-nav__link">
    <span class="md-ellipsis">
      DocumentUrl
    </span>
  </a>
  
    <nav class="md-nav" aria-label="DocumentUrl">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.DocumentUrl.url" class="md-nav__link">
    <span class="md-ellipsis">
      url
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.DocumentUrl.kind" class="md-nav__link">
    <span class="md-ellipsis">
      kind
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.DocumentUrl.media_type" class="md-nav__link">
    <span class="md-ellipsis">
      media_type
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.DocumentUrl.format" class="md-nav__link">
    <span class="md-ellipsis">
      format
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.messages.BinaryContent" class="md-nav__link">
    <span class="md-ellipsis">
      BinaryContent
    </span>
  </a>
  
    <nav class="md-nav" aria-label="BinaryContent">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.BinaryContent.data" class="md-nav__link">
    <span class="md-ellipsis">
      data
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.BinaryContent.media_type" class="md-nav__link">
    <span class="md-ellipsis">
      media_type
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.BinaryContent.kind" class="md-nav__link">
    <span class="md-ellipsis">
      kind
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.BinaryContent.is_audio" class="md-nav__link">
    <span class="md-ellipsis">
      is_audio
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.BinaryContent.is_image" class="md-nav__link">
    <span class="md-ellipsis">
      is_image
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.BinaryContent.is_document" class="md-nav__link">
    <span class="md-ellipsis">
      is_document
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.BinaryContent.format" class="md-nav__link">
    <span class="md-ellipsis">
      format
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.messages.UserPromptPart" class="md-nav__link">
    <span class="md-ellipsis">
      UserPromptPart
    </span>
  </a>
  
    <nav class="md-nav" aria-label="UserPromptPart">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.UserPromptPart.content" class="md-nav__link">
    <span class="md-ellipsis">
      content
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.UserPromptPart.timestamp" class="md-nav__link">
    <span class="md-ellipsis">
      timestamp
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.UserPromptPart.part_kind" class="md-nav__link">
    <span class="md-ellipsis">
      part_kind
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ToolReturnPart" class="md-nav__link">
    <span class="md-ellipsis">
      ToolReturnPart
    </span>
  </a>
  
    <nav class="md-nav" aria-label="ToolReturnPart">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ToolReturnPart.tool_name" class="md-nav__link">
    <span class="md-ellipsis">
      tool_name
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ToolReturnPart.content" class="md-nav__link">
    <span class="md-ellipsis">
      content
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ToolReturnPart.tool_call_id" class="md-nav__link">
    <span class="md-ellipsis">
      tool_call_id
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ToolReturnPart.timestamp" class="md-nav__link">
    <span class="md-ellipsis">
      timestamp
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ToolReturnPart.part_kind" class="md-nav__link">
    <span class="md-ellipsis">
      part_kind
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ToolReturnPart.model_response_str" class="md-nav__link">
    <span class="md-ellipsis">
      model_response_str
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ToolReturnPart.model_response_object" class="md-nav__link">
    <span class="md-ellipsis">
      model_response_object
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.messages.RetryPromptPart" class="md-nav__link">
    <span class="md-ellipsis">
      RetryPromptPart
    </span>
  </a>
  
    <nav class="md-nav" aria-label="RetryPromptPart">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.RetryPromptPart.content" class="md-nav__link">
    <span class="md-ellipsis">
      content
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.RetryPromptPart.tool_name" class="md-nav__link">
    <span class="md-ellipsis">
      tool_name
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.RetryPromptPart.tool_call_id" class="md-nav__link">
    <span class="md-ellipsis">
      tool_call_id
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.RetryPromptPart.timestamp" class="md-nav__link">
    <span class="md-ellipsis">
      timestamp
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.RetryPromptPart.part_kind" class="md-nav__link">
    <span class="md-ellipsis">
      part_kind
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.RetryPromptPart.model_response" class="md-nav__link">
    <span class="md-ellipsis">
      model_response
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ModelRequestPart" class="md-nav__link">
    <span class="md-ellipsis">
      ModelRequestPart
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ModelRequest" class="md-nav__link">
    <span class="md-ellipsis">
      ModelRequest
    </span>
  </a>
  
    <nav class="md-nav" aria-label="ModelRequest">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ModelRequest.parts" class="md-nav__link">
    <span class="md-ellipsis">
      parts
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ModelRequest.kind" class="md-nav__link">
    <span class="md-ellipsis">
      kind
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.messages.TextPart" class="md-nav__link">
    <span class="md-ellipsis">
      TextPart
    </span>
  </a>
  
    <nav class="md-nav" aria-label="TextPart">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.TextPart.content" class="md-nav__link">
    <span class="md-ellipsis">
      content
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.TextPart.part_kind" class="md-nav__link">
    <span class="md-ellipsis">
      part_kind
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.TextPart.has_content" class="md-nav__link">
    <span class="md-ellipsis">
      has_content
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ToolCallPart" class="md-nav__link">
    <span class="md-ellipsis">
      ToolCallPart
    </span>
  </a>
  
    <nav class="md-nav" aria-label="ToolCallPart">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ToolCallPart.tool_name" class="md-nav__link">
    <span class="md-ellipsis">
      tool_name
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ToolCallPart.args" class="md-nav__link">
    <span class="md-ellipsis">
      args
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ToolCallPart.tool_call_id" class="md-nav__link">
    <span class="md-ellipsis">
      tool_call_id
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ToolCallPart.part_kind" class="md-nav__link">
    <span class="md-ellipsis">
      part_kind
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ToolCallPart.args_as_dict" class="md-nav__link">
    <span class="md-ellipsis">
      args_as_dict
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ToolCallPart.args_as_json_str" class="md-nav__link">
    <span class="md-ellipsis">
      args_as_json_str
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ToolCallPart.has_content" class="md-nav__link">
    <span class="md-ellipsis">
      has_content
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ModelResponsePart" class="md-nav__link">
    <span class="md-ellipsis">
      ModelResponsePart
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ModelResponse" class="md-nav__link">
    <span class="md-ellipsis">
      ModelResponse
    </span>
  </a>
  
    <nav class="md-nav" aria-label="ModelResponse">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ModelResponse.parts" class="md-nav__link">
    <span class="md-ellipsis">
      parts
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ModelResponse.model_name" class="md-nav__link">
    <span class="md-ellipsis">
      model_name
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ModelResponse.timestamp" class="md-nav__link">
    <span class="md-ellipsis">
      timestamp
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ModelResponse.kind" class="md-nav__link">
    <span class="md-ellipsis">
      kind
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ModelResponse.otel_events" class="md-nav__link">
    <span class="md-ellipsis">
      otel_events
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ModelMessage" class="md-nav__link">
    <span class="md-ellipsis">
      ModelMessage
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ModelMessagesTypeAdapter" class="md-nav__link">
    <span class="md-ellipsis">
      ModelMessagesTypeAdapter
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.messages.TextPartDelta" class="md-nav__link">
    <span class="md-ellipsis">
      TextPartDelta
    </span>
  </a>
  
    <nav class="md-nav" aria-label="TextPartDelta">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.TextPartDelta.content_delta" class="md-nav__link">
    <span class="md-ellipsis">
      content_delta
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.TextPartDelta.part_delta_kind" class="md-nav__link">
    <span class="md-ellipsis">
      part_delta_kind
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.TextPartDelta.apply" class="md-nav__link">
    <span class="md-ellipsis">
      apply
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ToolCallPartDelta" class="md-nav__link">
    <span class="md-ellipsis">
      ToolCallPartDelta
    </span>
  </a>
  
    <nav class="md-nav" aria-label="ToolCallPartDelta">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ToolCallPartDelta.tool_name_delta" class="md-nav__link">
    <span class="md-ellipsis">
      tool_name_delta
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ToolCallPartDelta.args_delta" class="md-nav__link">
    <span class="md-ellipsis">
      args_delta
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ToolCallPartDelta.tool_call_id" class="md-nav__link">
    <span class="md-ellipsis">
      tool_call_id
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ToolCallPartDelta.part_delta_kind" class="md-nav__link">
    <span class="md-ellipsis">
      part_delta_kind
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ToolCallPartDelta.as_part" class="md-nav__link">
    <span class="md-ellipsis">
      as_part
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ToolCallPartDelta.apply" class="md-nav__link">
    <span class="md-ellipsis">
      apply
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ModelResponsePartDelta" class="md-nav__link">
    <span class="md-ellipsis">
      ModelResponsePartDelta
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.messages.PartStartEvent" class="md-nav__link">
    <span class="md-ellipsis">
      PartStartEvent
    </span>
  </a>
  
    <nav class="md-nav" aria-label="PartStartEvent">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.PartStartEvent.index" class="md-nav__link">
    <span class="md-ellipsis">
      index
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.PartStartEvent.part" class="md-nav__link">
    <span class="md-ellipsis">
      part
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.PartStartEvent.event_kind" class="md-nav__link">
    <span class="md-ellipsis">
      event_kind
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.messages.PartDeltaEvent" class="md-nav__link">
    <span class="md-ellipsis">
      PartDeltaEvent
    </span>
  </a>
  
    <nav class="md-nav" aria-label="PartDeltaEvent">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.PartDeltaEvent.index" class="md-nav__link">
    <span class="md-ellipsis">
      index
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.PartDeltaEvent.delta" class="md-nav__link">
    <span class="md-ellipsis">
      delta
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.PartDeltaEvent.event_kind" class="md-nav__link">
    <span class="md-ellipsis">
      event_kind
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.messages.FinalResultEvent" class="md-nav__link">
    <span class="md-ellipsis">
      FinalResultEvent
    </span>
  </a>
  
    <nav class="md-nav" aria-label="FinalResultEvent">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.FinalResultEvent.tool_name" class="md-nav__link">
    <span class="md-ellipsis">
      tool_name
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.FinalResultEvent.tool_call_id" class="md-nav__link">
    <span class="md-ellipsis">
      tool_call_id
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.FinalResultEvent.event_kind" class="md-nav__link">
    <span class="md-ellipsis">
      event_kind
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ModelResponseStreamEvent" class="md-nav__link">
    <span class="md-ellipsis">
      ModelResponseStreamEvent
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.messages.AgentStreamEvent" class="md-nav__link">
    <span class="md-ellipsis">
      AgentStreamEvent
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.messages.FunctionToolCallEvent" class="md-nav__link">
    <span class="md-ellipsis">
      FunctionToolCallEvent
    </span>
  </a>
  
    <nav class="md-nav" aria-label="FunctionToolCallEvent">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.FunctionToolCallEvent.part" class="md-nav__link">
    <span class="md-ellipsis">
      part
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.FunctionToolCallEvent.call_id" class="md-nav__link">
    <span class="md-ellipsis">
      call_id
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.FunctionToolCallEvent.event_kind" class="md-nav__link">
    <span class="md-ellipsis">
      event_kind
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.messages.FunctionToolResultEvent" class="md-nav__link">
    <span class="md-ellipsis">
      FunctionToolResultEvent
    </span>
  </a>
  
    <nav class="md-nav" aria-label="FunctionToolResultEvent">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.FunctionToolResultEvent.result" class="md-nav__link">
    <span class="md-ellipsis">
      result
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.FunctionToolResultEvent.tool_call_id" class="md-nav__link">
    <span class="md-ellipsis">
      tool_call_id
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.FunctionToolResultEvent.event_kind" class="md-nav__link">
    <span class="md-ellipsis">
      event_kind
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
    </ul>
  
</nav>
      
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../exceptions/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.exceptions
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../settings/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.settings
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../usage/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.usage
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../mcp/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.mcp
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../format_as_xml/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.format_as_xml
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../models/base/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../models/openai/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.openai
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../models/anthropic/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.anthropic
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../models/bedrock/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.bedrock
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../models/cohere/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.cohere
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../models/gemini/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.gemini
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../models/groq/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.groq
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../models/instrumented/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.instrumented
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../models/mistral/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.mistral
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../models/test/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.test
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../models/function/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.function
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../models/fallback/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.fallback
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../models/wrapper/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.wrapper
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../providers/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.providers
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../pydantic_graph/graph/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../pydantic_graph/nodes/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.nodes
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../pydantic_graph/persistence/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.persistence
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../pydantic_graph/mermaid/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.mermaid
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../pydantic_graph/exceptions/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.exceptions
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../pydantic_evals/dataset/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.dataset
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../pydantic_evals/evaluators/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.evaluators
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../pydantic_evals/reporting/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.reporting
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../pydantic_evals/otel/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.otel
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../pydantic_evals/generation/" class="md-nav__link">
        
  
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
  <a href="#pydantic_ai.messages" class="md-nav__link">
    <span class="md-ellipsis">
      messages
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.messages.SystemPromptPart" class="md-nav__link">
    <span class="md-ellipsis">
      SystemPromptPart
    </span>
  </a>
  
    <nav class="md-nav" aria-label="SystemPromptPart">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.SystemPromptPart.content" class="md-nav__link">
    <span class="md-ellipsis">
      content
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.SystemPromptPart.timestamp" class="md-nav__link">
    <span class="md-ellipsis">
      timestamp
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.SystemPromptPart.dynamic_ref" class="md-nav__link">
    <span class="md-ellipsis">
      dynamic_ref
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.SystemPromptPart.part_kind" class="md-nav__link">
    <span class="md-ellipsis">
      part_kind
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.messages.AudioUrl" class="md-nav__link">
    <span class="md-ellipsis">
      AudioUrl
    </span>
  </a>
  
    <nav class="md-nav" aria-label="AudioUrl">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.AudioUrl.url" class="md-nav__link">
    <span class="md-ellipsis">
      url
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.AudioUrl.kind" class="md-nav__link">
    <span class="md-ellipsis">
      kind
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.AudioUrl.media_type" class="md-nav__link">
    <span class="md-ellipsis">
      media_type
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ImageUrl" class="md-nav__link">
    <span class="md-ellipsis">
      ImageUrl
    </span>
  </a>
  
    <nav class="md-nav" aria-label="ImageUrl">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ImageUrl.url" class="md-nav__link">
    <span class="md-ellipsis">
      url
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ImageUrl.kind" class="md-nav__link">
    <span class="md-ellipsis">
      kind
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ImageUrl.media_type" class="md-nav__link">
    <span class="md-ellipsis">
      media_type
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ImageUrl.format" class="md-nav__link">
    <span class="md-ellipsis">
      format
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.messages.DocumentUrl" class="md-nav__link">
    <span class="md-ellipsis">
      DocumentUrl
    </span>
  </a>
  
    <nav class="md-nav" aria-label="DocumentUrl">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.DocumentUrl.url" class="md-nav__link">
    <span class="md-ellipsis">
      url
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.DocumentUrl.kind" class="md-nav__link">
    <span class="md-ellipsis">
      kind
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.DocumentUrl.media_type" class="md-nav__link">
    <span class="md-ellipsis">
      media_type
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.DocumentUrl.format" class="md-nav__link">
    <span class="md-ellipsis">
      format
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.messages.BinaryContent" class="md-nav__link">
    <span class="md-ellipsis">
      BinaryContent
    </span>
  </a>
  
    <nav class="md-nav" aria-label="BinaryContent">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.BinaryContent.data" class="md-nav__link">
    <span class="md-ellipsis">
      data
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.BinaryContent.media_type" class="md-nav__link">
    <span class="md-ellipsis">
      media_type
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.BinaryContent.kind" class="md-nav__link">
    <span class="md-ellipsis">
      kind
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.BinaryContent.is_audio" class="md-nav__link">
    <span class="md-ellipsis">
      is_audio
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.BinaryContent.is_image" class="md-nav__link">
    <span class="md-ellipsis">
      is_image
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.BinaryContent.is_document" class="md-nav__link">
    <span class="md-ellipsis">
      is_document
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.BinaryContent.format" class="md-nav__link">
    <span class="md-ellipsis">
      format
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.messages.UserPromptPart" class="md-nav__link">
    <span class="md-ellipsis">
      UserPromptPart
    </span>
  </a>
  
    <nav class="md-nav" aria-label="UserPromptPart">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.UserPromptPart.content" class="md-nav__link">
    <span class="md-ellipsis">
      content
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.UserPromptPart.timestamp" class="md-nav__link">
    <span class="md-ellipsis">
      timestamp
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.UserPromptPart.part_kind" class="md-nav__link">
    <span class="md-ellipsis">
      part_kind
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ToolReturnPart" class="md-nav__link">
    <span class="md-ellipsis">
      ToolReturnPart
    </span>
  </a>
  
    <nav class="md-nav" aria-label="ToolReturnPart">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ToolReturnPart.tool_name" class="md-nav__link">
    <span class="md-ellipsis">
      tool_name
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ToolReturnPart.content" class="md-nav__link">
    <span class="md-ellipsis">
      content
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ToolReturnPart.tool_call_id" class="md-nav__link">
    <span class="md-ellipsis">
      tool_call_id
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ToolReturnPart.timestamp" class="md-nav__link">
    <span class="md-ellipsis">
      timestamp
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ToolReturnPart.part_kind" class="md-nav__link">
    <span class="md-ellipsis">
      part_kind
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ToolReturnPart.model_response_str" class="md-nav__link">
    <span class="md-ellipsis">
      model_response_str
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ToolReturnPart.model_response_object" class="md-nav__link">
    <span class="md-ellipsis">
      model_response_object
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.messages.RetryPromptPart" class="md-nav__link">
    <span class="md-ellipsis">
      RetryPromptPart
    </span>
  </a>
  
    <nav class="md-nav" aria-label="RetryPromptPart">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.RetryPromptPart.content" class="md-nav__link">
    <span class="md-ellipsis">
      content
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.RetryPromptPart.tool_name" class="md-nav__link">
    <span class="md-ellipsis">
      tool_name
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.RetryPromptPart.tool_call_id" class="md-nav__link">
    <span class="md-ellipsis">
      tool_call_id
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.RetryPromptPart.timestamp" class="md-nav__link">
    <span class="md-ellipsis">
      timestamp
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.RetryPromptPart.part_kind" class="md-nav__link">
    <span class="md-ellipsis">
      part_kind
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.RetryPromptPart.model_response" class="md-nav__link">
    <span class="md-ellipsis">
      model_response
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ModelRequestPart" class="md-nav__link">
    <span class="md-ellipsis">
      ModelRequestPart
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ModelRequest" class="md-nav__link">
    <span class="md-ellipsis">
      ModelRequest
    </span>
  </a>
  
    <nav class="md-nav" aria-label="ModelRequest">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ModelRequest.parts" class="md-nav__link">
    <span class="md-ellipsis">
      parts
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ModelRequest.kind" class="md-nav__link">
    <span class="md-ellipsis">
      kind
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.messages.TextPart" class="md-nav__link">
    <span class="md-ellipsis">
      TextPart
    </span>
  </a>
  
    <nav class="md-nav" aria-label="TextPart">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.TextPart.content" class="md-nav__link">
    <span class="md-ellipsis">
      content
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.TextPart.part_kind" class="md-nav__link">
    <span class="md-ellipsis">
      part_kind
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.TextPart.has_content" class="md-nav__link">
    <span class="md-ellipsis">
      has_content
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ToolCallPart" class="md-nav__link">
    <span class="md-ellipsis">
      ToolCallPart
    </span>
  </a>
  
    <nav class="md-nav" aria-label="ToolCallPart">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ToolCallPart.tool_name" class="md-nav__link">
    <span class="md-ellipsis">
      tool_name
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ToolCallPart.args" class="md-nav__link">
    <span class="md-ellipsis">
      args
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ToolCallPart.tool_call_id" class="md-nav__link">
    <span class="md-ellipsis">
      tool_call_id
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ToolCallPart.part_kind" class="md-nav__link">
    <span class="md-ellipsis">
      part_kind
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ToolCallPart.args_as_dict" class="md-nav__link">
    <span class="md-ellipsis">
      args_as_dict
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ToolCallPart.args_as_json_str" class="md-nav__link">
    <span class="md-ellipsis">
      args_as_json_str
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ToolCallPart.has_content" class="md-nav__link">
    <span class="md-ellipsis">
      has_content
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ModelResponsePart" class="md-nav__link">
    <span class="md-ellipsis">
      ModelResponsePart
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ModelResponse" class="md-nav__link">
    <span class="md-ellipsis">
      ModelResponse
    </span>
  </a>
  
    <nav class="md-nav" aria-label="ModelResponse">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ModelResponse.parts" class="md-nav__link">
    <span class="md-ellipsis">
      parts
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ModelResponse.model_name" class="md-nav__link">
    <span class="md-ellipsis">
      model_name
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ModelResponse.timestamp" class="md-nav__link">
    <span class="md-ellipsis">
      timestamp
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ModelResponse.kind" class="md-nav__link">
    <span class="md-ellipsis">
      kind
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ModelResponse.otel_events" class="md-nav__link">
    <span class="md-ellipsis">
      otel_events
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ModelMessage" class="md-nav__link">
    <span class="md-ellipsis">
      ModelMessage
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ModelMessagesTypeAdapter" class="md-nav__link">
    <span class="md-ellipsis">
      ModelMessagesTypeAdapter
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.messages.TextPartDelta" class="md-nav__link">
    <span class="md-ellipsis">
      TextPartDelta
    </span>
  </a>
  
    <nav class="md-nav" aria-label="TextPartDelta">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.TextPartDelta.content_delta" class="md-nav__link">
    <span class="md-ellipsis">
      content_delta
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.TextPartDelta.part_delta_kind" class="md-nav__link">
    <span class="md-ellipsis">
      part_delta_kind
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.TextPartDelta.apply" class="md-nav__link">
    <span class="md-ellipsis">
      apply
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ToolCallPartDelta" class="md-nav__link">
    <span class="md-ellipsis">
      ToolCallPartDelta
    </span>
  </a>
  
    <nav class="md-nav" aria-label="ToolCallPartDelta">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ToolCallPartDelta.tool_name_delta" class="md-nav__link">
    <span class="md-ellipsis">
      tool_name_delta
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ToolCallPartDelta.args_delta" class="md-nav__link">
    <span class="md-ellipsis">
      args_delta
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ToolCallPartDelta.tool_call_id" class="md-nav__link">
    <span class="md-ellipsis">
      tool_call_id
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ToolCallPartDelta.part_delta_kind" class="md-nav__link">
    <span class="md-ellipsis">
      part_delta_kind
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ToolCallPartDelta.as_part" class="md-nav__link">
    <span class="md-ellipsis">
      as_part
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ToolCallPartDelta.apply" class="md-nav__link">
    <span class="md-ellipsis">
      apply
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ModelResponsePartDelta" class="md-nav__link">
    <span class="md-ellipsis">
      ModelResponsePartDelta
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.messages.PartStartEvent" class="md-nav__link">
    <span class="md-ellipsis">
      PartStartEvent
    </span>
  </a>
  
    <nav class="md-nav" aria-label="PartStartEvent">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.PartStartEvent.index" class="md-nav__link">
    <span class="md-ellipsis">
      index
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.PartStartEvent.part" class="md-nav__link">
    <span class="md-ellipsis">
      part
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.PartStartEvent.event_kind" class="md-nav__link">
    <span class="md-ellipsis">
      event_kind
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.messages.PartDeltaEvent" class="md-nav__link">
    <span class="md-ellipsis">
      PartDeltaEvent
    </span>
  </a>
  
    <nav class="md-nav" aria-label="PartDeltaEvent">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.PartDeltaEvent.index" class="md-nav__link">
    <span class="md-ellipsis">
      index
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.PartDeltaEvent.delta" class="md-nav__link">
    <span class="md-ellipsis">
      delta
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.PartDeltaEvent.event_kind" class="md-nav__link">
    <span class="md-ellipsis">
      event_kind
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.messages.FinalResultEvent" class="md-nav__link">
    <span class="md-ellipsis">
      FinalResultEvent
    </span>
  </a>
  
    <nav class="md-nav" aria-label="FinalResultEvent">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.FinalResultEvent.tool_name" class="md-nav__link">
    <span class="md-ellipsis">
      tool_name
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.FinalResultEvent.tool_call_id" class="md-nav__link">
    <span class="md-ellipsis">
      tool_call_id
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.FinalResultEvent.event_kind" class="md-nav__link">
    <span class="md-ellipsis">
      event_kind
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.messages.ModelResponseStreamEvent" class="md-nav__link">
    <span class="md-ellipsis">
      ModelResponseStreamEvent
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.messages.AgentStreamEvent" class="md-nav__link">
    <span class="md-ellipsis">
      AgentStreamEvent
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.messages.FunctionToolCallEvent" class="md-nav__link">
    <span class="md-ellipsis">
      FunctionToolCallEvent
    </span>
  </a>
  
    <nav class="md-nav" aria-label="FunctionToolCallEvent">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.FunctionToolCallEvent.part" class="md-nav__link">
    <span class="md-ellipsis">
      part
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.FunctionToolCallEvent.call_id" class="md-nav__link">
    <span class="md-ellipsis">
      call_id
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.FunctionToolCallEvent.event_kind" class="md-nav__link">
    <span class="md-ellipsis">
      event_kind
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.messages.FunctionToolResultEvent" class="md-nav__link">
    <span class="md-ellipsis">
      FunctionToolResultEvent
    </span>
  </a>
  
    <nav class="md-nav" aria-label="FunctionToolResultEvent">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.FunctionToolResultEvent.result" class="md-nav__link">
    <span class="md-ellipsis">
      result
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.FunctionToolResultEvent.tool_call_id" class="md-nav__link">
    <span class="md-ellipsis">
      tool_call_id
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.messages.FunctionToolResultEvent.event_kind" class="md-nav__link">
    <span class="md-ellipsis">
      event_kind
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
            
          
          
            <div class="md-content" data-md-component="content">
              <article class="md-content__inner md-typeset">
                
                  


  
  


<h1 id="pydantic_aimessages"><code>pydantic_ai.messages</code></h1>
<p>The structure of <a class="autorefs autorefs-internal" href="#pydantic_ai.messages.ModelMessage"><code>ModelMessage</code></a> can be shown as a graph:</p>
<div class="mermaid"></div>


<div class="doc doc-object doc-module">



<a id="pydantic_ai.messages"></a>
    <div class="doc doc-contents first">








  <div class="doc doc-children">















<div class="doc doc-object doc-class">



<h3 id="pydantic_ai.messages.SystemPromptPart" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">SystemPromptPart</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">


        <p>A system prompt, generally written by the application developer.</p>
<p>This gives the model context and guidance on how to respond.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/messages.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">19</span>
<span class="normal">20</span>
<span class="normal">21</span>
<span class="normal">22</span>
<span class="normal">23</span>
<span class="normal">24</span>
<span class="normal">25</span>
<span class="normal">26</span>
<span class="normal">27</span>
<span class="normal">28</span>
<span class="normal">29</span>
<span class="normal">30</span>
<span class="normal">31</span>
<span class="normal">32</span>
<span class="normal">33</span>
<span class="normal">34</span>
<span class="normal">35</span>
<span class="normal">36</span>
<span class="normal">37</span>
<span class="normal">38</span>
<span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span></pre></div></td><td class="code"><div><pre id="__code_0"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_0 > code"></button><code tabindex="0"><span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">SystemPromptPart</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""A system prompt, generally written by the application developer.</span>

<span class="sd">    This gives the model context and guidance on how to respond.</span>
<span class="sd">    """</span>

    <span class="n">content</span><span class="p">:</span> <span class="nb">str</span>
<span class="w">    </span><span class="sd">"""The content of the prompt."""</span>

    <span class="n">timestamp</span><span class="p">:</span> <span class="n">datetime</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span><span class="n">default_factory</span><span class="o">=</span><span class="n">_now_utc</span><span class="p">)</span>
<span class="w">    </span><span class="sd">"""The timestamp of the prompt."""</span>

    <span class="n">dynamic_ref</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="w">    </span><span class="sd">"""The ref of the dynamic system prompt function that generated this part.</span>

<span class="sd">    Only set if system prompt is dynamic, see [`system_prompt`][pydantic_ai.Agent.system_prompt] for more information.</span>
<span class="sd">    """</span>

    <span class="n">part_kind</span><span class="p">:</span> <span class="n">Literal</span><span class="p">[</span><span class="s1">'system-prompt'</span><span class="p">]</span> <span class="o">=</span> <span class="s1">'system-prompt'</span>
<span class="w">    </span><span class="sd">"""Part type identifier, this is available on all parts as a discriminator."""</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">otel_event</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Event</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">Event</span><span class="p">(</span><span class="s1">'gen_ai.system.message'</span><span class="p">,</span> <span class="n">body</span><span class="o">=</span><span class="p">{</span><span class="s1">'content'</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">content</span><span class="p">,</span> <span class="s1">'role'</span><span class="p">:</span> <span class="s1">'system'</span><span class="p">})</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.SystemPromptPart.content" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">content</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_1"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_1 > code"></button><code><span class="n">content</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The content of the prompt.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.SystemPromptPart.timestamp" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">timestamp</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_2"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_2 > code"></button><code><span class="n">timestamp</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="datetime.datetime" href="https://docs.python.org/3/library/datetime.html#datetime.datetime">datetime</a></span> <span class="o">=</span> <span class="n"><a class="autorefs autorefs-external" title="dataclasses.field" href="https://docs.python.org/3/library/dataclasses.html#dataclasses.field">field</a></span><span class="p">(</span><span class="n"><span title="dataclasses.field(default_factory)">default_factory</span></span><span class="o">=</span><span class="n"><span title="pydantic_ai._utils.now_utc">now_utc</span></span><span class="p">)</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The timestamp of the prompt.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.SystemPromptPart.dynamic_ref" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">dynamic_ref</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_3"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_3 > code"></button><code><span class="n">dynamic_ref</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The ref of the dynamic system prompt function that generated this part.</p>
<p>Only set if system prompt is dynamic, see <a class="autorefs autorefs-internal" href="../agent/#pydantic_ai.agent.Agent.system_prompt"><code>system_prompt</code></a> for more information.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.SystemPromptPart.part_kind" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">part_kind</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_4"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_4 > code"></button><code><span class="n">part_kind</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Literal" href="https://docs.python.org/3/library/typing.html#typing.Literal">Literal</a></span><span class="p">[</span><span class="s1">'system-prompt'</span><span class="p">]</span> <span class="o">=</span> <span class="s1">'system-prompt'</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Part type identifier, this is available on all parts as a discriminator.</p>
    </div>

</div>




  </div>

    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_ai.messages.AudioUrl" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">AudioUrl</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">


        <p>A URL to an audio file.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/messages.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span>
<span class="normal">49</span>
<span class="normal">50</span>
<span class="normal">51</span>
<span class="normal">52</span>
<span class="normal">53</span>
<span class="normal">54</span>
<span class="normal">55</span>
<span class="normal">56</span>
<span class="normal">57</span>
<span class="normal">58</span>
<span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span>
<span class="normal">63</span></pre></div></td><td class="code"><div><pre id="__code_5"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_5 > code"></button><code><span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">AudioUrl</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""A URL to an audio file."""</span>

    <span class="n">url</span><span class="p">:</span> <span class="nb">str</span>
<span class="w">    </span><span class="sd">"""The URL of the audio file."""</span>

    <span class="n">kind</span><span class="p">:</span> <span class="n">Literal</span><span class="p">[</span><span class="s1">'audio-url'</span><span class="p">]</span> <span class="o">=</span> <span class="s1">'audio-url'</span>
<span class="w">    </span><span class="sd">"""Type identifier, this is available on all parts as a discriminator."""</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">media_type</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AudioMediaType</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Return the media type of the audio file, based on the url."""</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">url</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s1">'.mp3'</span><span class="p">):</span>
            <span class="k">return</span> <span class="s1">'audio/mpeg'</span>
        <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">url</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s1">'.wav'</span><span class="p">):</span>
            <span class="k">return</span> <span class="s1">'audio/wav'</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s1">'Unknown audio file extension: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">url</span><span class="si">}</span><span class="s1">'</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.AudioUrl.url" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">url</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_6"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_6 > code"></button><code><span class="n">url</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The URL of the audio file.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.AudioUrl.kind" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">kind</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_7"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_7 > code"></button><code><span class="n">kind</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Literal" href="https://docs.python.org/3/library/typing.html#typing.Literal">Literal</a></span><span class="p">[</span><span class="s1">'audio-url'</span><span class="p">]</span> <span class="o">=</span> <span class="s1">'audio-url'</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Type identifier, this is available on all parts as a discriminator.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.AudioUrl.media_type" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">media_type</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-property"><code>property</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_8"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_8 > code"></button><code><span class="n">media_type</span><span class="p">:</span> <span class="n"><span title="pydantic_ai.messages.AudioMediaType">AudioMediaType</span></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Return the media type of the audio file, based on the url.</p>
    </div>

</div>




  </div>

    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_ai.messages.ImageUrl" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">ImageUrl</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">


        <p>A URL to an image.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/messages.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">66</span>
<span class="normal">67</span>
<span class="normal">68</span>
<span class="normal">69</span>
<span class="normal">70</span>
<span class="normal">71</span>
<span class="normal">72</span>
<span class="normal">73</span>
<span class="normal">74</span>
<span class="normal">75</span>
<span class="normal">76</span>
<span class="normal">77</span>
<span class="normal">78</span>
<span class="normal">79</span>
<span class="normal">80</span>
<span class="normal">81</span>
<span class="normal">82</span>
<span class="normal">83</span>
<span class="normal">84</span>
<span class="normal">85</span>
<span class="normal">86</span>
<span class="normal">87</span>
<span class="normal">88</span>
<span class="normal">89</span>
<span class="normal">90</span>
<span class="normal">91</span>
<span class="normal">92</span>
<span class="normal">93</span>
<span class="normal">94</span>
<span class="normal">95</span>
<span class="normal">96</span></pre></div></td><td class="code"><div><pre id="__code_9"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_9 > code"></button><code tabindex="0"><span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">ImageUrl</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""A URL to an image."""</span>

    <span class="n">url</span><span class="p">:</span> <span class="nb">str</span>
<span class="w">    </span><span class="sd">"""The URL of the image."""</span>

    <span class="n">kind</span><span class="p">:</span> <span class="n">Literal</span><span class="p">[</span><span class="s1">'image-url'</span><span class="p">]</span> <span class="o">=</span> <span class="s1">'image-url'</span>
<span class="w">    </span><span class="sd">"""Type identifier, this is available on all parts as a discriminator."""</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">media_type</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ImageMediaType</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Return the media type of the image, based on the url."""</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">url</span><span class="o">.</span><span class="n">endswith</span><span class="p">((</span><span class="s1">'.jpg'</span><span class="p">,</span> <span class="s1">'.jpeg'</span><span class="p">)):</span>
            <span class="k">return</span> <span class="s1">'image/jpeg'</span>
        <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">url</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s1">'.png'</span><span class="p">):</span>
            <span class="k">return</span> <span class="s1">'image/png'</span>
        <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">url</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s1">'.gif'</span><span class="p">):</span>
            <span class="k">return</span> <span class="s1">'image/gif'</span>
        <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">url</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s1">'.webp'</span><span class="p">):</span>
            <span class="k">return</span> <span class="s1">'image/webp'</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s1">'Unknown image file extension: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">url</span><span class="si">}</span><span class="s1">'</span><span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">format</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ImageFormat</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""The file format of the image.</span>

<span class="sd">        The choice of supported formats were based on the Bedrock Converse API. Other APIs don't require to use a format.</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="n">_image_format</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">media_type</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.ImageUrl.url" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">url</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_10"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_10 > code"></button><code><span class="n">url</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The URL of the image.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.ImageUrl.kind" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">kind</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_11"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_11 > code"></button><code><span class="n">kind</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Literal" href="https://docs.python.org/3/library/typing.html#typing.Literal">Literal</a></span><span class="p">[</span><span class="s1">'image-url'</span><span class="p">]</span> <span class="o">=</span> <span class="s1">'image-url'</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Type identifier, this is available on all parts as a discriminator.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.ImageUrl.media_type" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">media_type</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-property"><code>property</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_12"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_12 > code"></button><code><span class="n">media_type</span><span class="p">:</span> <span class="n"><span title="pydantic_ai.messages.ImageMediaType">ImageMediaType</span></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Return the media type of the image, based on the url.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.ImageUrl.format" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">format</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-property"><code>property</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_13"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_13 > code"></button><code><span class="nb">format</span><span class="p">:</span> <span class="n"><span title="pydantic_ai.messages.ImageFormat">ImageFormat</span></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The file format of the image.</p>
<p>The choice of supported formats were based on the Bedrock Converse API. Other APIs don't require to use a format.</p>
    </div>

</div>




  </div>

    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_ai.messages.DocumentUrl" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">DocumentUrl</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">


        <p>The URL of the document.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/messages.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 99</span>
<span class="normal">100</span>
<span class="normal">101</span>
<span class="normal">102</span>
<span class="normal">103</span>
<span class="normal">104</span>
<span class="normal">105</span>
<span class="normal">106</span>
<span class="normal">107</span>
<span class="normal">108</span>
<span class="normal">109</span>
<span class="normal">110</span>
<span class="normal">111</span>
<span class="normal">112</span>
<span class="normal">113</span>
<span class="normal">114</span>
<span class="normal">115</span>
<span class="normal">116</span>
<span class="normal">117</span>
<span class="normal">118</span>
<span class="normal">119</span>
<span class="normal">120</span>
<span class="normal">121</span>
<span class="normal">122</span>
<span class="normal">123</span></pre></div></td><td class="code"><div><pre id="__code_14"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_14 > code"></button><code tabindex="0"><span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">DocumentUrl</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""The URL of the document."""</span>

    <span class="n">url</span><span class="p">:</span> <span class="nb">str</span>
<span class="w">    </span><span class="sd">"""The URL of the document."""</span>

    <span class="n">kind</span><span class="p">:</span> <span class="n">Literal</span><span class="p">[</span><span class="s1">'document-url'</span><span class="p">]</span> <span class="o">=</span> <span class="s1">'document-url'</span>
<span class="w">    </span><span class="sd">"""Type identifier, this is available on all parts as a discriminator."""</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">media_type</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Return the media type of the document, based on the url."""</span>
        <span class="n">type_</span><span class="p">,</span> <span class="n">_</span> <span class="o">=</span> <span class="n">guess_type</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">url</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">type_</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="sa">f</span><span class="s1">'Unknown document file extension: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">url</span><span class="si">}</span><span class="s1">'</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">type_</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">format</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">DocumentFormat</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""The file format of the document.</span>

<span class="sd">        The choice of supported formats were based on the Bedrock Converse API. Other APIs don't require to use a format.</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="n">_document_format</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">media_type</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.DocumentUrl.url" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">url</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_15"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_15 > code"></button><code><span class="n">url</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The URL of the document.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.DocumentUrl.kind" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">kind</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_16"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_16 > code"></button><code><span class="n">kind</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Literal" href="https://docs.python.org/3/library/typing.html#typing.Literal">Literal</a></span><span class="p">[</span><span class="s1">'document-url'</span><span class="p">]</span> <span class="o">=</span> <span class="s1">'document-url'</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Type identifier, this is available on all parts as a discriminator.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.DocumentUrl.media_type" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">media_type</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-property"><code>property</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_17"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_17 > code"></button><code><span class="n">media_type</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Return the media type of the document, based on the url.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.DocumentUrl.format" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">format</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-property"><code>property</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_18"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_18 > code"></button><code><span class="nb">format</span><span class="p">:</span> <span class="n"><span title="pydantic_ai.messages.DocumentFormat">DocumentFormat</span></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The file format of the document.</p>
<p>The choice of supported formats were based on the Bedrock Converse API. Other APIs don't require to use a format.</p>
    </div>

</div>




  </div>

    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_ai.messages.BinaryContent" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">BinaryContent</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">


        <p>Binary content, e.g. an audio or image file.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/messages.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">143</span>
<span class="normal">144</span>
<span class="normal">145</span>
<span class="normal">146</span>
<span class="normal">147</span>
<span class="normal">148</span>
<span class="normal">149</span>
<span class="normal">150</span>
<span class="normal">151</span>
<span class="normal">152</span>
<span class="normal">153</span>
<span class="normal">154</span>
<span class="normal">155</span>
<span class="normal">156</span>
<span class="normal">157</span>
<span class="normal">158</span>
<span class="normal">159</span>
<span class="normal">160</span>
<span class="normal">161</span>
<span class="normal">162</span>
<span class="normal">163</span>
<span class="normal">164</span>
<span class="normal">165</span>
<span class="normal">166</span>
<span class="normal">167</span>
<span class="normal">168</span>
<span class="normal">169</span>
<span class="normal">170</span>
<span class="normal">171</span>
<span class="normal">172</span>
<span class="normal">173</span>
<span class="normal">174</span>
<span class="normal">175</span>
<span class="normal">176</span>
<span class="normal">177</span>
<span class="normal">178</span>
<span class="normal">179</span>
<span class="normal">180</span>
<span class="normal">181</span>
<span class="normal">182</span>
<span class="normal">183</span>
<span class="normal">184</span>
<span class="normal">185</span>
<span class="normal">186</span>
<span class="normal">187</span>
<span class="normal">188</span>
<span class="normal">189</span>
<span class="normal">190</span>
<span class="normal">191</span>
<span class="normal">192</span></pre></div></td><td class="code"><div><pre id="__code_19"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_19 > code"></button><code><span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">BinaryContent</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Binary content, e.g. an audio or image file."""</span>

    <span class="n">data</span><span class="p">:</span> <span class="nb">bytes</span>
<span class="w">    </span><span class="sd">"""The binary data."""</span>

    <span class="n">media_type</span><span class="p">:</span> <span class="n">AudioMediaType</span> <span class="o">|</span> <span class="n">ImageMediaType</span> <span class="o">|</span> <span class="n">DocumentMediaType</span> <span class="o">|</span> <span class="nb">str</span>
<span class="w">    </span><span class="sd">"""The media type of the binary data."""</span>

    <span class="n">kind</span><span class="p">:</span> <span class="n">Literal</span><span class="p">[</span><span class="s1">'binary'</span><span class="p">]</span> <span class="o">=</span> <span class="s1">'binary'</span>
<span class="w">    </span><span class="sd">"""Type identifier, this is available on all parts as a discriminator."""</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">is_audio</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Return `True` if the media type is an audio type."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">media_type</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s1">'audio/'</span><span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">is_image</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Return `True` if the media type is an image type."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">media_type</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s1">'image/'</span><span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">is_document</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Return `True` if the media type is a document type."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">media_type</span> <span class="ow">in</span> <span class="p">{</span>
            <span class="s1">'application/pdf'</span><span class="p">,</span>
            <span class="s1">'text/plain'</span><span class="p">,</span>
            <span class="s1">'text/csv'</span><span class="p">,</span>
            <span class="s1">'application/vnd.openxmlformats-officedocument.wordprocessingml.document'</span><span class="p">,</span>
            <span class="s1">'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'</span><span class="p">,</span>
            <span class="s1">'text/html'</span><span class="p">,</span>
            <span class="s1">'text/markdown'</span><span class="p">,</span>
            <span class="s1">'application/vnd.ms-excel'</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">format</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""The file format of the binary content."""</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">is_audio</span><span class="p">:</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">media_type</span> <span class="o">==</span> <span class="s1">'audio/mpeg'</span><span class="p">:</span>
                <span class="k">return</span> <span class="s1">'mp3'</span>
            <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">media_type</span> <span class="o">==</span> <span class="s1">'audio/wav'</span><span class="p">:</span>
                <span class="k">return</span> <span class="s1">'wav'</span>
        <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">is_image</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">_image_format</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">media_type</span><span class="p">)</span>
        <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">is_document</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">_document_format</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">media_type</span><span class="p">)</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s1">'Unknown media type: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">media_type</span><span class="si">}</span><span class="s1">'</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.BinaryContent.data" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">data</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_20"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_20 > code"></button><code><span class="n">data</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#bytes">bytes</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The binary data.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.BinaryContent.media_type" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">media_type</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_21"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_21 > code"></button><code><span class="n">media_type</span><span class="p">:</span> <span class="p">(</span>
    <span class="n"><span title="pydantic_ai.messages.AudioMediaType">AudioMediaType</span></span>
    <span class="o">|</span> <span class="n"><span title="pydantic_ai.messages.ImageMediaType">ImageMediaType</span></span>
    <span class="o">|</span> <span class="n"><span title="pydantic_ai.messages.DocumentMediaType">DocumentMediaType</span></span>
    <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span>
<span class="p">)</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The media type of the binary data.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.BinaryContent.kind" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">kind</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_22"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_22 > code"></button><code><span class="n">kind</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Literal" href="https://docs.python.org/3/library/typing.html#typing.Literal">Literal</a></span><span class="p">[</span><span class="s1">'binary'</span><span class="p">]</span> <span class="o">=</span> <span class="s1">'binary'</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Type identifier, this is available on all parts as a discriminator.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.BinaryContent.is_audio" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">is_audio</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-property"><code>property</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_23"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_23 > code"></button><code><span class="n">is_audio</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Return <code>True</code> if the media type is an audio type.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.BinaryContent.is_image" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">is_image</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-property"><code>property</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_24"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_24 > code"></button><code><span class="n">is_image</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Return <code>True</code> if the media type is an image type.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.BinaryContent.is_document" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">is_document</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-property"><code>property</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_25"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_25 > code"></button><code><span class="n">is_document</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Return <code>True</code> if the media type is a document type.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.BinaryContent.format" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">format</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-property"><code>property</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_26"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_26 > code"></button><code><span class="nb">format</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The file format of the binary content.</p>
    </div>

</div>




  </div>

    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_ai.messages.UserPromptPart" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">UserPromptPart</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">


        <p>A user prompt, generally written by the end user.</p>
<p>Content comes from the <code>user_prompt</code> parameter of <a class="autorefs autorefs-internal" href="../agent/#pydantic_ai.agent.Agent.run"><code>Agent.run</code></a>,
<a class="autorefs autorefs-internal" href="../agent/#pydantic_ai.agent.Agent.run_sync"><code>Agent.run_sync</code></a>, and <a class="autorefs autorefs-internal" href="../agent/#pydantic_ai.agent.Agent.run_stream"><code>Agent.run_stream</code></a>.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/messages.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">232</span>
<span class="normal">233</span>
<span class="normal">234</span>
<span class="normal">235</span>
<span class="normal">236</span>
<span class="normal">237</span>
<span class="normal">238</span>
<span class="normal">239</span>
<span class="normal">240</span>
<span class="normal">241</span>
<span class="normal">242</span>
<span class="normal">243</span>
<span class="normal">244</span>
<span class="normal">245</span>
<span class="normal">246</span>
<span class="normal">247</span>
<span class="normal">248</span>
<span class="normal">249</span>
<span class="normal">250</span>
<span class="normal">251</span>
<span class="normal">252</span>
<span class="normal">253</span>
<span class="normal">254</span>
<span class="normal">255</span></pre></div></td><td class="code"><div><pre id="__code_27"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_27 > code"></button><code><span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">UserPromptPart</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""A user prompt, generally written by the end user.</span>

<span class="sd">    Content comes from the `user_prompt` parameter of [`Agent.run`][pydantic_ai.Agent.run],</span>
<span class="sd">    [`Agent.run_sync`][pydantic_ai.Agent.run_sync], and [`Agent.run_stream`][pydantic_ai.Agent.run_stream].</span>
<span class="sd">    """</span>

    <span class="n">content</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">UserContent</span><span class="p">]</span>
<span class="w">    </span><span class="sd">"""The content of the prompt."""</span>

    <span class="n">timestamp</span><span class="p">:</span> <span class="n">datetime</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span><span class="n">default_factory</span><span class="o">=</span><span class="n">_now_utc</span><span class="p">)</span>
<span class="w">    </span><span class="sd">"""The timestamp of the prompt."""</span>

    <span class="n">part_kind</span><span class="p">:</span> <span class="n">Literal</span><span class="p">[</span><span class="s1">'user-prompt'</span><span class="p">]</span> <span class="o">=</span> <span class="s1">'user-prompt'</span>
<span class="w">    </span><span class="sd">"""Part type identifier, this is available on all parts as a discriminator."""</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">otel_event</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Event</span><span class="p">:</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">content</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
            <span class="n">content</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">content</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="c1"># TODO figure out what to record for images and audio</span>
            <span class="n">content</span> <span class="o">=</span> <span class="p">[</span><span class="n">part</span> <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">part</span><span class="p">,</span> <span class="nb">str</span><span class="p">)</span> <span class="k">else</span> <span class="p">{</span><span class="s1">'kind'</span><span class="p">:</span> <span class="n">part</span><span class="o">.</span><span class="n">kind</span><span class="p">}</span> <span class="k">for</span> <span class="n">part</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">content</span><span class="p">]</span>
        <span class="k">return</span> <span class="n">Event</span><span class="p">(</span><span class="s1">'gen_ai.user.message'</span><span class="p">,</span> <span class="n">body</span><span class="o">=</span><span class="p">{</span><span class="s1">'content'</span><span class="p">:</span> <span class="n">content</span><span class="p">,</span> <span class="s1">'role'</span><span class="p">:</span> <span class="s1">'user'</span><span class="p">})</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.UserPromptPart.content" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">content</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_28"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_28 > code"></button><code><span class="n">content</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="collections.abc.Sequence" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence">Sequence</a></span><span class="p">[</span><span class="n"><span title="pydantic_ai.messages.UserContent">UserContent</span></span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The content of the prompt.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.UserPromptPart.timestamp" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">timestamp</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_29"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_29 > code"></button><code><span class="n">timestamp</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="datetime.datetime" href="https://docs.python.org/3/library/datetime.html#datetime.datetime">datetime</a></span> <span class="o">=</span> <span class="n"><a class="autorefs autorefs-external" title="dataclasses.field" href="https://docs.python.org/3/library/dataclasses.html#dataclasses.field">field</a></span><span class="p">(</span><span class="n"><span title="dataclasses.field(default_factory)">default_factory</span></span><span class="o">=</span><span class="n"><span title="pydantic_ai._utils.now_utc">now_utc</span></span><span class="p">)</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The timestamp of the prompt.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.UserPromptPart.part_kind" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">part_kind</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_30"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_30 > code"></button><code><span class="n">part_kind</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Literal" href="https://docs.python.org/3/library/typing.html#typing.Literal">Literal</a></span><span class="p">[</span><span class="s1">'user-prompt'</span><span class="p">]</span> <span class="o">=</span> <span class="s1">'user-prompt'</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Part type identifier, this is available on all parts as a discriminator.</p>
    </div>

</div>




  </div>

    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_ai.messages.ToolReturnPart" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">ToolReturnPart</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">


        <p>A tool return message, this encodes the result of running a tool.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/messages.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">261</span>
<span class="normal">262</span>
<span class="normal">263</span>
<span class="normal">264</span>
<span class="normal">265</span>
<span class="normal">266</span>
<span class="normal">267</span>
<span class="normal">268</span>
<span class="normal">269</span>
<span class="normal">270</span>
<span class="normal">271</span>
<span class="normal">272</span>
<span class="normal">273</span>
<span class="normal">274</span>
<span class="normal">275</span>
<span class="normal">276</span>
<span class="normal">277</span>
<span class="normal">278</span>
<span class="normal">279</span>
<span class="normal">280</span>
<span class="normal">281</span>
<span class="normal">282</span>
<span class="normal">283</span>
<span class="normal">284</span>
<span class="normal">285</span>
<span class="normal">286</span>
<span class="normal">287</span>
<span class="normal">288</span>
<span class="normal">289</span>
<span class="normal">290</span>
<span class="normal">291</span>
<span class="normal">292</span>
<span class="normal">293</span>
<span class="normal">294</span>
<span class="normal">295</span>
<span class="normal">296</span>
<span class="normal">297</span>
<span class="normal">298</span>
<span class="normal">299</span></pre></div></td><td class="code"><div><pre id="__code_31"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_31 > code"></button><code tabindex="0"><span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">ToolReturnPart</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""A tool return message, this encodes the result of running a tool."""</span>

    <span class="n">tool_name</span><span class="p">:</span> <span class="nb">str</span>
<span class="w">    </span><span class="sd">"""The name of the "tool" was called."""</span>

    <span class="n">content</span><span class="p">:</span> <span class="n">Any</span>
<span class="w">    </span><span class="sd">"""The return value."""</span>

    <span class="n">tool_call_id</span><span class="p">:</span> <span class="nb">str</span>
<span class="w">    </span><span class="sd">"""The tool call identifier, this is used by some models including OpenAI."""</span>

    <span class="n">timestamp</span><span class="p">:</span> <span class="n">datetime</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span><span class="n">default_factory</span><span class="o">=</span><span class="n">_now_utc</span><span class="p">)</span>
<span class="w">    </span><span class="sd">"""The timestamp, when the tool returned."""</span>

    <span class="n">part_kind</span><span class="p">:</span> <span class="n">Literal</span><span class="p">[</span><span class="s1">'tool-return'</span><span class="p">]</span> <span class="o">=</span> <span class="s1">'tool-return'</span>
<span class="w">    </span><span class="sd">"""Part type identifier, this is available on all parts as a discriminator."""</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">model_response_str</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Return a string representation of the content for the model."""</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">content</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">content</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">tool_return_ta</span><span class="o">.</span><span class="n">dump_json</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">content</span><span class="p">)</span><span class="o">.</span><span class="n">decode</span><span class="p">()</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">model_response_object</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Return a dictionary representation of the content, wrapping non-dict types appropriately."""</span>
        <span class="c1"># gemini supports JSON dict return values, but no other JSON types, hence we wrap anything else in a dict</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">content</span><span class="p">,</span> <span class="nb">dict</span><span class="p">):</span>
            <span class="k">return</span> <span class="n">tool_return_ta</span><span class="o">.</span><span class="n">dump_python</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">content</span><span class="p">,</span> <span class="n">mode</span><span class="o">=</span><span class="s1">'json'</span><span class="p">)</span>  <span class="c1"># pyright: ignore[reportUnknownMemberType]</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="p">{</span><span class="s1">'return_value'</span><span class="p">:</span> <span class="n">tool_return_ta</span><span class="o">.</span><span class="n">dump_python</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">content</span><span class="p">,</span> <span class="n">mode</span><span class="o">=</span><span class="s1">'json'</span><span class="p">)}</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">otel_event</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Event</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">Event</span><span class="p">(</span>
            <span class="s1">'gen_ai.tool.message'</span><span class="p">,</span>
            <span class="n">body</span><span class="o">=</span><span class="p">{</span><span class="s1">'content'</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">content</span><span class="p">,</span> <span class="s1">'role'</span><span class="p">:</span> <span class="s1">'tool'</span><span class="p">,</span> <span class="s1">'id'</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">tool_call_id</span><span class="p">,</span> <span class="s1">'name'</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">tool_name</span><span class="p">},</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.ToolReturnPart.tool_name" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">tool_name</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_32"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_32 > code"></button><code><span class="n">tool_name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The name of the "tool" was called.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.ToolReturnPart.content" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">content</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_33"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_33 > code"></button><code><span class="n">content</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The return value.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.ToolReturnPart.tool_call_id" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">tool_call_id</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_34"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_34 > code"></button><code><span class="n">tool_call_id</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The tool call identifier, this is used by some models including OpenAI.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.ToolReturnPart.timestamp" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">timestamp</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_35"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_35 > code"></button><code><span class="n">timestamp</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="datetime.datetime" href="https://docs.python.org/3/library/datetime.html#datetime.datetime">datetime</a></span> <span class="o">=</span> <span class="n"><a class="autorefs autorefs-external" title="dataclasses.field" href="https://docs.python.org/3/library/dataclasses.html#dataclasses.field">field</a></span><span class="p">(</span><span class="n"><span title="dataclasses.field(default_factory)">default_factory</span></span><span class="o">=</span><span class="n"><span title="pydantic_ai._utils.now_utc">now_utc</span></span><span class="p">)</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The timestamp, when the tool returned.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.ToolReturnPart.part_kind" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">part_kind</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_36"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_36 > code"></button><code><span class="n">part_kind</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Literal" href="https://docs.python.org/3/library/typing.html#typing.Literal">Literal</a></span><span class="p">[</span><span class="s1">'tool-return'</span><span class="p">]</span> <span class="o">=</span> <span class="s1">'tool-return'</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Part type identifier, this is available on all parts as a discriminator.</p>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.messages.ToolReturnPart.model_response_str" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">model_response_str</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_37"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_37 > code"></button><code><span class="nf">model_response_str</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Return a string representation of the content for the model.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/messages.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">280</span>
<span class="normal">281</span>
<span class="normal">282</span>
<span class="normal">283</span>
<span class="normal">284</span>
<span class="normal">285</span></pre></div></td><td class="code"><div><pre id="__code_38"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_38 > code"></button><code><span class="k">def</span><span class="w"> </span><span class="nf">model_response_str</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Return a string representation of the content for the model."""</span>
    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">content</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">content</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">tool_return_ta</span><span class="o">.</span><span class="n">dump_json</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">content</span><span class="p">)</span><span class="o">.</span><span class="n">decode</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.messages.ToolReturnPart.model_response_object" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">model_response_object</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_39"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_39 > code"></button><code><span class="nf">model_response_object</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict">dict</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a></span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Return a dictionary representation of the content, wrapping non-dict types appropriately.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/messages.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">287</span>
<span class="normal">288</span>
<span class="normal">289</span>
<span class="normal">290</span>
<span class="normal">291</span>
<span class="normal">292</span>
<span class="normal">293</span></pre></div></td><td class="code"><div><pre id="__code_40"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_40 > code"></button><code tabindex="0"><span class="k">def</span><span class="w"> </span><span class="nf">model_response_object</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Return a dictionary representation of the content, wrapping non-dict types appropriately."""</span>
    <span class="c1"># gemini supports JSON dict return values, but no other JSON types, hence we wrap anything else in a dict</span>
    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">content</span><span class="p">,</span> <span class="nb">dict</span><span class="p">):</span>
        <span class="k">return</span> <span class="n">tool_return_ta</span><span class="o">.</span><span class="n">dump_python</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">content</span><span class="p">,</span> <span class="n">mode</span><span class="o">=</span><span class="s1">'json'</span><span class="p">)</span>  <span class="c1"># pyright: ignore[reportUnknownMemberType]</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">return</span> <span class="p">{</span><span class="s1">'return_value'</span><span class="p">:</span> <span class="n">tool_return_ta</span><span class="o">.</span><span class="n">dump_python</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">content</span><span class="p">,</span> <span class="n">mode</span><span class="o">=</span><span class="s1">'json'</span><span class="p">)}</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>




  </div>

    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_ai.messages.RetryPromptPart" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">RetryPromptPart</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">


        <p>A message back to a model asking it to try again.</p>
<p>This can be sent for a number of reasons:</p>
<ul>
<li>Pydantic validation of tool arguments failed, here content is derived from a Pydantic
  <a class="autorefs autorefs-external" href="https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError"><code>ValidationError</code></a></li>
<li>a tool raised a <a class="autorefs autorefs-internal" href="../exceptions/#pydantic_ai.exceptions.ModelRetry"><code>ModelRetry</code></a> exception</li>
<li>no tool was found for the tool name</li>
<li>the model returned plain text when a structured response was expected</li>
<li>Pydantic validation of a structured response failed, here content is derived from a Pydantic
  <a class="autorefs autorefs-external" href="https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError"><code>ValidationError</code></a></li>
<li>a result validator raised a <a class="autorefs autorefs-internal" href="../exceptions/#pydantic_ai.exceptions.ModelRetry"><code>ModelRetry</code></a> exception</li>
</ul>






              <details class="quote">
                <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/messages.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">305</span>
<span class="normal">306</span>
<span class="normal">307</span>
<span class="normal">308</span>
<span class="normal">309</span>
<span class="normal">310</span>
<span class="normal">311</span>
<span class="normal">312</span>
<span class="normal">313</span>
<span class="normal">314</span>
<span class="normal">315</span>
<span class="normal">316</span>
<span class="normal">317</span>
<span class="normal">318</span>
<span class="normal">319</span>
<span class="normal">320</span>
<span class="normal">321</span>
<span class="normal">322</span>
<span class="normal">323</span>
<span class="normal">324</span>
<span class="normal">325</span>
<span class="normal">326</span>
<span class="normal">327</span>
<span class="normal">328</span>
<span class="normal">329</span>
<span class="normal">330</span>
<span class="normal">331</span>
<span class="normal">332</span>
<span class="normal">333</span>
<span class="normal">334</span>
<span class="normal">335</span>
<span class="normal">336</span>
<span class="normal">337</span>
<span class="normal">338</span>
<span class="normal">339</span>
<span class="normal">340</span>
<span class="normal">341</span>
<span class="normal">342</span>
<span class="normal">343</span>
<span class="normal">344</span>
<span class="normal">345</span>
<span class="normal">346</span>
<span class="normal">347</span>
<span class="normal">348</span>
<span class="normal">349</span>
<span class="normal">350</span>
<span class="normal">351</span>
<span class="normal">352</span>
<span class="normal">353</span>
<span class="normal">354</span>
<span class="normal">355</span>
<span class="normal">356</span>
<span class="normal">357</span>
<span class="normal">358</span>
<span class="normal">359</span>
<span class="normal">360</span>
<span class="normal">361</span>
<span class="normal">362</span>
<span class="normal">363</span>
<span class="normal">364</span></pre></div></td><td class="code"><div><pre id="__code_41"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_41 > code"></button><code tabindex="0"><span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">RetryPromptPart</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""A message back to a model asking it to try again.</span>

<span class="sd">    This can be sent for a number of reasons:</span>

<span class="sd">    * Pydantic validation of tool arguments failed, here content is derived from a Pydantic</span>
<span class="sd">      [`ValidationError`][pydantic_core.ValidationError]</span>
<span class="sd">    * a tool raised a [`ModelRetry`][pydantic_ai.exceptions.ModelRetry] exception</span>
<span class="sd">    * no tool was found for the tool name</span>
<span class="sd">    * the model returned plain text when a structured response was expected</span>
<span class="sd">    * Pydantic validation of a structured response failed, here content is derived from a Pydantic</span>
<span class="sd">      [`ValidationError`][pydantic_core.ValidationError]</span>
<span class="sd">    * a result validator raised a [`ModelRetry`][pydantic_ai.exceptions.ModelRetry] exception</span>
<span class="sd">    """</span>

    <span class="n">content</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">pydantic_core</span><span class="o">.</span><span class="n">ErrorDetails</span><span class="p">]</span> <span class="o">|</span> <span class="nb">str</span>
<span class="w">    </span><span class="sd">"""Details of why and how the model should retry.</span>

<span class="sd">    If the retry was triggered by a [`ValidationError`][pydantic_core.ValidationError], this will be a list of</span>
<span class="sd">    error details.</span>
<span class="sd">    """</span>

    <span class="n">tool_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="w">    </span><span class="sd">"""The name of the tool that was called, if any."""</span>

    <span class="n">tool_call_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span><span class="n">default_factory</span><span class="o">=</span><span class="n">_generate_tool_call_id</span><span class="p">)</span>
<span class="w">    </span><span class="sd">"""The tool call identifier, this is used by some models including OpenAI.</span>

<span class="sd">    In case the tool call id is not provided by the model, PydanticAI will generate a random one.</span>
<span class="sd">    """</span>

    <span class="n">timestamp</span><span class="p">:</span> <span class="n">datetime</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span><span class="n">default_factory</span><span class="o">=</span><span class="n">_now_utc</span><span class="p">)</span>
<span class="w">    </span><span class="sd">"""The timestamp, when the retry was triggered."""</span>

    <span class="n">part_kind</span><span class="p">:</span> <span class="n">Literal</span><span class="p">[</span><span class="s1">'retry-prompt'</span><span class="p">]</span> <span class="o">=</span> <span class="s1">'retry-prompt'</span>
<span class="w">    </span><span class="sd">"""Part type identifier, this is available on all parts as a discriminator."""</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">model_response</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Return a string message describing why the retry is requested."""</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">content</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
            <span class="n">description</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">content</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">json_errors</span> <span class="o">=</span> <span class="n">error_details_ta</span><span class="o">.</span><span class="n">dump_json</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">content</span><span class="p">,</span> <span class="n">exclude</span><span class="o">=</span><span class="p">{</span><span class="s1">'__all__'</span><span class="p">:</span> <span class="p">{</span><span class="s1">'ctx'</span><span class="p">}},</span> <span class="n">indent</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
            <span class="n">description</span> <span class="o">=</span> <span class="sa">f</span><span class="s1">'</span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">content</span><span class="p">)</span><span class="si">}</span><span class="s1"> validation errors: </span><span class="si">{</span><span class="n">json_errors</span><span class="o">.</span><span class="n">decode</span><span class="p">()</span><span class="si">}</span><span class="s1">'</span>
        <span class="k">return</span> <span class="sa">f</span><span class="s1">'</span><span class="si">{</span><span class="n">description</span><span class="si">}</span><span class="se">\n\n</span><span class="s1">Fix the errors and try again.'</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">otel_event</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Event</span><span class="p">:</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">tool_name</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">Event</span><span class="p">(</span><span class="s1">'gen_ai.user.message'</span><span class="p">,</span> <span class="n">body</span><span class="o">=</span><span class="p">{</span><span class="s1">'content'</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">model_response</span><span class="p">(),</span> <span class="s1">'role'</span><span class="p">:</span> <span class="s1">'user'</span><span class="p">})</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">Event</span><span class="p">(</span>
                <span class="s1">'gen_ai.tool.message'</span><span class="p">,</span>
                <span class="n">body</span><span class="o">=</span><span class="p">{</span>
                    <span class="s1">'content'</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">model_response</span><span class="p">(),</span>
                    <span class="s1">'role'</span><span class="p">:</span> <span class="s1">'tool'</span><span class="p">,</span>
                    <span class="s1">'id'</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">tool_call_id</span><span class="p">,</span>
                    <span class="s1">'name'</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">tool_name</span><span class="p">,</span>
                <span class="p">},</span>
            <span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.RetryPromptPart.content" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">content</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_42"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_42 > code"></button><code><span class="n">content</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list">list</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" title="pydantic_core.ErrorDetails" href="https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ErrorDetails">ErrorDetails</a></span><span class="p">]</span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Details of why and how the model should retry.</p>
<p>If the retry was triggered by a <a class="autorefs autorefs-external" href="https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError"><code>ValidationError</code></a>, this will be a list of
error details.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.RetryPromptPart.tool_name" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">tool_name</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_43"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_43 > code"></button><code><span class="n">tool_name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The name of the tool that was called, if any.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.RetryPromptPart.tool_call_id" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">tool_call_id</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_44"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_44 > code"></button><code><span class="n">tool_call_id</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">=</span> <span class="n"><a class="autorefs autorefs-external" title="dataclasses.field" href="https://docs.python.org/3/library/dataclasses.html#dataclasses.field">field</a></span><span class="p">(</span>
    <span class="n"><span title="dataclasses.field(default_factory)">default_factory</span></span><span class="o">=</span><span class="n"><span title="pydantic_ai._utils.generate_tool_call_id">generate_tool_call_id</span></span>
<span class="p">)</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The tool call identifier, this is used by some models including OpenAI.</p>
<p>In case the tool call id is not provided by the model, PydanticAI will generate a random one.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.RetryPromptPart.timestamp" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">timestamp</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_45"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_45 > code"></button><code><span class="n">timestamp</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="datetime.datetime" href="https://docs.python.org/3/library/datetime.html#datetime.datetime">datetime</a></span> <span class="o">=</span> <span class="n"><a class="autorefs autorefs-external" title="dataclasses.field" href="https://docs.python.org/3/library/dataclasses.html#dataclasses.field">field</a></span><span class="p">(</span><span class="n"><span title="dataclasses.field(default_factory)">default_factory</span></span><span class="o">=</span><span class="n"><span title="pydantic_ai._utils.now_utc">now_utc</span></span><span class="p">)</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The timestamp, when the retry was triggered.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.RetryPromptPart.part_kind" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">part_kind</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_46"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_46 > code"></button><code><span class="n">part_kind</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Literal" href="https://docs.python.org/3/library/typing.html#typing.Literal">Literal</a></span><span class="p">[</span><span class="s1">'retry-prompt'</span><span class="p">]</span> <span class="o">=</span> <span class="s1">'retry-prompt'</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Part type identifier, this is available on all parts as a discriminator.</p>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.messages.RetryPromptPart.model_response" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">model_response</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_47"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_47 > code"></button><code><span class="nf">model_response</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Return a string message describing why the retry is requested.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/messages.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">343</span>
<span class="normal">344</span>
<span class="normal">345</span>
<span class="normal">346</span>
<span class="normal">347</span>
<span class="normal">348</span>
<span class="normal">349</span>
<span class="normal">350</span></pre></div></td><td class="code"><div><pre id="__code_48"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_48 > code"></button><code><span class="k">def</span><span class="w"> </span><span class="nf">model_response</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Return a string message describing why the retry is requested."""</span>
    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">content</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
        <span class="n">description</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">content</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">json_errors</span> <span class="o">=</span> <span class="n">error_details_ta</span><span class="o">.</span><span class="n">dump_json</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">content</span><span class="p">,</span> <span class="n">exclude</span><span class="o">=</span><span class="p">{</span><span class="s1">'__all__'</span><span class="p">:</span> <span class="p">{</span><span class="s1">'ctx'</span><span class="p">}},</span> <span class="n">indent</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
        <span class="n">description</span> <span class="o">=</span> <span class="sa">f</span><span class="s1">'</span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">content</span><span class="p">)</span><span class="si">}</span><span class="s1"> validation errors: </span><span class="si">{</span><span class="n">json_errors</span><span class="o">.</span><span class="n">decode</span><span class="p">()</span><span class="si">}</span><span class="s1">'</span>
    <span class="k">return</span> <span class="sa">f</span><span class="s1">'</span><span class="si">{</span><span class="n">description</span><span class="si">}</span><span class="se">\n\n</span><span class="s1">Fix the errors and try again.'</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>




  </div>

    </div>

</div>






<div class="doc doc-object doc-attribute">



<h3 id="pydantic_ai.messages.ModelRequestPart" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">ModelRequestPart</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span>

</h3>
<div class="language-python doc-signature highlight"><pre id="__code_49"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_49 > code"></button><code><span class="n">ModelRequestPart</span> <span class="o">=</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Annotated" href="https://docs.python.org/3/library/typing.html#typing.Annotated">Annotated</a></span><span class="p">[</span>
    <span class="n"><a class="autorefs autorefs-external" title="typing.Union" href="https://docs.python.org/3/library/typing.html#typing.Union">Union</a></span><span class="p">[</span>
        <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.SystemPromptPart" href="#pydantic_ai.messages.SystemPromptPart">SystemPromptPart</a></span><span class="p">,</span>
        <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.UserPromptPart" href="#pydantic_ai.messages.UserPromptPart">UserPromptPart</a></span><span class="p">,</span>
        <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ToolReturnPart" href="#pydantic_ai.messages.ToolReturnPart">ToolReturnPart</a></span><span class="p">,</span>
        <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.RetryPromptPart" href="#pydantic_ai.messages.RetryPromptPart">RetryPromptPart</a></span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n"><a class="autorefs autorefs-external" title="pydantic.Discriminator" href="https://docs.pydantic.dev/latest/api/types/#pydantic.types.Discriminator">Discriminator</a></span><span class="p">(</span><span class="s2">"part_kind"</span><span class="p">),</span>
<span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>A message part sent by PydanticAI to a model.</p>
    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_ai.messages.ModelRequest" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">ModelRequest</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">


        <p>A request generated by PydanticAI and sent to a model, e.g. a message from the PydanticAI app to the model.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/messages.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">373</span>
<span class="normal">374</span>
<span class="normal">375</span>
<span class="normal">376</span>
<span class="normal">377</span>
<span class="normal">378</span>
<span class="normal">379</span>
<span class="normal">380</span>
<span class="normal">381</span></pre></div></td><td class="code"><div><pre id="__code_50"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_50 > code"></button><code tabindex="0"><span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">ModelRequest</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""A request generated by PydanticAI and sent to a model, e.g. a message from the PydanticAI app to the model."""</span>

    <span class="n">parts</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">ModelRequestPart</span><span class="p">]</span>
<span class="w">    </span><span class="sd">"""The parts of the user message."""</span>

    <span class="n">kind</span><span class="p">:</span> <span class="n">Literal</span><span class="p">[</span><span class="s1">'request'</span><span class="p">]</span> <span class="o">=</span> <span class="s1">'request'</span>
<span class="w">    </span><span class="sd">"""Message type identifier, this is available on all parts as a discriminator."""</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.ModelRequest.parts" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">parts</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_51"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_51 > code"></button><code><span class="n">parts</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list">list</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ModelRequestPart" href="#pydantic_ai.messages.ModelRequestPart">ModelRequestPart</a></span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The parts of the user message.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.ModelRequest.kind" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">kind</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_52"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_52 > code"></button><code><span class="n">kind</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Literal" href="https://docs.python.org/3/library/typing.html#typing.Literal">Literal</a></span><span class="p">[</span><span class="s1">'request'</span><span class="p">]</span> <span class="o">=</span> <span class="s1">'request'</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Message type identifier, this is available on all parts as a discriminator.</p>
    </div>

</div>




  </div>

    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_ai.messages.TextPart" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">TextPart</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">


        <p>A plain text response from a model.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/messages.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">384</span>
<span class="normal">385</span>
<span class="normal">386</span>
<span class="normal">387</span>
<span class="normal">388</span>
<span class="normal">389</span>
<span class="normal">390</span>
<span class="normal">391</span>
<span class="normal">392</span>
<span class="normal">393</span>
<span class="normal">394</span>
<span class="normal">395</span>
<span class="normal">396</span></pre></div></td><td class="code"><div><pre id="__code_53"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_53 > code"></button><code><span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">TextPart</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""A plain text response from a model."""</span>

    <span class="n">content</span><span class="p">:</span> <span class="nb">str</span>
<span class="w">    </span><span class="sd">"""The text content of the response."""</span>

    <span class="n">part_kind</span><span class="p">:</span> <span class="n">Literal</span><span class="p">[</span><span class="s1">'text'</span><span class="p">]</span> <span class="o">=</span> <span class="s1">'text'</span>
<span class="w">    </span><span class="sd">"""Part type identifier, this is available on all parts as a discriminator."""</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">has_content</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Return `True` if the text content is non-empty."""</span>
        <span class="k">return</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">content</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.TextPart.content" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">content</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_54"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_54 > code"></button><code><span class="n">content</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The text content of the response.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.TextPart.part_kind" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">part_kind</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_55"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_55 > code"></button><code><span class="n">part_kind</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Literal" href="https://docs.python.org/3/library/typing.html#typing.Literal">Literal</a></span><span class="p">[</span><span class="s1">'text'</span><span class="p">]</span> <span class="o">=</span> <span class="s1">'text'</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Part type identifier, this is available on all parts as a discriminator.</p>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.messages.TextPart.has_content" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">has_content</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_56"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_56 > code"></button><code><span class="nf">has_content</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Return <code>True</code> if the text content is non-empty.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/messages.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">394</span>
<span class="normal">395</span>
<span class="normal">396</span></pre></div></td><td class="code"><div><pre id="__code_57"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_57 > code"></button><code><span class="k">def</span><span class="w"> </span><span class="nf">has_content</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Return `True` if the text content is non-empty."""</span>
    <span class="k">return</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">content</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>




  </div>

    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_ai.messages.ToolCallPart" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">ToolCallPart</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">


        <p>A tool call from a model.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/messages.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">399</span>
<span class="normal">400</span>
<span class="normal">401</span>
<span class="normal">402</span>
<span class="normal">403</span>
<span class="normal">404</span>
<span class="normal">405</span>
<span class="normal">406</span>
<span class="normal">407</span>
<span class="normal">408</span>
<span class="normal">409</span>
<span class="normal">410</span>
<span class="normal">411</span>
<span class="normal">412</span>
<span class="normal">413</span>
<span class="normal">414</span>
<span class="normal">415</span>
<span class="normal">416</span>
<span class="normal">417</span>
<span class="normal">418</span>
<span class="normal">419</span>
<span class="normal">420</span>
<span class="normal">421</span>
<span class="normal">422</span>
<span class="normal">423</span>
<span class="normal">424</span>
<span class="normal">425</span>
<span class="normal">426</span>
<span class="normal">427</span>
<span class="normal">428</span>
<span class="normal">429</span>
<span class="normal">430</span>
<span class="normal">431</span>
<span class="normal">432</span>
<span class="normal">433</span>
<span class="normal">434</span>
<span class="normal">435</span>
<span class="normal">436</span>
<span class="normal">437</span>
<span class="normal">438</span>
<span class="normal">439</span>
<span class="normal">440</span>
<span class="normal">441</span>
<span class="normal">442</span>
<span class="normal">443</span>
<span class="normal">444</span>
<span class="normal">445</span>
<span class="normal">446</span>
<span class="normal">447</span>
<span class="normal">448</span></pre></div></td><td class="code"><div><pre id="__code_58"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_58 > code"></button><code><span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">ToolCallPart</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""A tool call from a model."""</span>

    <span class="n">tool_name</span><span class="p">:</span> <span class="nb">str</span>
<span class="w">    </span><span class="sd">"""The name of the tool to call."""</span>

    <span class="n">args</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span>
<span class="w">    </span><span class="sd">"""The arguments to pass to the tool.</span>

<span class="sd">    This is stored either as a JSON string or a Python dictionary depending on how data was received.</span>
<span class="sd">    """</span>

    <span class="n">tool_call_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span><span class="n">default_factory</span><span class="o">=</span><span class="n">_generate_tool_call_id</span><span class="p">)</span>
<span class="w">    </span><span class="sd">"""The tool call identifier, this is used by some models including OpenAI.</span>

<span class="sd">    In case the tool call id is not provided by the model, PydanticAI will generate a random one.</span>
<span class="sd">    """</span>

    <span class="n">part_kind</span><span class="p">:</span> <span class="n">Literal</span><span class="p">[</span><span class="s1">'tool-call'</span><span class="p">]</span> <span class="o">=</span> <span class="s1">'tool-call'</span>
<span class="w">    </span><span class="sd">"""Part type identifier, this is available on all parts as a discriminator."""</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">args_as_dict</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Return the arguments as a Python dictionary.</span>

<span class="sd">        This is just for convenience with models that require dicts as input.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">,</span> <span class="nb">dict</span><span class="p">):</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">args</span>
        <span class="n">args</span> <span class="o">=</span> <span class="n">pydantic_core</span><span class="o">.</span><span class="n">from_json</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">)</span>
        <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">args</span><span class="p">,</span> <span class="nb">dict</span><span class="p">),</span> <span class="s1">'args should be a dict'</span>
        <span class="k">return</span> <span class="n">cast</span><span class="p">(</span><span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span> <span class="n">args</span><span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">args_as_json_str</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Return the arguments as a JSON string.</span>

<span class="sd">        This is just for convenience with models that require JSON strings as input.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">args</span>
        <span class="k">return</span> <span class="n">pydantic_core</span><span class="o">.</span><span class="n">to_json</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">)</span><span class="o">.</span><span class="n">decode</span><span class="p">()</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">has_content</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Return `True` if the arguments contain any data."""</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">,</span> <span class="nb">dict</span><span class="p">):</span>
            <span class="c1"># TODO: This should probably return True if you have the value False, or 0, etc.</span>
            <span class="c1">#   It makes sense to me to ignore empty strings, but not sure about empty lists or dicts</span>
            <span class="k">return</span> <span class="nb">any</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="o">.</span><span class="n">values</span><span class="p">())</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.ToolCallPart.tool_name" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">tool_name</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_59"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_59 > code"></button><code><span class="n">tool_name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The name of the tool to call.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.ToolCallPart.args" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">args</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_60"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_60 > code"></button><code><span class="n">args</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict">dict</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a></span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The arguments to pass to the tool.</p>
<p>This is stored either as a JSON string or a Python dictionary depending on how data was received.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.ToolCallPart.tool_call_id" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">tool_call_id</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_61"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_61 > code"></button><code><span class="n">tool_call_id</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">=</span> <span class="n"><a class="autorefs autorefs-external" title="dataclasses.field" href="https://docs.python.org/3/library/dataclasses.html#dataclasses.field">field</a></span><span class="p">(</span>
    <span class="n"><span title="dataclasses.field(default_factory)">default_factory</span></span><span class="o">=</span><span class="n"><span title="pydantic_ai._utils.generate_tool_call_id">generate_tool_call_id</span></span>
<span class="p">)</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The tool call identifier, this is used by some models including OpenAI.</p>
<p>In case the tool call id is not provided by the model, PydanticAI will generate a random one.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.ToolCallPart.part_kind" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">part_kind</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_62"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_62 > code"></button><code><span class="n">part_kind</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Literal" href="https://docs.python.org/3/library/typing.html#typing.Literal">Literal</a></span><span class="p">[</span><span class="s1">'tool-call'</span><span class="p">]</span> <span class="o">=</span> <span class="s1">'tool-call'</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Part type identifier, this is available on all parts as a discriminator.</p>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.messages.ToolCallPart.args_as_dict" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">args_as_dict</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_63"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_63 > code"></button><code><span class="nf">args_as_dict</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict">dict</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a></span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Return the arguments as a Python dictionary.</p>
<p>This is just for convenience with models that require dicts as input.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/messages.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">421</span>
<span class="normal">422</span>
<span class="normal">423</span>
<span class="normal">424</span>
<span class="normal">425</span>
<span class="normal">426</span>
<span class="normal">427</span>
<span class="normal">428</span>
<span class="normal">429</span>
<span class="normal">430</span></pre></div></td><td class="code"><div><pre id="__code_64"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_64 > code"></button><code><span class="k">def</span><span class="w"> </span><span class="nf">args_as_dict</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Return the arguments as a Python dictionary.</span>

<span class="sd">    This is just for convenience with models that require dicts as input.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">,</span> <span class="nb">dict</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">args</span>
    <span class="n">args</span> <span class="o">=</span> <span class="n">pydantic_core</span><span class="o">.</span><span class="n">from_json</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">)</span>
    <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">args</span><span class="p">,</span> <span class="nb">dict</span><span class="p">),</span> <span class="s1">'args should be a dict'</span>
    <span class="k">return</span> <span class="n">cast</span><span class="p">(</span><span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span> <span class="n">args</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.messages.ToolCallPart.args_as_json_str" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">args_as_json_str</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_65"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_65 > code"></button><code><span class="nf">args_as_json_str</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Return the arguments as a JSON string.</p>
<p>This is just for convenience with models that require JSON strings as input.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/messages.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">432</span>
<span class="normal">433</span>
<span class="normal">434</span>
<span class="normal">435</span>
<span class="normal">436</span>
<span class="normal">437</span>
<span class="normal">438</span>
<span class="normal">439</span></pre></div></td><td class="code"><div><pre id="__code_66"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_66 > code"></button><code><span class="k">def</span><span class="w"> </span><span class="nf">args_as_json_str</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Return the arguments as a JSON string.</span>

<span class="sd">    This is just for convenience with models that require JSON strings as input.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">args</span>
    <span class="k">return</span> <span class="n">pydantic_core</span><span class="o">.</span><span class="n">to_json</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">)</span><span class="o">.</span><span class="n">decode</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.messages.ToolCallPart.has_content" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">has_content</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_67"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_67 > code"></button><code><span class="nf">has_content</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Return <code>True</code> if the arguments contain any data.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/messages.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">441</span>
<span class="normal">442</span>
<span class="normal">443</span>
<span class="normal">444</span>
<span class="normal">445</span>
<span class="normal">446</span>
<span class="normal">447</span>
<span class="normal">448</span></pre></div></td><td class="code"><div><pre id="__code_68"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_68 > code"></button><code><span class="k">def</span><span class="w"> </span><span class="nf">has_content</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Return `True` if the arguments contain any data."""</span>
    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">,</span> <span class="nb">dict</span><span class="p">):</span>
        <span class="c1"># TODO: This should probably return True if you have the value False, or 0, etc.</span>
        <span class="c1">#   It makes sense to me to ignore empty strings, but not sure about empty lists or dicts</span>
        <span class="k">return</span> <span class="nb">any</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="o">.</span><span class="n">values</span><span class="p">())</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">return</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>




  </div>

    </div>

</div>






<div class="doc doc-object doc-attribute">



<h3 id="pydantic_ai.messages.ModelResponsePart" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">ModelResponsePart</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span>

</h3>
<div class="language-python doc-signature highlight"><pre id="__code_69"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_69 > code"></button><code><span class="n">ModelResponsePart</span> <span class="o">=</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Annotated" href="https://docs.python.org/3/library/typing.html#typing.Annotated">Annotated</a></span><span class="p">[</span>
    <span class="n"><a class="autorefs autorefs-external" title="typing.Union" href="https://docs.python.org/3/library/typing.html#typing.Union">Union</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.TextPart" href="#pydantic_ai.messages.TextPart">TextPart</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ToolCallPart" href="#pydantic_ai.messages.ToolCallPart">ToolCallPart</a></span><span class="p">],</span>
    <span class="n"><a class="autorefs autorefs-external" title="pydantic.Discriminator" href="https://docs.pydantic.dev/latest/api/types/#pydantic.types.Discriminator">Discriminator</a></span><span class="p">(</span><span class="s2">"part_kind"</span><span class="p">),</span>
<span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>A message part returned by a model.</p>
    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_ai.messages.ModelResponse" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">ModelResponse</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">


        <p>A response from a model, e.g. a message from the model to the PydanticAI app.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/messages.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">455</span>
<span class="normal">456</span>
<span class="normal">457</span>
<span class="normal">458</span>
<span class="normal">459</span>
<span class="normal">460</span>
<span class="normal">461</span>
<span class="normal">462</span>
<span class="normal">463</span>
<span class="normal">464</span>
<span class="normal">465</span>
<span class="normal">466</span>
<span class="normal">467</span>
<span class="normal">468</span>
<span class="normal">469</span>
<span class="normal">470</span>
<span class="normal">471</span>
<span class="normal">472</span>
<span class="normal">473</span>
<span class="normal">474</span>
<span class="normal">475</span>
<span class="normal">476</span>
<span class="normal">477</span>
<span class="normal">478</span>
<span class="normal">479</span>
<span class="normal">480</span>
<span class="normal">481</span>
<span class="normal">482</span>
<span class="normal">483</span>
<span class="normal">484</span>
<span class="normal">485</span>
<span class="normal">486</span>
<span class="normal">487</span>
<span class="normal">488</span>
<span class="normal">489</span>
<span class="normal">490</span>
<span class="normal">491</span>
<span class="normal">492</span>
<span class="normal">493</span>
<span class="normal">494</span>
<span class="normal">495</span>
<span class="normal">496</span>
<span class="normal">497</span>
<span class="normal">498</span>
<span class="normal">499</span>
<span class="normal">500</span>
<span class="normal">501</span>
<span class="normal">502</span></pre></div></td><td class="code"><div><pre id="__code_70"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_70 > code"></button><code><span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">ModelResponse</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""A response from a model, e.g. a message from the model to the PydanticAI app."""</span>

    <span class="n">parts</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">ModelResponsePart</span><span class="p">]</span>
<span class="w">    </span><span class="sd">"""The parts of the model message."""</span>

    <span class="n">model_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="w">    </span><span class="sd">"""The name of the model that generated the response."""</span>

    <span class="n">timestamp</span><span class="p">:</span> <span class="n">datetime</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span><span class="n">default_factory</span><span class="o">=</span><span class="n">_now_utc</span><span class="p">)</span>
<span class="w">    </span><span class="sd">"""The timestamp of the response.</span>

<span class="sd">    If the model provides a timestamp in the response (as OpenAI does) that will be used.</span>
<span class="sd">    """</span>

    <span class="n">kind</span><span class="p">:</span> <span class="n">Literal</span><span class="p">[</span><span class="s1">'response'</span><span class="p">]</span> <span class="o">=</span> <span class="s1">'response'</span>
<span class="w">    </span><span class="sd">"""Message type identifier, this is available on all parts as a discriminator."""</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">otel_events</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">list</span><span class="p">[</span><span class="n">Event</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Return OpenTelemetry events for the response."""</span>
        <span class="n">result</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">Event</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="k">def</span><span class="w"> </span><span class="nf">new_event_body</span><span class="p">():</span>
            <span class="n">new_body</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span><span class="s1">'role'</span><span class="p">:</span> <span class="s1">'assistant'</span><span class="p">}</span>
            <span class="n">ev</span> <span class="o">=</span> <span class="n">Event</span><span class="p">(</span><span class="s1">'gen_ai.assistant.message'</span><span class="p">,</span> <span class="n">body</span><span class="o">=</span><span class="n">new_body</span><span class="p">)</span>
            <span class="n">result</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">ev</span><span class="p">)</span>
            <span class="k">return</span> <span class="n">new_body</span>

        <span class="n">body</span> <span class="o">=</span> <span class="n">new_event_body</span><span class="p">()</span>
        <span class="k">for</span> <span class="n">part</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">parts</span><span class="p">:</span>
            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">part</span><span class="p">,</span> <span class="n">ToolCallPart</span><span class="p">):</span>
                <span class="n">body</span><span class="o">.</span><span class="n">setdefault</span><span class="p">(</span><span class="s1">'tool_calls'</span><span class="p">,</span> <span class="p">[])</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                    <span class="p">{</span>
                        <span class="s1">'id'</span><span class="p">:</span> <span class="n">part</span><span class="o">.</span><span class="n">tool_call_id</span><span class="p">,</span>
                        <span class="s1">'type'</span><span class="p">:</span> <span class="s1">'function'</span><span class="p">,</span>  <span class="c1"># TODO https://github.com/pydantic/pydantic-ai/issues/888</span>
                        <span class="s1">'function'</span><span class="p">:</span> <span class="p">{</span>
                            <span class="s1">'name'</span><span class="p">:</span> <span class="n">part</span><span class="o">.</span><span class="n">tool_name</span><span class="p">,</span>
                            <span class="s1">'arguments'</span><span class="p">:</span> <span class="n">part</span><span class="o">.</span><span class="n">args</span><span class="p">,</span>
                        <span class="p">},</span>
                    <span class="p">}</span>
                <span class="p">)</span>
            <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">part</span><span class="p">,</span> <span class="n">TextPart</span><span class="p">):</span>
                <span class="k">if</span> <span class="n">body</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'content'</span><span class="p">):</span>
                    <span class="n">body</span> <span class="o">=</span> <span class="n">new_event_body</span><span class="p">()</span>
                <span class="n">body</span><span class="p">[</span><span class="s1">'content'</span><span class="p">]</span> <span class="o">=</span> <span class="n">part</span><span class="o">.</span><span class="n">content</span>

        <span class="k">return</span> <span class="n">result</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.ModelResponse.parts" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">parts</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_71"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_71 > code"></button><code><span class="n">parts</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list">list</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ModelResponsePart" href="#pydantic_ai.messages.ModelResponsePart">ModelResponsePart</a></span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The parts of the model message.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.ModelResponse.model_name" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">model_name</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_72"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_72 > code"></button><code><span class="n">model_name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The name of the model that generated the response.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.ModelResponse.timestamp" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">timestamp</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_73"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_73 > code"></button><code><span class="n">timestamp</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="datetime.datetime" href="https://docs.python.org/3/library/datetime.html#datetime.datetime">datetime</a></span> <span class="o">=</span> <span class="n"><a class="autorefs autorefs-external" title="dataclasses.field" href="https://docs.python.org/3/library/dataclasses.html#dataclasses.field">field</a></span><span class="p">(</span><span class="n"><span title="dataclasses.field(default_factory)">default_factory</span></span><span class="o">=</span><span class="n"><span title="pydantic_ai._utils.now_utc">now_utc</span></span><span class="p">)</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The timestamp of the response.</p>
<p>If the model provides a timestamp in the response (as OpenAI does) that will be used.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.ModelResponse.kind" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">kind</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_74"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_74 > code"></button><code><span class="n">kind</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Literal" href="https://docs.python.org/3/library/typing.html#typing.Literal">Literal</a></span><span class="p">[</span><span class="s1">'response'</span><span class="p">]</span> <span class="o">=</span> <span class="s1">'response'</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Message type identifier, this is available on all parts as a discriminator.</p>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.messages.ModelResponse.otel_events" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">otel_events</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_75"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_75 > code"></button><code><span class="nf">otel_events</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list">list</a></span><span class="p">[</span><span class="n"><span title="opentelemetry._events.Event">Event</span></span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Return OpenTelemetry events for the response.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/messages.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">474</span>
<span class="normal">475</span>
<span class="normal">476</span>
<span class="normal">477</span>
<span class="normal">478</span>
<span class="normal">479</span>
<span class="normal">480</span>
<span class="normal">481</span>
<span class="normal">482</span>
<span class="normal">483</span>
<span class="normal">484</span>
<span class="normal">485</span>
<span class="normal">486</span>
<span class="normal">487</span>
<span class="normal">488</span>
<span class="normal">489</span>
<span class="normal">490</span>
<span class="normal">491</span>
<span class="normal">492</span>
<span class="normal">493</span>
<span class="normal">494</span>
<span class="normal">495</span>
<span class="normal">496</span>
<span class="normal">497</span>
<span class="normal">498</span>
<span class="normal">499</span>
<span class="normal">500</span>
<span class="normal">501</span>
<span class="normal">502</span></pre></div></td><td class="code"><div><pre id="__code_76"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_76 > code"></button><code><span class="k">def</span><span class="w"> </span><span class="nf">otel_events</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">list</span><span class="p">[</span><span class="n">Event</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Return OpenTelemetry events for the response."""</span>
    <span class="n">result</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">Event</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">new_event_body</span><span class="p">():</span>
        <span class="n">new_body</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span><span class="s1">'role'</span><span class="p">:</span> <span class="s1">'assistant'</span><span class="p">}</span>
        <span class="n">ev</span> <span class="o">=</span> <span class="n">Event</span><span class="p">(</span><span class="s1">'gen_ai.assistant.message'</span><span class="p">,</span> <span class="n">body</span><span class="o">=</span><span class="n">new_body</span><span class="p">)</span>
        <span class="n">result</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">ev</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">new_body</span>

    <span class="n">body</span> <span class="o">=</span> <span class="n">new_event_body</span><span class="p">()</span>
    <span class="k">for</span> <span class="n">part</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">parts</span><span class="p">:</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">part</span><span class="p">,</span> <span class="n">ToolCallPart</span><span class="p">):</span>
            <span class="n">body</span><span class="o">.</span><span class="n">setdefault</span><span class="p">(</span><span class="s1">'tool_calls'</span><span class="p">,</span> <span class="p">[])</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                <span class="p">{</span>
                    <span class="s1">'id'</span><span class="p">:</span> <span class="n">part</span><span class="o">.</span><span class="n">tool_call_id</span><span class="p">,</span>
                    <span class="s1">'type'</span><span class="p">:</span> <span class="s1">'function'</span><span class="p">,</span>  <span class="c1"># TODO https://github.com/pydantic/pydantic-ai/issues/888</span>
                    <span class="s1">'function'</span><span class="p">:</span> <span class="p">{</span>
                        <span class="s1">'name'</span><span class="p">:</span> <span class="n">part</span><span class="o">.</span><span class="n">tool_name</span><span class="p">,</span>
                        <span class="s1">'arguments'</span><span class="p">:</span> <span class="n">part</span><span class="o">.</span><span class="n">args</span><span class="p">,</span>
                    <span class="p">},</span>
                <span class="p">}</span>
            <span class="p">)</span>
        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">part</span><span class="p">,</span> <span class="n">TextPart</span><span class="p">):</span>
            <span class="k">if</span> <span class="n">body</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'content'</span><span class="p">):</span>
                <span class="n">body</span> <span class="o">=</span> <span class="n">new_event_body</span><span class="p">()</span>
            <span class="n">body</span><span class="p">[</span><span class="s1">'content'</span><span class="p">]</span> <span class="o">=</span> <span class="n">part</span><span class="o">.</span><span class="n">content</span>

    <span class="k">return</span> <span class="n">result</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>




  </div>

    </div>

</div>






<div class="doc doc-object doc-attribute">



<h3 id="pydantic_ai.messages.ModelMessage" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">ModelMessage</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span>

</h3>
<div class="language-python doc-signature highlight"><pre id="__code_77"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_77 > code"></button><code><span class="n">ModelMessage</span> <span class="o">=</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Annotated" href="https://docs.python.org/3/library/typing.html#typing.Annotated">Annotated</a></span><span class="p">[</span>
    <span class="n"><a class="autorefs autorefs-external" title="typing.Union" href="https://docs.python.org/3/library/typing.html#typing.Union">Union</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ModelRequest" href="#pydantic_ai.messages.ModelRequest">ModelRequest</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ModelResponse" href="#pydantic_ai.messages.ModelResponse">ModelResponse</a></span><span class="p">],</span>
    <span class="n"><a class="autorefs autorefs-external" title="pydantic.Discriminator" href="https://docs.pydantic.dev/latest/api/types/#pydantic.types.Discriminator">Discriminator</a></span><span class="p">(</span><span class="s2">"kind"</span><span class="p">),</span>
<span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Any message sent to or returned by a model.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h3 id="pydantic_ai.messages.ModelMessagesTypeAdapter" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">ModelMessagesTypeAdapter</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span>

</h3>
<div class="language-python doc-signature highlight"><pre id="__code_78"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_78 > code"></button><code><span class="n">ModelMessagesTypeAdapter</span> <span class="o">=</span> <span class="n"><a class="autorefs autorefs-external" title="pydantic.TypeAdapter" href="https://docs.pydantic.dev/latest/api/type_adapter/#pydantic.type_adapter.TypeAdapter">TypeAdapter</a></span><span class="p">(</span>
    <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list">list</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ModelMessage" href="#pydantic_ai.messages.ModelMessage">ModelMessage</a></span><span class="p">],</span>
    <span class="n"><span title="pydantic.TypeAdapter(config)">config</span></span><span class="o">=</span><span class="n"><a class="autorefs autorefs-external" title="pydantic.ConfigDict" href="https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict">ConfigDict</a></span><span class="p">(</span>
        <span class="n"><span title="pydantic.ConfigDict(defer_build)">defer_build</span></span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n"><span title="pydantic.ConfigDict(ser_json_bytes)">ser_json_bytes</span></span><span class="o">=</span><span class="s2">"base64"</span>
    <span class="p">),</span>
<span class="p">)</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Pydantic <a class="autorefs autorefs-external" href="https://docs.pydantic.dev/latest/api/type_adapter/#pydantic.type_adapter.TypeAdapter"><code>TypeAdapter</code></a> for (de)serializing messages.</p>
    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_ai.messages.TextPartDelta" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">TextPartDelta</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">


        <p>A partial update (delta) for a <code>TextPart</code> to append new text content.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/messages.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">514</span>
<span class="normal">515</span>
<span class="normal">516</span>
<span class="normal">517</span>
<span class="normal">518</span>
<span class="normal">519</span>
<span class="normal">520</span>
<span class="normal">521</span>
<span class="normal">522</span>
<span class="normal">523</span>
<span class="normal">524</span>
<span class="normal">525</span>
<span class="normal">526</span>
<span class="normal">527</span>
<span class="normal">528</span>
<span class="normal">529</span>
<span class="normal">530</span>
<span class="normal">531</span>
<span class="normal">532</span>
<span class="normal">533</span>
<span class="normal">534</span>
<span class="normal">535</span>
<span class="normal">536</span>
<span class="normal">537</span>
<span class="normal">538</span></pre></div></td><td class="code"><div><pre id="__code_79"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_79 > code"></button><code><span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">TextPartDelta</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""A partial update (delta) for a `TextPart` to append new text content."""</span>

    <span class="n">content_delta</span><span class="p">:</span> <span class="nb">str</span>
<span class="w">    </span><span class="sd">"""The incremental text content to add to the existing `TextPart` content."""</span>

    <span class="n">part_delta_kind</span><span class="p">:</span> <span class="n">Literal</span><span class="p">[</span><span class="s1">'text'</span><span class="p">]</span> <span class="o">=</span> <span class="s1">'text'</span>
<span class="w">    </span><span class="sd">"""Part delta type identifier, used as a discriminator."""</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">apply</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">part</span><span class="p">:</span> <span class="n">ModelResponsePart</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TextPart</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Apply this text delta to an existing `TextPart`.</span>

<span class="sd">        Args:</span>
<span class="sd">            part: The existing model response part, which must be a `TextPart`.</span>

<span class="sd">        Returns:</span>
<span class="sd">            A new `TextPart` with updated text content.</span>

<span class="sd">        Raises:</span>
<span class="sd">            ValueError: If `part` is not a `TextPart`.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">part</span><span class="p">,</span> <span class="n">TextPart</span><span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s1">'Cannot apply TextPartDeltas to non-TextParts'</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">replace</span><span class="p">(</span><span class="n">part</span><span class="p">,</span> <span class="n">content</span><span class="o">=</span><span class="n">part</span><span class="o">.</span><span class="n">content</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">content_delta</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.TextPartDelta.content_delta" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">content_delta</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_80"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_80 > code"></button><code><span class="n">content_delta</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The incremental text content to add to the existing <code>TextPart</code> content.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.TextPartDelta.part_delta_kind" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">part_delta_kind</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_81"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_81 > code"></button><code><span class="n">part_delta_kind</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Literal" href="https://docs.python.org/3/library/typing.html#typing.Literal">Literal</a></span><span class="p">[</span><span class="s1">'text'</span><span class="p">]</span> <span class="o">=</span> <span class="s1">'text'</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Part delta type identifier, used as a discriminator.</p>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.messages.TextPartDelta.apply" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">apply</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_82"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_82 > code"></button><code><span class="nf">apply</span><span class="p">(</span><span class="n">part</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ModelResponsePart" href="#pydantic_ai.messages.ModelResponsePart">ModelResponsePart</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.TextPart" href="#pydantic_ai.messages.TextPart">TextPart</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Apply this text delta to an existing <code>TextPart</code>.</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <div class="md-typeset__scrollwrap"><div class="md-typeset__table"><table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>part</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ModelResponsePart" href="#pydantic_ai.messages.ModelResponsePart">ModelResponsePart</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The existing model response part, which must be a <code>TextPart</code>.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
      </tbody>
    </table></div></div>


    <p><span class="doc-section-title">Returns:</span></p>
    <div class="md-typeset__scrollwrap"><div class="md-typeset__table"><table>
      <thead>
        <tr>
          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_ai.messages.TextPart" href="#pydantic_ai.messages.TextPart">TextPart</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>A new <code>TextPart</code> with updated text content.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table></div></div>


<p><span class="doc-section-title">Raises:</span></p>
    <div class="md-typeset__scrollwrap"><div class="md-typeset__table"><table>
      <thead>
        <tr>
          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/exceptions.html#ValueError">ValueError</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>If <code>part</code> is not a <code>TextPart</code>.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/messages.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">524</span>
<span class="normal">525</span>
<span class="normal">526</span>
<span class="normal">527</span>
<span class="normal">528</span>
<span class="normal">529</span>
<span class="normal">530</span>
<span class="normal">531</span>
<span class="normal">532</span>
<span class="normal">533</span>
<span class="normal">534</span>
<span class="normal">535</span>
<span class="normal">536</span>
<span class="normal">537</span>
<span class="normal">538</span></pre></div></td><td class="code"><div><pre id="__code_83"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_83 > code"></button><code><span class="k">def</span><span class="w"> </span><span class="nf">apply</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">part</span><span class="p">:</span> <span class="n">ModelResponsePart</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TextPart</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Apply this text delta to an existing `TextPart`.</span>

<span class="sd">    Args:</span>
<span class="sd">        part: The existing model response part, which must be a `TextPart`.</span>

<span class="sd">    Returns:</span>
<span class="sd">        A new `TextPart` with updated text content.</span>

<span class="sd">    Raises:</span>
<span class="sd">        ValueError: If `part` is not a `TextPart`.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">part</span><span class="p">,</span> <span class="n">TextPart</span><span class="p">):</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s1">'Cannot apply TextPartDeltas to non-TextParts'</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">replace</span><span class="p">(</span><span class="n">part</span><span class="p">,</span> <span class="n">content</span><span class="o">=</span><span class="n">part</span><span class="o">.</span><span class="n">content</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">content_delta</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>




  </div>

    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_ai.messages.ToolCallPartDelta" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">ToolCallPartDelta</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">


        <p>A partial update (delta) for a <code>ToolCallPart</code> to modify tool name, arguments, or tool call ID.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/messages.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">541</span>
<span class="normal">542</span>
<span class="normal">543</span>
<span class="normal">544</span>
<span class="normal">545</span>
<span class="normal">546</span>
<span class="normal">547</span>
<span class="normal">548</span>
<span class="normal">549</span>
<span class="normal">550</span>
<span class="normal">551</span>
<span class="normal">552</span>
<span class="normal">553</span>
<span class="normal">554</span>
<span class="normal">555</span>
<span class="normal">556</span>
<span class="normal">557</span>
<span class="normal">558</span>
<span class="normal">559</span>
<span class="normal">560</span>
<span class="normal">561</span>
<span class="normal">562</span>
<span class="normal">563</span>
<span class="normal">564</span>
<span class="normal">565</span>
<span class="normal">566</span>
<span class="normal">567</span>
<span class="normal">568</span>
<span class="normal">569</span>
<span class="normal">570</span>
<span class="normal">571</span>
<span class="normal">572</span>
<span class="normal">573</span>
<span class="normal">574</span>
<span class="normal">575</span>
<span class="normal">576</span>
<span class="normal">577</span>
<span class="normal">578</span>
<span class="normal">579</span>
<span class="normal">580</span>
<span class="normal">581</span>
<span class="normal">582</span>
<span class="normal">583</span>
<span class="normal">584</span>
<span class="normal">585</span>
<span class="normal">586</span>
<span class="normal">587</span>
<span class="normal">588</span>
<span class="normal">589</span>
<span class="normal">590</span>
<span class="normal">591</span>
<span class="normal">592</span>
<span class="normal">593</span>
<span class="normal">594</span>
<span class="normal">595</span>
<span class="normal">596</span>
<span class="normal">597</span>
<span class="normal">598</span>
<span class="normal">599</span>
<span class="normal">600</span>
<span class="normal">601</span>
<span class="normal">602</span>
<span class="normal">603</span>
<span class="normal">604</span>
<span class="normal">605</span>
<span class="normal">606</span>
<span class="normal">607</span>
<span class="normal">608</span>
<span class="normal">609</span>
<span class="normal">610</span>
<span class="normal">611</span>
<span class="normal">612</span>
<span class="normal">613</span>
<span class="normal">614</span>
<span class="normal">615</span>
<span class="normal">616</span>
<span class="normal">617</span>
<span class="normal">618</span>
<span class="normal">619</span>
<span class="normal">620</span>
<span class="normal">621</span>
<span class="normal">622</span>
<span class="normal">623</span>
<span class="normal">624</span>
<span class="normal">625</span>
<span class="normal">626</span>
<span class="normal">627</span>
<span class="normal">628</span>
<span class="normal">629</span>
<span class="normal">630</span>
<span class="normal">631</span>
<span class="normal">632</span>
<span class="normal">633</span>
<span class="normal">634</span>
<span class="normal">635</span>
<span class="normal">636</span>
<span class="normal">637</span>
<span class="normal">638</span>
<span class="normal">639</span>
<span class="normal">640</span>
<span class="normal">641</span>
<span class="normal">642</span>
<span class="normal">643</span>
<span class="normal">644</span>
<span class="normal">645</span>
<span class="normal">646</span>
<span class="normal">647</span>
<span class="normal">648</span>
<span class="normal">649</span>
<span class="normal">650</span>
<span class="normal">651</span>
<span class="normal">652</span>
<span class="normal">653</span></pre></div></td><td class="code"><div><pre id="__code_84"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_84 > code"></button><code tabindex="0"><span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">ToolCallPartDelta</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""A partial update (delta) for a `ToolCallPart` to modify tool name, arguments, or tool call ID."""</span>

    <span class="n">tool_name_delta</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="w">    </span><span class="sd">"""Incremental text to add to the existing tool name, if any."""</span>

    <span class="n">args_delta</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="w">    </span><span class="sd">"""Incremental data to add to the tool arguments.</span>

<span class="sd">    If this is a string, it will be appended to existing JSON arguments.</span>
<span class="sd">    If this is a dict, it will be merged with existing dict arguments.</span>
<span class="sd">    """</span>

    <span class="n">tool_call_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="w">    </span><span class="sd">"""Optional tool call identifier, this is used by some models including OpenAI.</span>

<span class="sd">    Note this is never treated as a delta — it can replace None, but otherwise if a</span>
<span class="sd">    non-matching value is provided an error will be raised."""</span>

    <span class="n">part_delta_kind</span><span class="p">:</span> <span class="n">Literal</span><span class="p">[</span><span class="s1">'tool_call'</span><span class="p">]</span> <span class="o">=</span> <span class="s1">'tool_call'</span>
<span class="w">    </span><span class="sd">"""Part delta type identifier, used as a discriminator."""</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">as_part</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ToolCallPart</span> <span class="o">|</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Convert this delta to a fully formed `ToolCallPart` if possible, otherwise return `None`.</span>

<span class="sd">        Returns:</span>
<span class="sd">            A `ToolCallPart` if both `tool_name_delta` and `args_delta` are set, otherwise `None`.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">tool_name_delta</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">args_delta</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">return</span> <span class="kc">None</span>

        <span class="k">return</span> <span class="n">ToolCallPart</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">tool_name_delta</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">args_delta</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">tool_call_id</span> <span class="ow">or</span> <span class="n">_generate_tool_call_id</span><span class="p">())</span>

    <span class="nd">@overload</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">apply</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">part</span><span class="p">:</span> <span class="n">ModelResponsePart</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ToolCallPart</span><span class="p">:</span> <span class="o">...</span>

    <span class="nd">@overload</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">apply</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">part</span><span class="p">:</span> <span class="n">ModelResponsePart</span> <span class="o">|</span> <span class="n">ToolCallPartDelta</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ToolCallPart</span> <span class="o">|</span> <span class="n">ToolCallPartDelta</span><span class="p">:</span> <span class="o">...</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">apply</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">part</span><span class="p">:</span> <span class="n">ModelResponsePart</span> <span class="o">|</span> <span class="n">ToolCallPartDelta</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ToolCallPart</span> <span class="o">|</span> <span class="n">ToolCallPartDelta</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Apply this delta to a part or delta, returning a new part or delta with the changes applied.</span>

<span class="sd">        Args:</span>
<span class="sd">            part: The existing model response part or delta to update.</span>

<span class="sd">        Returns:</span>
<span class="sd">            Either a new `ToolCallPart` or an updated `ToolCallPartDelta`.</span>

<span class="sd">        Raises:</span>
<span class="sd">            ValueError: If `part` is neither a `ToolCallPart` nor a `ToolCallPartDelta`.</span>
<span class="sd">            UnexpectedModelBehavior: If applying JSON deltas to dict arguments or vice versa.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">part</span><span class="p">,</span> <span class="n">ToolCallPart</span><span class="p">):</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_apply_to_part</span><span class="p">(</span><span class="n">part</span><span class="p">)</span>

        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">part</span><span class="p">,</span> <span class="n">ToolCallPartDelta</span><span class="p">):</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_apply_to_delta</span><span class="p">(</span><span class="n">part</span><span class="p">)</span>

        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s1">'Can only apply ToolCallPartDeltas to ToolCallParts or ToolCallPartDeltas, not </span><span class="si">{</span><span class="n">part</span><span class="si">}</span><span class="s1">'</span><span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">_apply_to_delta</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">delta</span><span class="p">:</span> <span class="n">ToolCallPartDelta</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ToolCallPart</span> <span class="o">|</span> <span class="n">ToolCallPartDelta</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Internal helper to apply this delta to another delta."""</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">tool_name_delta</span><span class="p">:</span>
            <span class="c1"># Append incremental text to the existing tool_name_delta</span>
            <span class="n">updated_tool_name_delta</span> <span class="o">=</span> <span class="p">(</span><span class="n">delta</span><span class="o">.</span><span class="n">tool_name_delta</span> <span class="ow">or</span> <span class="s1">''</span><span class="p">)</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">tool_name_delta</span>
            <span class="n">delta</span> <span class="o">=</span> <span class="n">replace</span><span class="p">(</span><span class="n">delta</span><span class="p">,</span> <span class="n">tool_name_delta</span><span class="o">=</span><span class="n">updated_tool_name_delta</span><span class="p">)</span>

        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">args_delta</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">delta</span><span class="o">.</span><span class="n">args_delta</span><span class="p">,</span> <span class="nb">dict</span><span class="p">):</span>
                <span class="k">raise</span> <span class="n">UnexpectedModelBehavior</span><span class="p">(</span>
                    <span class="sa">f</span><span class="s1">'Cannot apply JSON deltas to non-JSON tool arguments (</span><span class="si">{</span><span class="n">delta</span><span class="si">=}</span><span class="s1">, </span><span class="si">{</span><span class="bp">self</span><span class="si">=}</span><span class="s1">)'</span>
                <span class="p">)</span>
            <span class="n">updated_args_delta</span> <span class="o">=</span> <span class="p">(</span><span class="n">delta</span><span class="o">.</span><span class="n">args_delta</span> <span class="ow">or</span> <span class="s1">''</span><span class="p">)</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">args_delta</span>
            <span class="n">delta</span> <span class="o">=</span> <span class="n">replace</span><span class="p">(</span><span class="n">delta</span><span class="p">,</span> <span class="n">args_delta</span><span class="o">=</span><span class="n">updated_args_delta</span><span class="p">)</span>
        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">args_delta</span><span class="p">,</span> <span class="nb">dict</span><span class="p">):</span>
            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">delta</span><span class="o">.</span><span class="n">args_delta</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
                <span class="k">raise</span> <span class="n">UnexpectedModelBehavior</span><span class="p">(</span>
                    <span class="sa">f</span><span class="s1">'Cannot apply dict deltas to non-dict tool arguments (</span><span class="si">{</span><span class="n">delta</span><span class="si">=}</span><span class="s1">, </span><span class="si">{</span><span class="bp">self</span><span class="si">=}</span><span class="s1">)'</span>
                <span class="p">)</span>
            <span class="n">updated_args_delta</span> <span class="o">=</span> <span class="p">{</span><span class="o">**</span><span class="p">(</span><span class="n">delta</span><span class="o">.</span><span class="n">args_delta</span> <span class="ow">or</span> <span class="p">{}),</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">args_delta</span><span class="p">}</span>
            <span class="n">delta</span> <span class="o">=</span> <span class="n">replace</span><span class="p">(</span><span class="n">delta</span><span class="p">,</span> <span class="n">args_delta</span><span class="o">=</span><span class="n">updated_args_delta</span><span class="p">)</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">tool_call_id</span><span class="p">:</span>
            <span class="n">delta</span> <span class="o">=</span> <span class="n">replace</span><span class="p">(</span><span class="n">delta</span><span class="p">,</span> <span class="n">tool_call_id</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">tool_call_id</span><span class="p">)</span>

        <span class="c1"># If we now have enough data to create a full ToolCallPart, do so</span>
        <span class="k">if</span> <span class="n">delta</span><span class="o">.</span><span class="n">tool_name_delta</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">delta</span><span class="o">.</span><span class="n">args_delta</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">ToolCallPart</span><span class="p">(</span><span class="n">delta</span><span class="o">.</span><span class="n">tool_name_delta</span><span class="p">,</span> <span class="n">delta</span><span class="o">.</span><span class="n">args_delta</span><span class="p">,</span> <span class="n">delta</span><span class="o">.</span><span class="n">tool_call_id</span> <span class="ow">or</span> <span class="n">_generate_tool_call_id</span><span class="p">())</span>

        <span class="k">return</span> <span class="n">delta</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">_apply_to_part</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">part</span><span class="p">:</span> <span class="n">ToolCallPart</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ToolCallPart</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Internal helper to apply this delta directly to a `ToolCallPart`."""</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">tool_name_delta</span><span class="p">:</span>
            <span class="c1"># Append incremental text to the existing tool_name</span>
            <span class="n">tool_name</span> <span class="o">=</span> <span class="n">part</span><span class="o">.</span><span class="n">tool_name</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">tool_name_delta</span>
            <span class="n">part</span> <span class="o">=</span> <span class="n">replace</span><span class="p">(</span><span class="n">part</span><span class="p">,</span> <span class="n">tool_name</span><span class="o">=</span><span class="n">tool_name</span><span class="p">)</span>

        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">args_delta</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">part</span><span class="o">.</span><span class="n">args</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
                <span class="k">raise</span> <span class="n">UnexpectedModelBehavior</span><span class="p">(</span><span class="sa">f</span><span class="s1">'Cannot apply JSON deltas to non-JSON tool arguments (</span><span class="si">{</span><span class="n">part</span><span class="si">=}</span><span class="s1">, </span><span class="si">{</span><span class="bp">self</span><span class="si">=}</span><span class="s1">)'</span><span class="p">)</span>
            <span class="n">updated_json</span> <span class="o">=</span> <span class="n">part</span><span class="o">.</span><span class="n">args</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">args_delta</span>
            <span class="n">part</span> <span class="o">=</span> <span class="n">replace</span><span class="p">(</span><span class="n">part</span><span class="p">,</span> <span class="n">args</span><span class="o">=</span><span class="n">updated_json</span><span class="p">)</span>
        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">args_delta</span><span class="p">,</span> <span class="nb">dict</span><span class="p">):</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">part</span><span class="o">.</span><span class="n">args</span><span class="p">,</span> <span class="nb">dict</span><span class="p">):</span>
                <span class="k">raise</span> <span class="n">UnexpectedModelBehavior</span><span class="p">(</span><span class="sa">f</span><span class="s1">'Cannot apply dict deltas to non-dict tool arguments (</span><span class="si">{</span><span class="n">part</span><span class="si">=}</span><span class="s1">, </span><span class="si">{</span><span class="bp">self</span><span class="si">=}</span><span class="s1">)'</span><span class="p">)</span>
            <span class="n">updated_dict</span> <span class="o">=</span> <span class="p">{</span><span class="o">**</span><span class="p">(</span><span class="n">part</span><span class="o">.</span><span class="n">args</span> <span class="ow">or</span> <span class="p">{}),</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">args_delta</span><span class="p">}</span>
            <span class="n">part</span> <span class="o">=</span> <span class="n">replace</span><span class="p">(</span><span class="n">part</span><span class="p">,</span> <span class="n">args</span><span class="o">=</span><span class="n">updated_dict</span><span class="p">)</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">tool_call_id</span><span class="p">:</span>
            <span class="n">part</span> <span class="o">=</span> <span class="n">replace</span><span class="p">(</span><span class="n">part</span><span class="p">,</span> <span class="n">tool_call_id</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">tool_call_id</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">part</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.ToolCallPartDelta.tool_name_delta" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">tool_name_delta</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_85"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_85 > code"></button><code><span class="n">tool_name_delta</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Incremental text to add to the existing tool name, if any.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.ToolCallPartDelta.args_delta" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">args_delta</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_86"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_86 > code"></button><code><span class="n">args_delta</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict">dict</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Incremental data to add to the tool arguments.</p>
<p>If this is a string, it will be appended to existing JSON arguments.
If this is a dict, it will be merged with existing dict arguments.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.ToolCallPartDelta.tool_call_id" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">tool_call_id</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_87"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_87 > code"></button><code><span class="n">tool_call_id</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Optional tool call identifier, this is used by some models including OpenAI.</p>
<p>Note this is never treated as a delta — it can replace None, but otherwise if a
non-matching value is provided an error will be raised.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.ToolCallPartDelta.part_delta_kind" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">part_delta_kind</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_88"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_88 > code"></button><code><span class="n">part_delta_kind</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Literal" href="https://docs.python.org/3/library/typing.html#typing.Literal">Literal</a></span><span class="p">[</span><span class="s1">'tool_call'</span><span class="p">]</span> <span class="o">=</span> <span class="s1">'tool_call'</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Part delta type identifier, used as a discriminator.</p>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.messages.ToolCallPartDelta.as_part" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">as_part</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_89"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_89 > code"></button><code><span class="nf">as_part</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ToolCallPart" href="#pydantic_ai.messages.ToolCallPart">ToolCallPart</a></span> <span class="o">|</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Convert this delta to a fully formed <code>ToolCallPart</code> if possible, otherwise return <code>None</code>.</p>


    <p><span class="doc-section-title">Returns:</span></p>
    <div class="md-typeset__scrollwrap"><div class="md-typeset__table"><table>
      <thead>
        <tr>
          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ToolCallPart" href="#pydantic_ai.messages.ToolCallPart">ToolCallPart</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>A <code>ToolCallPart</code> if both <code>tool_name_delta</code> and <code>args_delta</code> are set, otherwise <code>None</code>.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/messages.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">564</span>
<span class="normal">565</span>
<span class="normal">566</span>
<span class="normal">567</span>
<span class="normal">568</span>
<span class="normal">569</span>
<span class="normal">570</span>
<span class="normal">571</span>
<span class="normal">572</span>
<span class="normal">573</span></pre></div></td><td class="code"><div><pre id="__code_90"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_90 > code"></button><code><span class="k">def</span><span class="w"> </span><span class="nf">as_part</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ToolCallPart</span> <span class="o">|</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Convert this delta to a fully formed `ToolCallPart` if possible, otherwise return `None`.</span>

<span class="sd">    Returns:</span>
<span class="sd">        A `ToolCallPart` if both `tool_name_delta` and `args_delta` are set, otherwise `None`.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">tool_name_delta</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">args_delta</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">return</span> <span class="kc">None</span>

    <span class="k">return</span> <span class="n">ToolCallPart</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">tool_name_delta</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">args_delta</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">tool_call_id</span> <span class="ow">or</span> <span class="n">_generate_tool_call_id</span><span class="p">())</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.messages.ToolCallPartDelta.apply" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">apply</span>


</h4>
          <div class="doc-overloads">
<div class="language-python doc-signature highlight"><pre id="__code_91"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_91 > code"></button><code><span class="nf">apply</span><span class="p">(</span><span class="n">part</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ModelResponsePart" href="#pydantic_ai.messages.ModelResponsePart">ModelResponsePart</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ToolCallPart" href="#pydantic_ai.messages.ToolCallPart">ToolCallPart</a></span>
</code></pre></div><div class="language-python doc-signature highlight"><pre id="__code_92"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_92 > code"></button><code><span class="nf">apply</span><span class="p">(</span>
    <span class="n">part</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ModelResponsePart" href="#pydantic_ai.messages.ModelResponsePart">ModelResponsePart</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ToolCallPartDelta" href="#pydantic_ai.messages.ToolCallPartDelta">ToolCallPartDelta</a></span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ToolCallPart" href="#pydantic_ai.messages.ToolCallPart">ToolCallPart</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ToolCallPartDelta" href="#pydantic_ai.messages.ToolCallPartDelta">ToolCallPartDelta</a></span>
</code></pre></div>          </div>
<div class="language-python doc-signature highlight"><pre id="__code_93"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_93 > code"></button><code><span class="nf">apply</span><span class="p">(</span>
    <span class="n">part</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ModelResponsePart" href="#pydantic_ai.messages.ModelResponsePart">ModelResponsePart</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ToolCallPartDelta" href="#pydantic_ai.messages.ToolCallPartDelta">ToolCallPartDelta</a></span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ToolCallPart" href="#pydantic_ai.messages.ToolCallPart">ToolCallPart</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ToolCallPartDelta" href="#pydantic_ai.messages.ToolCallPartDelta">ToolCallPartDelta</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Apply this delta to a part or delta, returning a new part or delta with the changes applied.</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <div class="md-typeset__scrollwrap"><div class="md-typeset__table"><table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>part</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ModelResponsePart" href="#pydantic_ai.messages.ModelResponsePart">ModelResponsePart</a> | <a class="autorefs autorefs-internal" title="pydantic_ai.messages.ToolCallPartDelta" href="#pydantic_ai.messages.ToolCallPartDelta">ToolCallPartDelta</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The existing model response part or delta to update.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
      </tbody>
    </table></div></div>


    <p><span class="doc-section-title">Returns:</span></p>
    <div class="md-typeset__scrollwrap"><div class="md-typeset__table"><table>
      <thead>
        <tr>
          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ToolCallPart" href="#pydantic_ai.messages.ToolCallPart">ToolCallPart</a> | <a class="autorefs autorefs-internal" title="pydantic_ai.messages.ToolCallPartDelta" href="#pydantic_ai.messages.ToolCallPartDelta">ToolCallPartDelta</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Either a new <code>ToolCallPart</code> or an updated <code>ToolCallPartDelta</code>.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table></div></div>


<p><span class="doc-section-title">Raises:</span></p>
    <div class="md-typeset__scrollwrap"><div class="md-typeset__table"><table>
      <thead>
        <tr>
          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/exceptions.html#ValueError">ValueError</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>If <code>part</code> is neither a <code>ToolCallPart</code> nor a <code>ToolCallPartDelta</code>.</p>
              </div>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_ai.exceptions.UnexpectedModelBehavior" href="../exceptions/#pydantic_ai.exceptions.UnexpectedModelBehavior">UnexpectedModelBehavior</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>If applying JSON deltas to dict arguments or vice versa.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/messages.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">581</span>
<span class="normal">582</span>
<span class="normal">583</span>
<span class="normal">584</span>
<span class="normal">585</span>
<span class="normal">586</span>
<span class="normal">587</span>
<span class="normal">588</span>
<span class="normal">589</span>
<span class="normal">590</span>
<span class="normal">591</span>
<span class="normal">592</span>
<span class="normal">593</span>
<span class="normal">594</span>
<span class="normal">595</span>
<span class="normal">596</span>
<span class="normal">597</span>
<span class="normal">598</span>
<span class="normal">599</span>
<span class="normal">600</span></pre></div></td><td class="code"><div><pre id="__code_94"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_94 > code"></button><code><span class="k">def</span><span class="w"> </span><span class="nf">apply</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">part</span><span class="p">:</span> <span class="n">ModelResponsePart</span> <span class="o">|</span> <span class="n">ToolCallPartDelta</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ToolCallPart</span> <span class="o">|</span> <span class="n">ToolCallPartDelta</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Apply this delta to a part or delta, returning a new part or delta with the changes applied.</span>

<span class="sd">    Args:</span>
<span class="sd">        part: The existing model response part or delta to update.</span>

<span class="sd">    Returns:</span>
<span class="sd">        Either a new `ToolCallPart` or an updated `ToolCallPartDelta`.</span>

<span class="sd">    Raises:</span>
<span class="sd">        ValueError: If `part` is neither a `ToolCallPart` nor a `ToolCallPartDelta`.</span>
<span class="sd">        UnexpectedModelBehavior: If applying JSON deltas to dict arguments or vice versa.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">part</span><span class="p">,</span> <span class="n">ToolCallPart</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_apply_to_part</span><span class="p">(</span><span class="n">part</span><span class="p">)</span>

    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">part</span><span class="p">,</span> <span class="n">ToolCallPartDelta</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_apply_to_delta</span><span class="p">(</span><span class="n">part</span><span class="p">)</span>

    <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s1">'Can only apply ToolCallPartDeltas to ToolCallParts or ToolCallPartDeltas, not </span><span class="si">{</span><span class="n">part</span><span class="si">}</span><span class="s1">'</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>












  </div>

    </div>

</div>






<div class="doc doc-object doc-attribute">



<h3 id="pydantic_ai.messages.ModelResponsePartDelta" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">ModelResponsePartDelta</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span>

</h3>
<div class="language-python doc-signature highlight"><pre id="__code_95"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_95 > code"></button><code><span class="n">ModelResponsePartDelta</span> <span class="o">=</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Annotated" href="https://docs.python.org/3/library/typing.html#typing.Annotated">Annotated</a></span><span class="p">[</span>
    <span class="n"><a class="autorefs autorefs-external" title="typing.Union" href="https://docs.python.org/3/library/typing.html#typing.Union">Union</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.TextPartDelta" href="#pydantic_ai.messages.TextPartDelta">TextPartDelta</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ToolCallPartDelta" href="#pydantic_ai.messages.ToolCallPartDelta">ToolCallPartDelta</a></span><span class="p">],</span>
    <span class="n"><a class="autorefs autorefs-external" title="pydantic.Discriminator" href="https://docs.pydantic.dev/latest/api/types/#pydantic.types.Discriminator">Discriminator</a></span><span class="p">(</span><span class="s2">"part_delta_kind"</span><span class="p">),</span>
<span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>A partial update (delta) for any model response part.</p>
    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_ai.messages.PartStartEvent" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">PartStartEvent</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">


        <p>An event indicating that a new part has started.</p>
<p>If multiple <code>PartStartEvent</code>s are received with the same index,
the new one should fully replace the old one.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/messages.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">660</span>
<span class="normal">661</span>
<span class="normal">662</span>
<span class="normal">663</span>
<span class="normal">664</span>
<span class="normal">665</span>
<span class="normal">666</span>
<span class="normal">667</span>
<span class="normal">668</span>
<span class="normal">669</span>
<span class="normal">670</span>
<span class="normal">671</span>
<span class="normal">672</span>
<span class="normal">673</span>
<span class="normal">674</span>
<span class="normal">675</span></pre></div></td><td class="code"><div><pre id="__code_96"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_96 > code"></button><code><span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">PartStartEvent</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""An event indicating that a new part has started.</span>

<span class="sd">    If multiple `PartStartEvent`s are received with the same index,</span>
<span class="sd">    the new one should fully replace the old one.</span>
<span class="sd">    """</span>

    <span class="n">index</span><span class="p">:</span> <span class="nb">int</span>
<span class="w">    </span><span class="sd">"""The index of the part within the overall response parts list."""</span>

    <span class="n">part</span><span class="p">:</span> <span class="n">ModelResponsePart</span>
<span class="w">    </span><span class="sd">"""The newly started `ModelResponsePart`."""</span>

    <span class="n">event_kind</span><span class="p">:</span> <span class="n">Literal</span><span class="p">[</span><span class="s1">'part_start'</span><span class="p">]</span> <span class="o">=</span> <span class="s1">'part_start'</span>
<span class="w">    </span><span class="sd">"""Event type identifier, used as a discriminator."""</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.PartStartEvent.index" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">index</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_97"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_97 > code"></button><code><span class="n">index</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#int">int</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The index of the part within the overall response parts list.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.PartStartEvent.part" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">part</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_98"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_98 > code"></button><code><span class="n">part</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ModelResponsePart" href="#pydantic_ai.messages.ModelResponsePart">ModelResponsePart</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The newly started <code>ModelResponsePart</code>.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.PartStartEvent.event_kind" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">event_kind</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_99"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_99 > code"></button><code><span class="n">event_kind</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Literal" href="https://docs.python.org/3/library/typing.html#typing.Literal">Literal</a></span><span class="p">[</span><span class="s1">'part_start'</span><span class="p">]</span> <span class="o">=</span> <span class="s1">'part_start'</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Event type identifier, used as a discriminator.</p>
    </div>

</div>




  </div>

    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_ai.messages.PartDeltaEvent" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">PartDeltaEvent</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">


        <p>An event indicating a delta update for an existing part.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/messages.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">678</span>
<span class="normal">679</span>
<span class="normal">680</span>
<span class="normal">681</span>
<span class="normal">682</span>
<span class="normal">683</span>
<span class="normal">684</span>
<span class="normal">685</span>
<span class="normal">686</span>
<span class="normal">687</span>
<span class="normal">688</span>
<span class="normal">689</span></pre></div></td><td class="code"><div><pre id="__code_100"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_100 > code"></button><code><span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">PartDeltaEvent</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""An event indicating a delta update for an existing part."""</span>

    <span class="n">index</span><span class="p">:</span> <span class="nb">int</span>
<span class="w">    </span><span class="sd">"""The index of the part within the overall response parts list."""</span>

    <span class="n">delta</span><span class="p">:</span> <span class="n">ModelResponsePartDelta</span>
<span class="w">    </span><span class="sd">"""The delta to apply to the specified part."""</span>

    <span class="n">event_kind</span><span class="p">:</span> <span class="n">Literal</span><span class="p">[</span><span class="s1">'part_delta'</span><span class="p">]</span> <span class="o">=</span> <span class="s1">'part_delta'</span>
<span class="w">    </span><span class="sd">"""Event type identifier, used as a discriminator."""</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.PartDeltaEvent.index" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">index</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_101"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_101 > code"></button><code><span class="n">index</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#int">int</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The index of the part within the overall response parts list.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.PartDeltaEvent.delta" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">delta</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_102"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_102 > code"></button><code><span class="n">delta</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ModelResponsePartDelta" href="#pydantic_ai.messages.ModelResponsePartDelta">ModelResponsePartDelta</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The delta to apply to the specified part.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.PartDeltaEvent.event_kind" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">event_kind</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_103"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_103 > code"></button><code><span class="n">event_kind</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Literal" href="https://docs.python.org/3/library/typing.html#typing.Literal">Literal</a></span><span class="p">[</span><span class="s1">'part_delta'</span><span class="p">]</span> <span class="o">=</span> <span class="s1">'part_delta'</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Event type identifier, used as a discriminator.</p>
    </div>

</div>




  </div>

    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_ai.messages.FinalResultEvent" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">FinalResultEvent</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">


        <p>An event indicating the response to the current model request matches the result schema.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/messages.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">692</span>
<span class="normal">693</span>
<span class="normal">694</span>
<span class="normal">695</span>
<span class="normal">696</span>
<span class="normal">697</span>
<span class="normal">698</span>
<span class="normal">699</span>
<span class="normal">700</span>
<span class="normal">701</span></pre></div></td><td class="code"><div><pre id="__code_104"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_104 > code"></button><code tabindex="0"><span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">FinalResultEvent</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""An event indicating the response to the current model request matches the result schema."""</span>

    <span class="n">tool_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span>
<span class="w">    </span><span class="sd">"""The name of the result tool that was called. `None` if the result is from text content and not from a tool."""</span>
    <span class="n">tool_call_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span>
<span class="w">    </span><span class="sd">"""The tool call ID, if any, that this result is associated with."""</span>
    <span class="n">event_kind</span><span class="p">:</span> <span class="n">Literal</span><span class="p">[</span><span class="s1">'final_result'</span><span class="p">]</span> <span class="o">=</span> <span class="s1">'final_result'</span>
<span class="w">    </span><span class="sd">"""Event type identifier, used as a discriminator."""</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.FinalResultEvent.tool_name" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">tool_name</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_105"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_105 > code"></button><code><span class="n">tool_name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The name of the result tool that was called. <code>None</code> if the result is from text content and not from a tool.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.FinalResultEvent.tool_call_id" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">tool_call_id</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_106"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_106 > code"></button><code><span class="n">tool_call_id</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The tool call ID, if any, that this result is associated with.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.FinalResultEvent.event_kind" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">event_kind</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_107"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_107 > code"></button><code><span class="n">event_kind</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Literal" href="https://docs.python.org/3/library/typing.html#typing.Literal">Literal</a></span><span class="p">[</span><span class="s1">'final_result'</span><span class="p">]</span> <span class="o">=</span> <span class="s1">'final_result'</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Event type identifier, used as a discriminator.</p>
    </div>

</div>




  </div>

    </div>

</div>






<div class="doc doc-object doc-attribute">



<h3 id="pydantic_ai.messages.ModelResponseStreamEvent" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">ModelResponseStreamEvent</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span>

</h3>
<div class="language-python doc-signature highlight"><pre id="__code_108"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_108 > code"></button><code><span class="n">ModelResponseStreamEvent</span> <span class="o">=</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Annotated" href="https://docs.python.org/3/library/typing.html#typing.Annotated">Annotated</a></span><span class="p">[</span>
    <span class="n"><a class="autorefs autorefs-external" title="typing.Union" href="https://docs.python.org/3/library/typing.html#typing.Union">Union</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.PartStartEvent" href="#pydantic_ai.messages.PartStartEvent">PartStartEvent</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.PartDeltaEvent" href="#pydantic_ai.messages.PartDeltaEvent">PartDeltaEvent</a></span><span class="p">],</span>
    <span class="n"><a class="autorefs autorefs-external" title="pydantic.Discriminator" href="https://docs.pydantic.dev/latest/api/types/#pydantic.types.Discriminator">Discriminator</a></span><span class="p">(</span><span class="s2">"event_kind"</span><span class="p">),</span>
<span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>An event in the model response stream, either starting a new part or applying a delta to an existing one.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h3 id="pydantic_ai.messages.AgentStreamEvent" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">AgentStreamEvent</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span>

</h3>
<div class="language-python doc-signature highlight"><pre id="__code_109"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_109 > code"></button><code><span class="n">AgentStreamEvent</span> <span class="o">=</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Annotated" href="https://docs.python.org/3/library/typing.html#typing.Annotated">Annotated</a></span><span class="p">[</span>
    <span class="n"><a class="autorefs autorefs-external" title="typing.Union" href="https://docs.python.org/3/library/typing.html#typing.Union">Union</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.PartStartEvent" href="#pydantic_ai.messages.PartStartEvent">PartStartEvent</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.PartDeltaEvent" href="#pydantic_ai.messages.PartDeltaEvent">PartDeltaEvent</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.FinalResultEvent" href="#pydantic_ai.messages.FinalResultEvent">FinalResultEvent</a></span><span class="p">],</span>
    <span class="n"><a class="autorefs autorefs-external" title="pydantic.Discriminator" href="https://docs.pydantic.dev/latest/api/types/#pydantic.types.Discriminator">Discriminator</a></span><span class="p">(</span><span class="s2">"event_kind"</span><span class="p">),</span>
<span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>An event in the agent stream.</p>
    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_ai.messages.FunctionToolCallEvent" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">FunctionToolCallEvent</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">


        <p>An event indicating the start to a call to a function tool.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/messages.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">713</span>
<span class="normal">714</span>
<span class="normal">715</span>
<span class="normal">716</span>
<span class="normal">717</span>
<span class="normal">718</span>
<span class="normal">719</span>
<span class="normal">720</span>
<span class="normal">721</span>
<span class="normal">722</span>
<span class="normal">723</span>
<span class="normal">724</span>
<span class="normal">725</span></pre></div></td><td class="code"><div><pre id="__code_110"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_110 > code"></button><code tabindex="0"><span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">FunctionToolCallEvent</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""An event indicating the start to a call to a function tool."""</span>

    <span class="n">part</span><span class="p">:</span> <span class="n">ToolCallPart</span>
<span class="w">    </span><span class="sd">"""The (function) tool call to make."""</span>
    <span class="n">call_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span><span class="n">init</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
<span class="w">    </span><span class="sd">"""An ID used for matching details about the call to its result. If present, defaults to the part's tool_call_id."""</span>
    <span class="n">event_kind</span><span class="p">:</span> <span class="n">Literal</span><span class="p">[</span><span class="s1">'function_tool_call'</span><span class="p">]</span> <span class="o">=</span> <span class="s1">'function_tool_call'</span>
<span class="w">    </span><span class="sd">"""Event type identifier, used as a discriminator."""</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">__post_init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">call_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">part</span><span class="o">.</span><span class="n">tool_call_id</span> <span class="ow">or</span> <span class="nb">str</span><span class="p">(</span><span class="n">uuid</span><span class="o">.</span><span class="n">uuid4</span><span class="p">())</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.FunctionToolCallEvent.part" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">part</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_111"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_111 > code"></button><code><span class="n">part</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ToolCallPart" href="#pydantic_ai.messages.ToolCallPart">ToolCallPart</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The (function) tool call to make.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.FunctionToolCallEvent.call_id" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">call_id</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_112"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_112 > code"></button><code><span class="n">call_id</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">=</span> <span class="n"><a class="autorefs autorefs-external" title="dataclasses.field" href="https://docs.python.org/3/library/dataclasses.html#dataclasses.field">field</a></span><span class="p">(</span><span class="n"><span title="dataclasses.field(init)">init</span></span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>An ID used for matching details about the call to its result. If present, defaults to the part's tool_call_id.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.FunctionToolCallEvent.event_kind" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">event_kind</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_113"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_113 > code"></button><code><span class="n">event_kind</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Literal" href="https://docs.python.org/3/library/typing.html#typing.Literal">Literal</a></span><span class="p">[</span><span class="s2">"function_tool_call"</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span>
    <span class="s2">"function_tool_call"</span>
<span class="p">)</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Event type identifier, used as a discriminator.</p>
    </div>

</div>




  </div>

    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_ai.messages.FunctionToolResultEvent" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">FunctionToolResultEvent</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">


        <p>An event indicating the result of a function tool call.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/messages.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">728</span>
<span class="normal">729</span>
<span class="normal">730</span>
<span class="normal">731</span>
<span class="normal">732</span>
<span class="normal">733</span>
<span class="normal">734</span>
<span class="normal">735</span>
<span class="normal">736</span>
<span class="normal">737</span></pre></div></td><td class="code"><div><pre id="__code_114"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_114 > code"></button><code><span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">FunctionToolResultEvent</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""An event indicating the result of a function tool call."""</span>

    <span class="n">result</span><span class="p">:</span> <span class="n">ToolReturnPart</span> <span class="o">|</span> <span class="n">RetryPromptPart</span>
<span class="w">    </span><span class="sd">"""The result of the call to the function tool."""</span>
    <span class="n">tool_call_id</span><span class="p">:</span> <span class="nb">str</span>
<span class="w">    </span><span class="sd">"""An ID used to match the result to its original call."""</span>
    <span class="n">event_kind</span><span class="p">:</span> <span class="n">Literal</span><span class="p">[</span><span class="s1">'function_tool_result'</span><span class="p">]</span> <span class="o">=</span> <span class="s1">'function_tool_result'</span>
<span class="w">    </span><span class="sd">"""Event type identifier, used as a discriminator."""</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.FunctionToolResultEvent.result" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">result</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_115"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_115 > code"></button><code><span class="n">result</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ToolReturnPart" href="#pydantic_ai.messages.ToolReturnPart">ToolReturnPart</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.RetryPromptPart" href="#pydantic_ai.messages.RetryPromptPart">RetryPromptPart</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The result of the call to the function tool.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.FunctionToolResultEvent.tool_call_id" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">tool_call_id</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_116"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_116 > code"></button><code><span class="n">tool_call_id</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>An ID used to match the result to its original call.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.messages.FunctionToolResultEvent.event_kind" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">event_kind</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_117"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_117 > code"></button><code><span class="n">event_kind</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Literal" href="https://docs.python.org/3/library/typing.html#typing.Literal">Literal</a></span><span class="p">[</span><span class="s2">"function_tool_result"</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span>
    <span class="s2">"function_tool_result"</span>
<span class="p">)</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Event type identifier, used as a discriminator.</p>
    </div>

</div>




  </div>

    </div>

</div>




  </div>

    </div>

</div>







  
  






                
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