<!DOCTYPE html><html lang="en" class="js-focus-visible js" data-js-focus-visible=""><head>
    
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width,initial-scale=1">
      
        <meta name="description" content="Agent Framework / shim to use Pydantic with LLMs">
      
      
      
        <link rel="canonical" href="https://ai.pydantic.dev/api/pydantic_graph/persistence/">
      
      
        <link rel="prev" href="../nodes/">
      
      
        <link rel="next" href="../mermaid/">
      
      
      <link rel="icon" href="../../../favicon.ico">
      <meta name="generator" content="mkdocs-1.6.1, mkdocs-material-9.6.5">
    
    
      
        <title>pydantic_graph.persistence - PydanticAI</title>
      
    
    
      <link rel="stylesheet" href="../../../assets/stylesheets/main.8608ea7d.min.css">
      
        
        <link rel="stylesheet" href="../../../assets/stylesheets/palette.06af60db.min.css">
      
      


    
    
      
    
    
      
        
        
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,300i,400,400i,700,700i%7CRoboto+Mono:400,400i,700,700i&amp;display=fallback">
        <style>:root{--md-text-font:"Roboto";--md-code-font:"Roboto Mono"}</style>
      
    
    
      <link rel="stylesheet" href="../../../assets/_mkdocstrings.css">
    
      <link rel="stylesheet" href="../../../extra/tweaks.css">
    
    <script>__md_scope=new URL("../../..",location),__md_hash=e=>[...e].reduce(((e,_)=>(e<<5)-e+_.charCodeAt(0)),0),__md_get=(e,_=localStorage,t=__md_scope)=>JSON.parse(_.getItem(t.pathname+"."+e)),__md_set=(e,_,t=localStorage,a=__md_scope)=>{try{t.setItem(a.pathname+"."+e,JSON.stringify(_))}catch(e){}}</script>
    
      

    
    
      
        <meta property="og:type" content="website">
      
        <meta property="og:title" content="pydantic_graph.persistence - PydanticAI">
      
        <meta property="og:description" content="Agent Framework / shim to use Pydantic with LLMs">
      
        <meta property="og:image" content="https://ai.pydantic.dev/assets/images/social/api/pydantic_graph/persistence.png">
      
        <meta property="og:image:type" content="image/png">
      
        <meta property="og:image:width" content="1200">
      
        <meta property="og:image:height" content="630">
      
        <meta property="og:url" content="https://ai.pydantic.dev/api/pydantic_graph/persistence/">
      
        <meta name="twitter:card" content="summary_large_image">
      
        <meta name="twitter:title" content="pydantic_graph.persistence - PydanticAI">
      
        <meta name="twitter:description" content="Agent Framework / shim to use Pydantic with LLMs">
      
        <meta name="twitter:image" content="https://ai.pydantic.dev/assets/images/social/api/pydantic_graph/persistence.png">
      
    
    
   <link href="../../../assets/stylesheets/glightbox.min.css" rel="stylesheet"><style>
    html.glightbox-open { overflow: initial; height: 100%; }
    .gslide-title { margin-top: 0px; user-select: text; }
    .gslide-desc { color: #666; user-select: text; }
    .gslide-image img { background: white; }
    .gscrollbar-fixer { padding-right: 15px; }
    .gdesc-inner { font-size: 0.75rem; }
    body[data-md-color-scheme="slate"] .gdesc-inner { background: var(--md-default-bg-color);}
    body[data-md-color-scheme="slate"] .gslide-title { color: var(--md-default-fg-color);}
    body[data-md-color-scheme="slate"] .gslide-desc { color: var(--md-default-fg-color);}</style> <script src="../../../assets/javascripts/glightbox.min.js"></script><meta name="theme-color" content="#e92063"><meta name="color-scheme" content="light"></head>
  
  
    
    
      
    
    
    
    
    <body dir="ltr" data-md-color-scheme="default" data-md-color-primary="pink" data-md-color-accent="pink" data-md-color-media="(prefers-color-scheme)">
  
    
    <input class="md-toggle" data-md-toggle="drawer" type="checkbox" id="__drawer" autocomplete="off">
    <input class="md-toggle" data-md-toggle="search" type="checkbox" id="__search" autocomplete="off">
    <label class="md-overlay" for="__drawer"></label>
    <div data-md-component="skip">
      
        
        <a href="#pydantic_graphpersistence" class="md-skip">
          Skip to content
        </a>
      
    </div>
    <div data-md-component="announce">
      
    </div>
    
    
      

  

<header class="md-header md-header--shadow" data-md-component="header">
  <nav class="md-header__inner md-grid" aria-label="Header">
    <a href="../../.." title="PydanticAI" class="md-header__button md-logo" aria-label="PydanticAI" data-md-component="logo">
      
  <img src="../../../img/logo-white.svg" alt="logo">

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
            
              pydantic_graph.persistence
            
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
    <a href="../../.." title="PydanticAI" class="md-nav__button md-logo" aria-label="PydanticAI" data-md-component="logo">
      
  <img src="../../../img/logo-white.svg" alt="logo">

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
      <a href="../../.." class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Introduction
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../install/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Installation
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../help/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Getting Help
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../contributing/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Contributing
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../troubleshooting/" class="md-nav__link">
        
  
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
      <a href="../../../agents/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Agents
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../models/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Models
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../dependencies/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Dependencies
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Function Tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../common-tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Common Tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../results/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Results
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../message-history/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Messages and chat history
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../testing/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Unit testing
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../logfire/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Debugging and Monitoring
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../multi-agent-applications/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Multi-agent Applications
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../graph/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Graphs
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../evals/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Evals
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../input/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Image, Audio &amp; Document Input
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    
    
      
        
          
        
      
        
      
        
      
        
      
    
    
      
    
    
    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_6_14">
        
          
          
          <div class="md-nav__link md-nav__container">
            <a href="../../../mcp/" class="md-nav__link ">
              
  
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
      <a href="../../../mcp/client/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Client
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../mcp/server/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Server
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../mcp/run-python/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    MCP Run Python
    
  </span>
  

      </a>
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../cli/" class="md-nav__link">
        
  
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
            <a href="../../../examples/" class="md-nav__link ">
              
  
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
      <a href="../../../examples/pydantic-model/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Pydantic Model
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../examples/weather-agent/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Weather agent
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../examples/bank-support/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Bank support
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../examples/sql-gen/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    SQL Generation
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../examples/flight-booking/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Flight booking
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../examples/rag/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    RAG
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../examples/stream-markdown/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Stream markdown
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../examples/stream-whales/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Stream whales
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../examples/chat-app/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Chat App with FastAPI
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../examples/question-graph/" class="md-nav__link">
        
  
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
      <a href="../../agent/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.agent
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../common_tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.common_tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../result/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.result
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../messages/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.messages
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../exceptions/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.exceptions
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../settings/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.settings
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../usage/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.usage
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../mcp/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.mcp
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../format_as_xml/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.format_as_xml
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/base/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/openai/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.openai
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/anthropic/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.anthropic
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/bedrock/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.bedrock
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/cohere/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.cohere
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/gemini/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.gemini
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/groq/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.groq
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/instrumented/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.instrumented
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/mistral/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.mistral
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/test/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.test
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/function/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.function
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/fallback/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.fallback
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/wrapper/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.wrapper
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../providers/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.providers
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../graph/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../nodes/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.nodes
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
    
  
  
  
    <li class="md-nav__item md-nav__item--active">
      
      <input class="md-nav__toggle md-toggle" type="checkbox" id="__toc">
      
      
        
      
      
        <label class="md-nav__link md-nav__link--active" for="__toc">
          
  
  <span class="md-ellipsis">
    pydantic_graph.persistence
    
  </span>
  

          <span class="md-nav__icon md-icon"></span>
        </label>
      
      <a href="./" class="md-nav__link md-nav__link--active">
        
  
  <span class="md-ellipsis">
    pydantic_graph.persistence
    
  </span>
  

      </a>
      
        

<nav class="md-nav md-nav--secondary" aria-label="Table of contents">
  
  
  
    
  
  
    <label class="md-nav__title" for="__toc">
      <span class="md-nav__icon md-icon"></span>
      Table of contents
    </label>
    <ul class="md-nav__list" data-md-component="toc">
      
        <li class="md-nav__item">
  <a href="#pydantic_graph.persistence" class="md-nav__link">
    <span class="md-ellipsis">
      persistence
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.SnapshotStatus" class="md-nav__link">
    <span class="md-ellipsis">
      SnapshotStatus
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.NodeSnapshot" class="md-nav__link">
    <span class="md-ellipsis">
      NodeSnapshot
    </span>
  </a>
  
    <nav class="md-nav" aria-label="NodeSnapshot">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.NodeSnapshot.state" class="md-nav__link">
    <span class="md-ellipsis">
      state
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.NodeSnapshot.node" class="md-nav__link">
    <span class="md-ellipsis">
      node
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.NodeSnapshot.start_ts" class="md-nav__link">
    <span class="md-ellipsis">
      start_ts
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.NodeSnapshot.duration" class="md-nav__link">
    <span class="md-ellipsis">
      duration
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.NodeSnapshot.status" class="md-nav__link">
    <span class="md-ellipsis">
      status
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.NodeSnapshot.kind" class="md-nav__link">
    <span class="md-ellipsis">
      kind
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.NodeSnapshot.id" class="md-nav__link">
    <span class="md-ellipsis">
      id
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.EndSnapshot" class="md-nav__link">
    <span class="md-ellipsis">
      EndSnapshot
    </span>
  </a>
  
    <nav class="md-nav" aria-label="EndSnapshot">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.EndSnapshot.state" class="md-nav__link">
    <span class="md-ellipsis">
      state
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.EndSnapshot.result" class="md-nav__link">
    <span class="md-ellipsis">
      result
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.EndSnapshot.ts" class="md-nav__link">
    <span class="md-ellipsis">
      ts
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.EndSnapshot.kind" class="md-nav__link">
    <span class="md-ellipsis">
      kind
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.EndSnapshot.id" class="md-nav__link">
    <span class="md-ellipsis">
      id
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.EndSnapshot.node" class="md-nav__link">
    <span class="md-ellipsis">
      node
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.Snapshot" class="md-nav__link">
    <span class="md-ellipsis">
      Snapshot
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.BaseStatePersistence" class="md-nav__link">
    <span class="md-ellipsis">
      BaseStatePersistence
    </span>
  </a>
  
    <nav class="md-nav" aria-label="BaseStatePersistence">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.BaseStatePersistence.snapshot_node" class="md-nav__link">
    <span class="md-ellipsis">
      snapshot_node
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.BaseStatePersistence.snapshot_node_if_new" class="md-nav__link">
    <span class="md-ellipsis">
      snapshot_node_if_new
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.BaseStatePersistence.snapshot_end" class="md-nav__link">
    <span class="md-ellipsis">
      snapshot_end
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.BaseStatePersistence.record_run" class="md-nav__link">
    <span class="md-ellipsis">
      record_run
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.BaseStatePersistence.load_next" class="md-nav__link">
    <span class="md-ellipsis">
      load_next
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.BaseStatePersistence.load_all" class="md-nav__link">
    <span class="md-ellipsis">
      load_all
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.BaseStatePersistence.set_graph_types" class="md-nav__link">
    <span class="md-ellipsis">
      set_graph_types
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.BaseStatePersistence.should_set_types" class="md-nav__link">
    <span class="md-ellipsis">
      should_set_types
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.BaseStatePersistence.set_types" class="md-nav__link">
    <span class="md-ellipsis">
      set_types
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.build_snapshot_list_type_adapter" class="md-nav__link">
    <span class="md-ellipsis">
      build_snapshot_list_type_adapter
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.in_mem" class="md-nav__link">
    <span class="md-ellipsis">
      in_mem
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.in_mem.SimpleStatePersistence" class="md-nav__link">
    <span class="md-ellipsis">
      SimpleStatePersistence
    </span>
  </a>
  
    <nav class="md-nav" aria-label="SimpleStatePersistence">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.in_mem.SimpleStatePersistence.last_snapshot" class="md-nav__link">
    <span class="md-ellipsis">
      last_snapshot
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.in_mem.FullStatePersistence" class="md-nav__link">
    <span class="md-ellipsis">
      FullStatePersistence
    </span>
  </a>
  
    <nav class="md-nav" aria-label="FullStatePersistence">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.in_mem.FullStatePersistence.deep_copy" class="md-nav__link">
    <span class="md-ellipsis">
      deep_copy
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.in_mem.FullStatePersistence.history" class="md-nav__link">
    <span class="md-ellipsis">
      history
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.in_mem.FullStatePersistence.dump_json" class="md-nav__link">
    <span class="md-ellipsis">
      dump_json
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.in_mem.FullStatePersistence.load_json" class="md-nav__link">
    <span class="md-ellipsis">
      load_json
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.file" class="md-nav__link">
    <span class="md-ellipsis">
      file
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.file.FileStatePersistence" class="md-nav__link">
    <span class="md-ellipsis">
      FileStatePersistence
    </span>
  </a>
  
    <nav class="md-nav" aria-label="FileStatePersistence">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.file.FileStatePersistence.json_file" class="md-nav__link">
    <span class="md-ellipsis">
      json_file
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.file.FileStatePersistence.should_set_types" class="md-nav__link">
    <span class="md-ellipsis">
      should_set_types
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
      <a href="../mermaid/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.mermaid
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../exceptions/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.exceptions
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../pydantic_evals/dataset/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.dataset
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../pydantic_evals/evaluators/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.evaluators
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../pydantic_evals/reporting/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.reporting
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../pydantic_evals/otel/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.otel
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../pydantic_evals/generation/" class="md-nav__link">
        
  
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
  <a href="#pydantic_graph.persistence" class="md-nav__link">
    <span class="md-ellipsis">
      persistence
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.SnapshotStatus" class="md-nav__link">
    <span class="md-ellipsis">
      SnapshotStatus
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.NodeSnapshot" class="md-nav__link">
    <span class="md-ellipsis">
      NodeSnapshot
    </span>
  </a>
  
    <nav class="md-nav" aria-label="NodeSnapshot">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.NodeSnapshot.state" class="md-nav__link">
    <span class="md-ellipsis">
      state
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.NodeSnapshot.node" class="md-nav__link">
    <span class="md-ellipsis">
      node
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.NodeSnapshot.start_ts" class="md-nav__link">
    <span class="md-ellipsis">
      start_ts
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.NodeSnapshot.duration" class="md-nav__link">
    <span class="md-ellipsis">
      duration
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.NodeSnapshot.status" class="md-nav__link">
    <span class="md-ellipsis">
      status
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.NodeSnapshot.kind" class="md-nav__link">
    <span class="md-ellipsis">
      kind
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.NodeSnapshot.id" class="md-nav__link">
    <span class="md-ellipsis">
      id
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.EndSnapshot" class="md-nav__link">
    <span class="md-ellipsis">
      EndSnapshot
    </span>
  </a>
  
    <nav class="md-nav" aria-label="EndSnapshot">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.EndSnapshot.state" class="md-nav__link">
    <span class="md-ellipsis">
      state
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.EndSnapshot.result" class="md-nav__link">
    <span class="md-ellipsis">
      result
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.EndSnapshot.ts" class="md-nav__link">
    <span class="md-ellipsis">
      ts
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.EndSnapshot.kind" class="md-nav__link">
    <span class="md-ellipsis">
      kind
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.EndSnapshot.id" class="md-nav__link">
    <span class="md-ellipsis">
      id
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.EndSnapshot.node" class="md-nav__link">
    <span class="md-ellipsis">
      node
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.Snapshot" class="md-nav__link">
    <span class="md-ellipsis">
      Snapshot
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.BaseStatePersistence" class="md-nav__link">
    <span class="md-ellipsis">
      BaseStatePersistence
    </span>
  </a>
  
    <nav class="md-nav" aria-label="BaseStatePersistence">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.BaseStatePersistence.snapshot_node" class="md-nav__link">
    <span class="md-ellipsis">
      snapshot_node
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.BaseStatePersistence.snapshot_node_if_new" class="md-nav__link">
    <span class="md-ellipsis">
      snapshot_node_if_new
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.BaseStatePersistence.snapshot_end" class="md-nav__link">
    <span class="md-ellipsis">
      snapshot_end
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.BaseStatePersistence.record_run" class="md-nav__link">
    <span class="md-ellipsis">
      record_run
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.BaseStatePersistence.load_next" class="md-nav__link">
    <span class="md-ellipsis">
      load_next
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.BaseStatePersistence.load_all" class="md-nav__link">
    <span class="md-ellipsis">
      load_all
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.BaseStatePersistence.set_graph_types" class="md-nav__link">
    <span class="md-ellipsis">
      set_graph_types
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.BaseStatePersistence.should_set_types" class="md-nav__link">
    <span class="md-ellipsis">
      should_set_types
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.BaseStatePersistence.set_types" class="md-nav__link">
    <span class="md-ellipsis">
      set_types
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.build_snapshot_list_type_adapter" class="md-nav__link">
    <span class="md-ellipsis">
      build_snapshot_list_type_adapter
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.in_mem" class="md-nav__link">
    <span class="md-ellipsis">
      in_mem
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.in_mem.SimpleStatePersistence" class="md-nav__link">
    <span class="md-ellipsis">
      SimpleStatePersistence
    </span>
  </a>
  
    <nav class="md-nav" aria-label="SimpleStatePersistence">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.in_mem.SimpleStatePersistence.last_snapshot" class="md-nav__link">
    <span class="md-ellipsis">
      last_snapshot
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.in_mem.FullStatePersistence" class="md-nav__link">
    <span class="md-ellipsis">
      FullStatePersistence
    </span>
  </a>
  
    <nav class="md-nav" aria-label="FullStatePersistence">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.in_mem.FullStatePersistence.deep_copy" class="md-nav__link">
    <span class="md-ellipsis">
      deep_copy
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.in_mem.FullStatePersistence.history" class="md-nav__link">
    <span class="md-ellipsis">
      history
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.in_mem.FullStatePersistence.dump_json" class="md-nav__link">
    <span class="md-ellipsis">
      dump_json
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.in_mem.FullStatePersistence.load_json" class="md-nav__link">
    <span class="md-ellipsis">
      load_json
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.file" class="md-nav__link">
    <span class="md-ellipsis">
      file
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.file.FileStatePersistence" class="md-nav__link">
    <span class="md-ellipsis">
      FileStatePersistence
    </span>
  </a>
  
    <nav class="md-nav" aria-label="FileStatePersistence">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.file.FileStatePersistence.json_file" class="md-nav__link">
    <span class="md-ellipsis">
      json_file
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.persistence.file.FileStatePersistence.should_set_types" class="md-nav__link">
    <span class="md-ellipsis">
      should_set_types
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
                
                  


  
  


<h1 id="pydantic_graphpersistence"><code>pydantic_graph.persistence</code></h1>


<div class="doc doc-object doc-module">



<a id="pydantic_graph.persistence"></a>
    <div class="doc doc-contents first">








  <div class="doc doc-children">



























<div class="doc doc-object doc-attribute">



<h3 id="pydantic_graph.persistence.SnapshotStatus" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">SnapshotStatus</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span>

</h3>
<div class="language-python doc-signature highlight"><pre id="__code_0"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_0 > code"></button><code><span class="n">SnapshotStatus</span> <span class="o">=</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Literal" href="https://docs.python.org/3/library/typing.html#typing.Literal">Literal</a></span><span class="p">[</span>
    <span class="s2">"created"</span><span class="p">,</span> <span class="s2">"pending"</span><span class="p">,</span> <span class="s2">"running"</span><span class="p">,</span> <span class="s2">"success"</span><span class="p">,</span> <span class="s2">"error"</span>
<span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The status of a snapshot.</p>
<ul>
<li><code>'created'</code>: The snapshot has been created but not yet run.</li>
<li><code>'pending'</code>: The snapshot has been retrieved with
  <a class="autorefs autorefs-internal" href="#pydantic_graph.persistence.BaseStatePersistence.load_next"><code>load_next</code></a> but not yet run.</li>
<li><code>'running'</code>: The snapshot is currently running.</li>
<li><code>'success'</code>: The snapshot has been run successfully.</li>
<li><code>'error'</code>: The snapshot has been run but an error occurred.</li>
</ul>
    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_graph.persistence.NodeSnapshot" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">NodeSnapshot</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">
            <p class="doc doc-class-bases">
              Bases: <code><a class="autorefs autorefs-external" title="typing.Generic" href="https://docs.python.org/3/library/typing.html#typing.Generic">Generic</a>[<span title="pydantic_graph.persistence.StateT">StateT</span>, <span title="pydantic_graph.persistence.RunEndT">RunEndT</span>]</code></p>


        <p>History step describing the execution of a node in a graph.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_graph/pydantic_graph/persistence/__init__.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">44</span>
<span class="normal">45</span>
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
<span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span></pre></div></td><td class="code"><div><pre id="__code_1"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_1 > code"></button><code><span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">NodeSnapshot</span><span class="p">(</span><span class="n">Generic</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""History step describing the execution of a node in a graph."""</span>

    <span class="n">state</span><span class="p">:</span> <span class="n">StateT</span>
<span class="w">    </span><span class="sd">"""The state of the graph before the node is run."""</span>
    <span class="n">node</span><span class="p">:</span> <span class="n">Annotated</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">Any</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">],</span> <span class="n">_utils</span><span class="o">.</span><span class="n">CustomNodeSchema</span><span class="p">()]</span>
<span class="w">    </span><span class="sd">"""The node to run next."""</span>
    <span class="n">start_ts</span><span class="p">:</span> <span class="n">datetime</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="w">    </span><span class="sd">"""The timestamp when the node started running, `None` until the run starts."""</span>
    <span class="n">duration</span><span class="p">:</span> <span class="nb">float</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="w">    </span><span class="sd">"""The duration of the node run in seconds, if the node has been run."""</span>
    <span class="n">status</span><span class="p">:</span> <span class="n">SnapshotStatus</span> <span class="o">=</span> <span class="s1">'created'</span>
<span class="w">    </span><span class="sd">"""The status of the snapshot."""</span>
    <span class="n">kind</span><span class="p">:</span> <span class="n">Literal</span><span class="p">[</span><span class="s1">'node'</span><span class="p">]</span> <span class="o">=</span> <span class="s1">'node'</span>
<span class="w">    </span><span class="sd">"""The kind of history step, can be used as a discriminator when deserializing history."""</span>

    <span class="nb">id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">UNSET_SNAPSHOT_ID</span>
<span class="w">    </span><span class="sd">"""Unique ID of the snapshot."""</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">__post_init__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">id</span> <span class="o">==</span> <span class="n">UNSET_SNAPSHOT_ID</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">get_snapshot_id</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-attribute">



<h4 id="pydantic_graph.persistence.NodeSnapshot.state" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">state</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_2"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_2 > code"></button><code><span class="n">state</span><span class="p">:</span> <span class="n"><span title="pydantic_graph.persistence.StateT">StateT</span></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The state of the graph before the node is run.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_graph.persistence.NodeSnapshot.node" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">node</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_3"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_3 > code"></button><code><span class="n">node</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Annotated" href="https://docs.python.org/3/library/typing.html#typing.Annotated">Annotated</a></span><span class="p">[</span>
    <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.BaseNode" href="../nodes/#pydantic_graph.nodes.BaseNode">BaseNode</a></span><span class="p">[</span><span class="n"><span title="pydantic_graph.persistence.StateT">StateT</span></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a></span><span class="p">,</span> <span class="n"><span title="pydantic_graph.persistence.RunEndT">RunEndT</span></span><span class="p">],</span> <span class="n"><span title="pydantic_graph.persistence._utils.CustomNodeSchema">CustomNodeSchema</span></span><span class="p">()</span>
<span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The node to run next.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_graph.persistence.NodeSnapshot.start_ts" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">start_ts</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_4"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_4 > code"></button><code><span class="n">start_ts</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="datetime.datetime" href="https://docs.python.org/3/library/datetime.html#datetime.datetime">datetime</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The timestamp when the node started running, <code>None</code> until the run starts.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_graph.persistence.NodeSnapshot.duration" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">duration</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_5"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_5 > code"></button><code><span class="n">duration</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#float">float</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The duration of the node run in seconds, if the node has been run.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_graph.persistence.NodeSnapshot.status" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">status</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_6"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_6 > code"></button><code><span class="n">status</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.persistence.SnapshotStatus" href="#pydantic_graph.persistence.SnapshotStatus">SnapshotStatus</a></span> <span class="o">=</span> <span class="s1">'created'</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The status of the snapshot.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_graph.persistence.NodeSnapshot.kind" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">kind</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_7"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_7 > code"></button><code><span class="n">kind</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Literal" href="https://docs.python.org/3/library/typing.html#typing.Literal">Literal</a></span><span class="p">[</span><span class="s1">'node'</span><span class="p">]</span> <span class="o">=</span> <span class="s1">'node'</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The kind of history step, can be used as a discriminator when deserializing history.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_graph.persistence.NodeSnapshot.id" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">id</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_8"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_8 > code"></button><code><span class="nb">id</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">=</span> <span class="n"><span title="pydantic_graph.persistence.UNSET_SNAPSHOT_ID">UNSET_SNAPSHOT_ID</span></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Unique ID of the snapshot.</p>
    </div>

</div>




  </div>

    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_graph.persistence.EndSnapshot" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">EndSnapshot</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">
            <p class="doc doc-class-bases">
              Bases: <code><a class="autorefs autorefs-external" title="typing.Generic" href="https://docs.python.org/3/library/typing.html#typing.Generic">Generic</a>[<span title="pydantic_graph.persistence.StateT">StateT</span>, <span title="pydantic_graph.persistence.RunEndT">RunEndT</span>]</code></p>


        <p>History step describing the end of a graph run.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_graph/pydantic_graph/persistence/__init__.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">69</span>
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
<span class="normal">95</span></pre></div></td><td class="code"><div><pre id="__code_9"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_9 > code"></button><code><span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">EndSnapshot</span><span class="p">(</span><span class="n">Generic</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""History step describing the end of a graph run."""</span>

    <span class="n">state</span><span class="p">:</span> <span class="n">StateT</span>
<span class="w">    </span><span class="sd">"""The state of the graph at the end of the run."""</span>
    <span class="n">result</span><span class="p">:</span> <span class="n">End</span><span class="p">[</span><span class="n">RunEndT</span><span class="p">]</span>
<span class="w">    </span><span class="sd">"""The result of the graph run."""</span>
    <span class="n">ts</span><span class="p">:</span> <span class="n">datetime</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span><span class="n">default_factory</span><span class="o">=</span><span class="n">_utils</span><span class="o">.</span><span class="n">now_utc</span><span class="p">)</span>
<span class="w">    </span><span class="sd">"""The timestamp when the graph run ended."""</span>
    <span class="n">kind</span><span class="p">:</span> <span class="n">Literal</span><span class="p">[</span><span class="s1">'end'</span><span class="p">]</span> <span class="o">=</span> <span class="s1">'end'</span>
<span class="w">    </span><span class="sd">"""The kind of history step, can be used as a discriminator when deserializing history."""</span>

    <span class="nb">id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">UNSET_SNAPSHOT_ID</span>
<span class="w">    </span><span class="sd">"""Unique ID of the snapshot."""</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">__post_init__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">id</span> <span class="o">==</span> <span class="n">UNSET_SNAPSHOT_ID</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">get_snapshot_id</span><span class="p">()</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">node</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">End</span><span class="p">[</span><span class="n">RunEndT</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Shim to get the [`result`][pydantic_graph.persistence.EndSnapshot.result].</span>

<span class="sd">        Useful to allow `[snapshot.node for snapshot in persistence.history]`.</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">result</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-attribute">



<h4 id="pydantic_graph.persistence.EndSnapshot.state" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">state</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_10"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_10 > code"></button><code><span class="n">state</span><span class="p">:</span> <span class="n"><span title="pydantic_graph.persistence.StateT">StateT</span></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The state of the graph at the end of the run.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_graph.persistence.EndSnapshot.result" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">result</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_11"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_11 > code"></button><code><span class="n">result</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.End" href="../nodes/#pydantic_graph.nodes.End">End</a></span><span class="p">[</span><span class="n"><span title="pydantic_graph.persistence.RunEndT">RunEndT</span></span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The result of the graph run.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_graph.persistence.EndSnapshot.ts" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">ts</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_12"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_12 > code"></button><code><span class="n">ts</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="datetime.datetime" href="https://docs.python.org/3/library/datetime.html#datetime.datetime">datetime</a></span> <span class="o">=</span> <span class="n"><a class="autorefs autorefs-external" title="dataclasses.field" href="https://docs.python.org/3/library/dataclasses.html#dataclasses.field">field</a></span><span class="p">(</span><span class="n"><span title="dataclasses.field(default_factory)">default_factory</span></span><span class="o">=</span><span class="n"><span title="pydantic_graph.persistence._utils.now_utc">now_utc</span></span><span class="p">)</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The timestamp when the graph run ended.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_graph.persistence.EndSnapshot.kind" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">kind</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_13"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_13 > code"></button><code><span class="n">kind</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Literal" href="https://docs.python.org/3/library/typing.html#typing.Literal">Literal</a></span><span class="p">[</span><span class="s1">'end'</span><span class="p">]</span> <span class="o">=</span> <span class="s1">'end'</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The kind of history step, can be used as a discriminator when deserializing history.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_graph.persistence.EndSnapshot.id" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">id</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_14"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_14 > code"></button><code><span class="nb">id</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">=</span> <span class="n"><span title="pydantic_graph.persistence.UNSET_SNAPSHOT_ID">UNSET_SNAPSHOT_ID</span></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Unique ID of the snapshot.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_graph.persistence.EndSnapshot.node" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">node</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-property"><code>property</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_15"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_15 > code"></button><code><span class="n">node</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.End" href="../nodes/#pydantic_graph.nodes.End">End</a></span><span class="p">[</span><span class="n"><span title="pydantic_graph.persistence.RunEndT">RunEndT</span></span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Shim to get the <a class="autorefs autorefs-internal" href="#pydantic_graph.persistence.EndSnapshot.result"><code>result</code></a>.</p>
<p>Useful to allow <code>[snapshot.node for snapshot in persistence.history]</code>.</p>
    </div>

</div>




  </div>

    </div>

</div>






<div class="doc doc-object doc-attribute">



<h3 id="pydantic_graph.persistence.Snapshot" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">Snapshot</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span>

</h3>
<div class="language-python doc-signature highlight"><pre id="__code_16"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_16 > code"></button><code><span class="n">Snapshot</span> <span class="o">=</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Union" href="https://docs.python.org/3/library/typing.html#typing.Union">Union</a></span><span class="p">[</span>
    <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.persistence.NodeSnapshot" href="#pydantic_graph.persistence.NodeSnapshot">NodeSnapshot</a></span><span class="p">[</span><span class="n"><span title="pydantic_graph.persistence.StateT">StateT</span></span><span class="p">,</span> <span class="n"><span title="pydantic_graph.persistence.RunEndT">RunEndT</span></span><span class="p">],</span>
    <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.persistence.EndSnapshot" href="#pydantic_graph.persistence.EndSnapshot">EndSnapshot</a></span><span class="p">[</span><span class="n"><span title="pydantic_graph.persistence.StateT">StateT</span></span><span class="p">,</span> <span class="n"><span title="pydantic_graph.persistence.RunEndT">RunEndT</span></span><span class="p">],</span>
<span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>A step in the history of a graph run.</p>
<p><a class="autorefs autorefs-internal" href="../graph/#pydantic_graph.graph.Graph.run"><code>Graph.run</code></a> returns a list of these steps describing the execution of the graph,
together with the run return value.</p>
    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_graph.persistence.BaseStatePersistence" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">BaseStatePersistence</span>


</h3>


    <div class="doc doc-contents ">
            <p class="doc doc-class-bases">
              Bases: <code><a class="autorefs autorefs-external" title="abc.ABC" href="https://docs.python.org/3/library/abc.html#abc.ABC">ABC</a></code>, <code><a class="autorefs autorefs-external" title="typing.Generic" href="https://docs.python.org/3/library/typing.html#typing.Generic">Generic</a>[<span title="pydantic_graph.persistence.StateT">StateT</span>, <span title="pydantic_graph.persistence.RunEndT">RunEndT</span>]</code></p>


        <p>Abstract base class for storing the state of a graph run.</p>
<p>Each instance of a <code>BaseStatePersistence</code> subclass should be used for a single graph run.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_graph/pydantic_graph/persistence/__init__.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">106</span>
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
<span class="normal">123</span>
<span class="normal">124</span>
<span class="normal">125</span>
<span class="normal">126</span>
<span class="normal">127</span>
<span class="normal">128</span>
<span class="normal">129</span>
<span class="normal">130</span>
<span class="normal">131</span>
<span class="normal">132</span>
<span class="normal">133</span>
<span class="normal">134</span>
<span class="normal">135</span>
<span class="normal">136</span>
<span class="normal">137</span>
<span class="normal">138</span>
<span class="normal">139</span>
<span class="normal">140</span>
<span class="normal">141</span>
<span class="normal">142</span>
<span class="normal">143</span>
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
<span class="normal">192</span>
<span class="normal">193</span>
<span class="normal">194</span>
<span class="normal">195</span>
<span class="normal">196</span>
<span class="normal">197</span>
<span class="normal">198</span>
<span class="normal">199</span>
<span class="normal">200</span>
<span class="normal">201</span>
<span class="normal">202</span>
<span class="normal">203</span>
<span class="normal">204</span>
<span class="normal">205</span>
<span class="normal">206</span>
<span class="normal">207</span>
<span class="normal">208</span>
<span class="normal">209</span>
<span class="normal">210</span>
<span class="normal">211</span>
<span class="normal">212</span>
<span class="normal">213</span>
<span class="normal">214</span>
<span class="normal">215</span>
<span class="normal">216</span>
<span class="normal">217</span>
<span class="normal">218</span>
<span class="normal">219</span>
<span class="normal">220</span>
<span class="normal">221</span>
<span class="normal">222</span>
<span class="normal">223</span>
<span class="normal">224</span>
<span class="normal">225</span></pre></div></td><td class="code"><div><pre id="__code_17"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_17 > code"></button><code tabindex="0"><span class="k">class</span><span class="w"> </span><span class="nc">BaseStatePersistence</span><span class="p">(</span><span class="n">ABC</span><span class="p">,</span> <span class="n">Generic</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""Abstract base class for storing the state of a graph run.</span>

<span class="sd">    Each instance of a `BaseStatePersistence` subclass should be used for a single graph run.</span>
<span class="sd">    """</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">snapshot_node</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">:</span> <span class="n">StateT</span><span class="p">,</span> <span class="n">next_node</span><span class="p">:</span> <span class="n">BaseNode</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">Any</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Snapshot the state of a graph, when the next step is to run a node.</span>

<span class="sd">        This method should add a [`NodeSnapshot`][pydantic_graph.persistence.NodeSnapshot] to persistence.</span>

<span class="sd">        Args:</span>
<span class="sd">            state: The state of the graph.</span>
<span class="sd">            next_node: The next node to run.</span>
<span class="sd">        """</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">snapshot_node_if_new</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">snapshot_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">state</span><span class="p">:</span> <span class="n">StateT</span><span class="p">,</span> <span class="n">next_node</span><span class="p">:</span> <span class="n">BaseNode</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">Any</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Snapshot the state of a graph if the snapshot ID doesn't already exist in persistence.</span>

<span class="sd">        This method will generally call [`snapshot_node`][pydantic_graph.persistence.BaseStatePersistence.snapshot_node]</span>
<span class="sd">        but should do so in an atomic way.</span>

<span class="sd">        Args:</span>
<span class="sd">            snapshot_id: The ID of the snapshot to check.</span>
<span class="sd">            state: The state of the graph.</span>
<span class="sd">            next_node: The next node to run.</span>
<span class="sd">        """</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">snapshot_end</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">:</span> <span class="n">StateT</span><span class="p">,</span> <span class="n">end</span><span class="p">:</span> <span class="n">End</span><span class="p">[</span><span class="n">RunEndT</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Snapshot the state of a graph when the graph has ended.</span>

<span class="sd">        This method should add an [`EndSnapshot`][pydantic_graph.persistence.EndSnapshot] to persistence.</span>

<span class="sd">        Args:</span>
<span class="sd">            state: The state of the graph.</span>
<span class="sd">            end: data from the end of the run.</span>
<span class="sd">        """</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">record_run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">snapshot_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AbstractAsyncContextManager</span><span class="p">[</span><span class="kc">None</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Record the run of the node, or error if the node is already running.</span>

<span class="sd">        Args:</span>
<span class="sd">            snapshot_id: The ID of the snapshot to record.</span>

<span class="sd">        Raises:</span>
<span class="sd">            GraphNodeRunningError: if the node status it not `'created'` or `'pending'`.</span>
<span class="sd">            LookupError: if the snapshot ID is not found in persistence.</span>

<span class="sd">        Returns:</span>
<span class="sd">            An async context manager that records the run of the node.</span>

<span class="sd">        In particular this should set:</span>

<span class="sd">        - [`NodeSnapshot.status`][pydantic_graph.persistence.NodeSnapshot.status] to `'running'` and</span>
<span class="sd">          [`NodeSnapshot.start_ts`][pydantic_graph.persistence.NodeSnapshot.start_ts] when the run starts.</span>
<span class="sd">        - [`NodeSnapshot.status`][pydantic_graph.persistence.NodeSnapshot.status] to `'success'` or `'error'` and</span>
<span class="sd">          [`NodeSnapshot.duration`][pydantic_graph.persistence.NodeSnapshot.duration] when the run finishes.</span>
<span class="sd">        """</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">load_next</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">NodeSnapshot</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Retrieve a node snapshot with status `'created`' and set its status to `'pending'`.</span>

<span class="sd">        This is used by [`Graph.iter_from_persistence`][pydantic_graph.graph.Graph.iter_from_persistence]</span>
<span class="sd">        to get the next node to run.</span>

<span class="sd">        Returns: The snapshot, or `None` if no snapshot with status `'created`' exists.</span>
<span class="sd">        """</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">load_all</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">list</span><span class="p">[</span><span class="n">Snapshot</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""Load the entire history of snapshots.</span>

<span class="sd">        `load_all` is not used by pydantic-graph itself, instead it's provided to make it convenient to</span>
<span class="sd">        get all [snapshots][pydantic_graph.persistence.Snapshot] from persistence.</span>

<span class="sd">        Returns: The list of snapshots.</span>
<span class="sd">        """</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">set_graph_types</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">graph</span><span class="p">:</span> <span class="n">Graph</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">Any</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Set the types of the state and run end from a graph.</span>

<span class="sd">        You generally won't need to customise this method, instead implement</span>
<span class="sd">        [`set_types`][pydantic_graph.persistence.BaseStatePersistence.set_types] and</span>
<span class="sd">        [`should_set_types`][pydantic_graph.persistence.BaseStatePersistence.should_set_types].</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">should_set_types</span><span class="p">():</span>
            <span class="k">with</span> <span class="n">_utils</span><span class="o">.</span><span class="n">set_nodes_type_context</span><span class="p">(</span><span class="n">graph</span><span class="o">.</span><span class="n">get_nodes</span><span class="p">()):</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">set_types</span><span class="p">(</span><span class="o">*</span><span class="n">graph</span><span class="o">.</span><span class="n">inferred_types</span><span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">should_set_types</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Whether types need to be set.</span>

<span class="sd">        Implementations should override this method to return `True` when types have not been set if they are needed.</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="kc">False</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">set_types</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state_type</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n">StateT</span><span class="p">],</span> <span class="n">run_end_type</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n">RunEndT</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Set the types of the state and run end.</span>

<span class="sd">        This can be used to create [type adapters][pydantic.TypeAdapter] for serializing and deserializing snapshots,</span>
<span class="sd">        e.g. with [`build_snapshot_list_type_adapter`][pydantic_graph.persistence.build_snapshot_list_type_adapter].</span>

<span class="sd">        Args:</span>
<span class="sd">            state_type: The state type.</span>
<span class="sd">            run_end_type: The run end type.</span>
<span class="sd">        """</span>
        <span class="k">pass</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-function">


<h4 id="pydantic_graph.persistence.BaseStatePersistence.snapshot_node" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">snapshot_node</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-abstractmethod"><code>abstractmethod</code></small>
      <small class="doc doc-label doc-label-async"><code>async</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_18"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_18 > code"></button><code><span class="nf">snapshot_node</span><span class="p">(</span>
    <span class="n">state</span><span class="p">:</span> <span class="n"><span title="pydantic_graph.persistence.StateT">StateT</span></span><span class="p">,</span> <span class="n">next_node</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.BaseNode" href="../nodes/#pydantic_graph.nodes.BaseNode">BaseNode</a></span><span class="p">[</span><span class="n"><span title="pydantic_graph.persistence.StateT">StateT</span></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a></span><span class="p">,</span> <span class="n"><span title="pydantic_graph.persistence.RunEndT">RunEndT</span></span><span class="p">]</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Snapshot the state of a graph, when the next step is to run a node.</p>
<p>This method should add a <a class="autorefs autorefs-internal" href="#pydantic_graph.persistence.NodeSnapshot"><code>NodeSnapshot</code></a> to persistence.</p>


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
                <code>state</code>
            </td>
            <td>
                  <code><span title="pydantic_graph.persistence.StateT">StateT</span></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The state of the graph.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>next_node</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.BaseNode" href="../nodes/#pydantic_graph.nodes.BaseNode">BaseNode</a>[<span title="pydantic_graph.persistence.StateT">StateT</span>, <a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a>, <span title="pydantic_graph.persistence.RunEndT">RunEndT</span>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The next node to run.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_graph/pydantic_graph/persistence/__init__.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">112</span>
<span class="normal">113</span>
<span class="normal">114</span>
<span class="normal">115</span>
<span class="normal">116</span>
<span class="normal">117</span>
<span class="normal">118</span>
<span class="normal">119</span>
<span class="normal">120</span>
<span class="normal">121</span>
<span class="normal">122</span></pre></div></td><td class="code"><div><pre id="__code_19"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_19 > code"></button><code><span class="nd">@abstractmethod</span>
<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">snapshot_node</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">:</span> <span class="n">StateT</span><span class="p">,</span> <span class="n">next_node</span><span class="p">:</span> <span class="n">BaseNode</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">Any</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Snapshot the state of a graph, when the next step is to run a node.</span>

<span class="sd">    This method should add a [`NodeSnapshot`][pydantic_graph.persistence.NodeSnapshot] to persistence.</span>

<span class="sd">    Args:</span>
<span class="sd">        state: The state of the graph.</span>
<span class="sd">        next_node: The next node to run.</span>
<span class="sd">    """</span>
    <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_graph.persistence.BaseStatePersistence.snapshot_node_if_new" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">snapshot_node_if_new</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-abstractmethod"><code>abstractmethod</code></small>
      <small class="doc doc-label doc-label-async"><code>async</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_20"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_20 > code"></button><code><span class="nf">snapshot_node_if_new</span><span class="p">(</span>
    <span class="n">snapshot_id</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span><span class="p">,</span>
    <span class="n">state</span><span class="p">:</span> <span class="n"><span title="pydantic_graph.persistence.StateT">StateT</span></span><span class="p">,</span>
    <span class="n">next_node</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.BaseNode" href="../nodes/#pydantic_graph.nodes.BaseNode">BaseNode</a></span><span class="p">[</span><span class="n"><span title="pydantic_graph.persistence.StateT">StateT</span></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a></span><span class="p">,</span> <span class="n"><span title="pydantic_graph.persistence.RunEndT">RunEndT</span></span><span class="p">],</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Snapshot the state of a graph if the snapshot ID doesn't already exist in persistence.</p>
<p>This method will generally call <a class="autorefs autorefs-internal" href="#pydantic_graph.persistence.BaseStatePersistence.snapshot_node"><code>snapshot_node</code></a>
but should do so in an atomic way.</p>


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
                <code>snapshot_id</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The ID of the snapshot to check.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>state</code>
            </td>
            <td>
                  <code><span title="pydantic_graph.persistence.StateT">StateT</span></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The state of the graph.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>next_node</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.BaseNode" href="../nodes/#pydantic_graph.nodes.BaseNode">BaseNode</a>[<span title="pydantic_graph.persistence.StateT">StateT</span>, <a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a>, <span title="pydantic_graph.persistence.RunEndT">RunEndT</span>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The next node to run.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_graph/pydantic_graph/persistence/__init__.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">124</span>
<span class="normal">125</span>
<span class="normal">126</span>
<span class="normal">127</span>
<span class="normal">128</span>
<span class="normal">129</span>
<span class="normal">130</span>
<span class="normal">131</span>
<span class="normal">132</span>
<span class="normal">133</span>
<span class="normal">134</span>
<span class="normal">135</span>
<span class="normal">136</span>
<span class="normal">137</span>
<span class="normal">138</span></pre></div></td><td class="code"><div><pre id="__code_21"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_21 > code"></button><code tabindex="0"><span class="nd">@abstractmethod</span>
<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">snapshot_node_if_new</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">snapshot_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">state</span><span class="p">:</span> <span class="n">StateT</span><span class="p">,</span> <span class="n">next_node</span><span class="p">:</span> <span class="n">BaseNode</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">Any</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Snapshot the state of a graph if the snapshot ID doesn't already exist in persistence.</span>

<span class="sd">    This method will generally call [`snapshot_node`][pydantic_graph.persistence.BaseStatePersistence.snapshot_node]</span>
<span class="sd">    but should do so in an atomic way.</span>

<span class="sd">    Args:</span>
<span class="sd">        snapshot_id: The ID of the snapshot to check.</span>
<span class="sd">        state: The state of the graph.</span>
<span class="sd">        next_node: The next node to run.</span>
<span class="sd">    """</span>
    <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_graph.persistence.BaseStatePersistence.snapshot_end" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">snapshot_end</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-abstractmethod"><code>abstractmethod</code></small>
      <small class="doc doc-label doc-label-async"><code>async</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_22"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_22 > code"></button><code><span class="nf">snapshot_end</span><span class="p">(</span><span class="n">state</span><span class="p">:</span> <span class="n"><span title="pydantic_graph.persistence.StateT">StateT</span></span><span class="p">,</span> <span class="n">end</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.End" href="../nodes/#pydantic_graph.nodes.End">End</a></span><span class="p">[</span><span class="n"><span title="pydantic_graph.persistence.RunEndT">RunEndT</span></span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Snapshot the state of a graph when the graph has ended.</p>
<p>This method should add an <a class="autorefs autorefs-internal" href="#pydantic_graph.persistence.EndSnapshot"><code>EndSnapshot</code></a> to persistence.</p>


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
                <code>state</code>
            </td>
            <td>
                  <code><span title="pydantic_graph.persistence.StateT">StateT</span></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The state of the graph.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>end</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.End" href="../nodes/#pydantic_graph.nodes.End">End</a>[<span title="pydantic_graph.persistence.RunEndT">RunEndT</span>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>data from the end of the run.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_graph/pydantic_graph/persistence/__init__.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">140</span>
<span class="normal">141</span>
<span class="normal">142</span>
<span class="normal">143</span>
<span class="normal">144</span>
<span class="normal">145</span>
<span class="normal">146</span>
<span class="normal">147</span>
<span class="normal">148</span>
<span class="normal">149</span>
<span class="normal">150</span></pre></div></td><td class="code"><div><pre id="__code_23"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_23 > code"></button><code><span class="nd">@abstractmethod</span>
<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">snapshot_end</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">:</span> <span class="n">StateT</span><span class="p">,</span> <span class="n">end</span><span class="p">:</span> <span class="n">End</span><span class="p">[</span><span class="n">RunEndT</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Snapshot the state of a graph when the graph has ended.</span>

<span class="sd">    This method should add an [`EndSnapshot`][pydantic_graph.persistence.EndSnapshot] to persistence.</span>

<span class="sd">    Args:</span>
<span class="sd">        state: The state of the graph.</span>
<span class="sd">        end: data from the end of the run.</span>
<span class="sd">    """</span>
    <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_graph.persistence.BaseStatePersistence.record_run" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">record_run</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-abstractmethod"><code>abstractmethod</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_24"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_24 > code"></button><code><span class="nf">record_run</span><span class="p">(</span>
    <span class="n">snapshot_id</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" title="contextlib.AbstractAsyncContextManager" href="https://docs.python.org/3/library/contextlib.html#contextlib.AbstractAsyncContextManager">AbstractAsyncContextManager</a></span><span class="p">[</span><span class="kc">None</span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Record the run of the node, or error if the node is already running.</p>


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
                <code>snapshot_id</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The ID of the snapshot to record.</p>
              </div>
            </td>
            <td>
                <em>required</em>
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
                  <code>GraphNodeRunningError</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>if the node status it not <code>'created'</code> or <code>'pending'</code>.</p>
              </div>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/exceptions.html#LookupError">LookupError</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>if the snapshot ID is not found in persistence.</p>
              </div>
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
                  <code><a class="autorefs autorefs-external" title="contextlib.AbstractAsyncContextManager" href="https://docs.python.org/3/library/contextlib.html#contextlib.AbstractAsyncContextManager">AbstractAsyncContextManager</a>[None]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>An async context manager that records the run of the node.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table></div></div>
        <p>In particular this should set:</p>
<ul>
<li><a class="autorefs autorefs-internal" href="#pydantic_graph.persistence.NodeSnapshot.status"><code>NodeSnapshot.status</code></a> to <code>'running'</code> and
  <a class="autorefs autorefs-internal" href="#pydantic_graph.persistence.NodeSnapshot.start_ts"><code>NodeSnapshot.start_ts</code></a> when the run starts.</li>
<li><a class="autorefs autorefs-internal" href="#pydantic_graph.persistence.NodeSnapshot.status"><code>NodeSnapshot.status</code></a> to <code>'success'</code> or <code>'error'</code> and
  <a class="autorefs autorefs-internal" href="#pydantic_graph.persistence.NodeSnapshot.duration"><code>NodeSnapshot.duration</code></a> when the run finishes.</li>
</ul>

            <details class="quote">
              <summary>Source code in <code>pydantic_graph/pydantic_graph/persistence/__init__.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">152</span>
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
<span class="normal">173</span></pre></div></td><td class="code"><div><pre id="__code_25"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_25 > code"></button><code><span class="nd">@abstractmethod</span>
<span class="k">def</span><span class="w"> </span><span class="nf">record_run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">snapshot_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AbstractAsyncContextManager</span><span class="p">[</span><span class="kc">None</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Record the run of the node, or error if the node is already running.</span>

<span class="sd">    Args:</span>
<span class="sd">        snapshot_id: The ID of the snapshot to record.</span>

<span class="sd">    Raises:</span>
<span class="sd">        GraphNodeRunningError: if the node status it not `'created'` or `'pending'`.</span>
<span class="sd">        LookupError: if the snapshot ID is not found in persistence.</span>

<span class="sd">    Returns:</span>
<span class="sd">        An async context manager that records the run of the node.</span>

<span class="sd">    In particular this should set:</span>

<span class="sd">    - [`NodeSnapshot.status`][pydantic_graph.persistence.NodeSnapshot.status] to `'running'` and</span>
<span class="sd">      [`NodeSnapshot.start_ts`][pydantic_graph.persistence.NodeSnapshot.start_ts] when the run starts.</span>
<span class="sd">    - [`NodeSnapshot.status`][pydantic_graph.persistence.NodeSnapshot.status] to `'success'` or `'error'` and</span>
<span class="sd">      [`NodeSnapshot.duration`][pydantic_graph.persistence.NodeSnapshot.duration] when the run finishes.</span>
<span class="sd">    """</span>
    <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_graph.persistence.BaseStatePersistence.load_next" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">load_next</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-abstractmethod"><code>abstractmethod</code></small>
      <small class="doc doc-label doc-label-async"><code>async</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_26"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_26 > code"></button><code><span class="nf">load_next</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.persistence.NodeSnapshot" href="#pydantic_graph.persistence.NodeSnapshot">NodeSnapshot</a></span><span class="p">[</span><span class="n"><span title="pydantic_graph.persistence.StateT">StateT</span></span><span class="p">,</span> <span class="n"><span title="pydantic_graph.persistence.RunEndT">RunEndT</span></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Retrieve a node snapshot with status <code>'created</code>' and set its status to <code>'pending'</code>.</p>
<p>This is used by <a class="autorefs autorefs-internal" href="../graph/#pydantic_graph.graph.Graph.iter_from_persistence"><code>Graph.iter_from_persistence</code></a>
to get the next node to run.</p>
<p>Returns: The snapshot, or <code>None</code> if no snapshot with status <code>'created</code>' exists.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_graph/pydantic_graph/persistence/__init__.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">175</span>
<span class="normal">176</span>
<span class="normal">177</span>
<span class="normal">178</span>
<span class="normal">179</span>
<span class="normal">180</span>
<span class="normal">181</span>
<span class="normal">182</span>
<span class="normal">183</span>
<span class="normal">184</span></pre></div></td><td class="code"><div><pre id="__code_27"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_27 > code"></button><code><span class="nd">@abstractmethod</span>
<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">load_next</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">NodeSnapshot</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Retrieve a node snapshot with status `'created`' and set its status to `'pending'`.</span>

<span class="sd">    This is used by [`Graph.iter_from_persistence`][pydantic_graph.graph.Graph.iter_from_persistence]</span>
<span class="sd">    to get the next node to run.</span>

<span class="sd">    Returns: The snapshot, or `None` if no snapshot with status `'created`' exists.</span>
<span class="sd">    """</span>
    <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_graph.persistence.BaseStatePersistence.load_all" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">load_all</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-abstractmethod"><code>abstractmethod</code></small>
      <small class="doc doc-label doc-label-async"><code>async</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_28"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_28 > code"></button><code><span class="nf">load_all</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list">list</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.persistence.Snapshot" href="#pydantic_graph.persistence.Snapshot">Snapshot</a></span><span class="p">[</span><span class="n"><span title="pydantic_graph.persistence.StateT">StateT</span></span><span class="p">,</span> <span class="n"><span title="pydantic_graph.persistence.RunEndT">RunEndT</span></span><span class="p">]]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Load the entire history of snapshots.</p>
<p><code>load_all</code> is not used by pydantic-graph itself, instead it's provided to make it convenient to
get all <a class="autorefs autorefs-internal" href="#pydantic_graph.persistence.Snapshot">snapshots</a> from persistence.</p>
<p>Returns: The list of snapshots.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_graph/pydantic_graph/persistence/__init__.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">186</span>
<span class="normal">187</span>
<span class="normal">188</span>
<span class="normal">189</span>
<span class="normal">190</span>
<span class="normal">191</span>
<span class="normal">192</span>
<span class="normal">193</span>
<span class="normal">194</span>
<span class="normal">195</span></pre></div></td><td class="code"><div><pre id="__code_29"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_29 > code"></button><code><span class="nd">@abstractmethod</span>
<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">load_all</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">list</span><span class="p">[</span><span class="n">Snapshot</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]]:</span>
<span class="w">    </span><span class="sd">"""Load the entire history of snapshots.</span>

<span class="sd">    `load_all` is not used by pydantic-graph itself, instead it's provided to make it convenient to</span>
<span class="sd">    get all [snapshots][pydantic_graph.persistence.Snapshot] from persistence.</span>

<span class="sd">    Returns: The list of snapshots.</span>
<span class="sd">    """</span>
    <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_graph.persistence.BaseStatePersistence.set_graph_types" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">set_graph_types</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_30"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_30 > code"></button><code><span class="nf">set_graph_types</span><span class="p">(</span><span class="n">graph</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.Graph" href="../graph/#pydantic_graph.graph.Graph">Graph</a></span><span class="p">[</span><span class="n"><span title="pydantic_graph.persistence.StateT">StateT</span></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a></span><span class="p">,</span> <span class="n"><span title="pydantic_graph.persistence.RunEndT">RunEndT</span></span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Set the types of the state and run end from a graph.</p>
<p>You generally won't need to customise this method, instead implement
<a class="autorefs autorefs-internal" href="#pydantic_graph.persistence.BaseStatePersistence.set_types"><code>set_types</code></a> and
<a class="autorefs autorefs-internal" href="#pydantic_graph.persistence.BaseStatePersistence.should_set_types"><code>should_set_types</code></a>.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_graph/pydantic_graph/persistence/__init__.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">197</span>
<span class="normal">198</span>
<span class="normal">199</span>
<span class="normal">200</span>
<span class="normal">201</span>
<span class="normal">202</span>
<span class="normal">203</span>
<span class="normal">204</span>
<span class="normal">205</span>
<span class="normal">206</span></pre></div></td><td class="code"><div><pre id="__code_31"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_31 > code"></button><code><span class="k">def</span><span class="w"> </span><span class="nf">set_graph_types</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">graph</span><span class="p">:</span> <span class="n">Graph</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">Any</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Set the types of the state and run end from a graph.</span>

<span class="sd">    You generally won't need to customise this method, instead implement</span>
<span class="sd">    [`set_types`][pydantic_graph.persistence.BaseStatePersistence.set_types] and</span>
<span class="sd">    [`should_set_types`][pydantic_graph.persistence.BaseStatePersistence.should_set_types].</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">should_set_types</span><span class="p">():</span>
        <span class="k">with</span> <span class="n">_utils</span><span class="o">.</span><span class="n">set_nodes_type_context</span><span class="p">(</span><span class="n">graph</span><span class="o">.</span><span class="n">get_nodes</span><span class="p">()):</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">set_types</span><span class="p">(</span><span class="o">*</span><span class="n">graph</span><span class="o">.</span><span class="n">inferred_types</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_graph.persistence.BaseStatePersistence.should_set_types" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">should_set_types</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_32"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_32 > code"></button><code><span class="nf">should_set_types</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Whether types need to be set.</p>
<p>Implementations should override this method to return <code>True</code> when types have not been set if they are needed.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_graph/pydantic_graph/persistence/__init__.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">208</span>
<span class="normal">209</span>
<span class="normal">210</span>
<span class="normal">211</span>
<span class="normal">212</span>
<span class="normal">213</span></pre></div></td><td class="code"><div><pre id="__code_33"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_33 > code"></button><code tabindex="0"><span class="k">def</span><span class="w"> </span><span class="nf">should_set_types</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Whether types need to be set.</span>

<span class="sd">    Implementations should override this method to return `True` when types have not been set if they are needed.</span>
<span class="sd">    """</span>
    <span class="k">return</span> <span class="kc">False</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_graph.persistence.BaseStatePersistence.set_types" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">set_types</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_34"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_34 > code"></button><code><span class="nf">set_types</span><span class="p">(</span>
    <span class="n">state_type</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type">type</a></span><span class="p">[</span><span class="n"><span title="pydantic_graph.persistence.StateT">StateT</span></span><span class="p">],</span> <span class="n">run_end_type</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type">type</a></span><span class="p">[</span><span class="n"><span title="pydantic_graph.persistence.RunEndT">RunEndT</span></span><span class="p">]</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Set the types of the state and run end.</p>
<p>This can be used to create <a class="autorefs autorefs-external" href="https://docs.pydantic.dev/latest/api/type_adapter/#pydantic.type_adapter.TypeAdapter">type adapters</a> for serializing and deserializing snapshots,
e.g. with <a class="autorefs autorefs-internal" href="#pydantic_graph.persistence.build_snapshot_list_type_adapter"><code>build_snapshot_list_type_adapter</code></a>.</p>


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
                <code>state_type</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type">type</a>[<span title="pydantic_graph.persistence.StateT">StateT</span>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The state type.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>run_end_type</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type">type</a>[<span title="pydantic_graph.persistence.RunEndT">RunEndT</span>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The run end type.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_graph/pydantic_graph/persistence/__init__.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">215</span>
<span class="normal">216</span>
<span class="normal">217</span>
<span class="normal">218</span>
<span class="normal">219</span>
<span class="normal">220</span>
<span class="normal">221</span>
<span class="normal">222</span>
<span class="normal">223</span>
<span class="normal">224</span>
<span class="normal">225</span></pre></div></td><td class="code"><div><pre id="__code_35"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_35 > code"></button><code tabindex="0"><span class="k">def</span><span class="w"> </span><span class="nf">set_types</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state_type</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n">StateT</span><span class="p">],</span> <span class="n">run_end_type</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n">RunEndT</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Set the types of the state and run end.</span>

<span class="sd">    This can be used to create [type adapters][pydantic.TypeAdapter] for serializing and deserializing snapshots,</span>
<span class="sd">    e.g. with [`build_snapshot_list_type_adapter`][pydantic_graph.persistence.build_snapshot_list_type_adapter].</span>

<span class="sd">    Args:</span>
<span class="sd">        state_type: The state type.</span>
<span class="sd">        run_end_type: The run end type.</span>
<span class="sd">    """</span>
    <span class="k">pass</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>




  </div>

    </div>

</div>






<div class="doc doc-object doc-function">


<h3 id="pydantic_graph.persistence.build_snapshot_list_type_adapter" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">build_snapshot_list_type_adapter</span>


</h3>
<div class="language-python doc-signature highlight"><pre id="__code_36"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_36 > code"></button><code><span class="nf">build_snapshot_list_type_adapter</span><span class="p">(</span>
    <span class="n">state_t</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type">type</a></span><span class="p">[</span><span class="n"><span title="pydantic_graph.persistence.StateT">StateT</span></span><span class="p">],</span> <span class="n">run_end_t</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type">type</a></span><span class="p">[</span><span class="n"><span title="pydantic_graph.persistence.RunEndT">RunEndT</span></span><span class="p">]</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" title="pydantic.TypeAdapter" href="https://docs.pydantic.dev/latest/api/type_adapter/#pydantic.type_adapter.TypeAdapter">TypeAdapter</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list">list</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.persistence.Snapshot" href="#pydantic_graph.persistence.Snapshot">Snapshot</a></span><span class="p">[</span><span class="n"><span title="pydantic_graph.persistence.StateT">StateT</span></span><span class="p">,</span> <span class="n"><span title="pydantic_graph.persistence.RunEndT">RunEndT</span></span><span class="p">]]]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Build a type adapter for a list of snapshots.</p>
<p>This method should be called from within
<a class="autorefs autorefs-internal" href="#pydantic_graph.persistence.BaseStatePersistence.set_types"><code>set_types</code></a>
where context variables will be set such that Pydantic can create a schema for
<a class="autorefs autorefs-internal" href="#pydantic_graph.persistence.NodeSnapshot.node"><code>NodeSnapshot.node</code></a>.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_graph/pydantic_graph/persistence/__init__.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">228</span>
<span class="normal">229</span>
<span class="normal">230</span>
<span class="normal">231</span>
<span class="normal">232</span>
<span class="normal">233</span>
<span class="normal">234</span>
<span class="normal">235</span>
<span class="normal">236</span>
<span class="normal">237</span>
<span class="normal">238</span></pre></div></td><td class="code"><div><pre id="__code_37"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_37 > code"></button><code tabindex="0"><span class="k">def</span><span class="w"> </span><span class="nf">build_snapshot_list_type_adapter</span><span class="p">(</span>
    <span class="n">state_t</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n">StateT</span><span class="p">],</span> <span class="n">run_end_t</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n">RunEndT</span><span class="p">]</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">pydantic</span><span class="o">.</span><span class="n">TypeAdapter</span><span class="p">[</span><span class="nb">list</span><span class="p">[</span><span class="n">Snapshot</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]]]:</span>
<span class="w">    </span><span class="sd">"""Build a type adapter for a list of snapshots.</span>

<span class="sd">    This method should be called from within</span>
<span class="sd">    [`set_types`][pydantic_graph.persistence.BaseStatePersistence.set_types]</span>
<span class="sd">    where context variables will be set such that Pydantic can create a schema for</span>
<span class="sd">    [`NodeSnapshot.node`][pydantic_graph.persistence.NodeSnapshot.node].</span>
<span class="sd">    """</span>
    <span class="k">return</span> <span class="n">pydantic</span><span class="o">.</span><span class="n">TypeAdapter</span><span class="p">(</span><span class="nb">list</span><span class="p">[</span><span class="n">Annotated</span><span class="p">[</span><span class="n">Snapshot</span><span class="p">[</span><span class="n">state_t</span><span class="p">,</span> <span class="n">run_end_t</span><span class="p">],</span> <span class="n">pydantic</span><span class="o">.</span><span class="n">Discriminator</span><span class="p">(</span><span class="s1">'kind'</span><span class="p">)]])</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>




  </div>

    </div>

</div>

<div class="doc doc-object doc-module">



<a id="pydantic_graph.persistence.in_mem"></a>
    <div class="doc doc-contents first">

        <p>In memory state persistence.</p>
<p>This module provides simple in memory state persistence for graphs.</p>








  <div class="doc doc-children">







































<div class="doc doc-object doc-class">



<h3 id="pydantic_graph.persistence.in_mem.SimpleStatePersistence" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">SimpleStatePersistence</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">
            <p class="doc doc-class-bases">
              Bases: <code><a class="autorefs autorefs-internal" title="pydantic_graph.persistence.BaseStatePersistence" href="#pydantic_graph.persistence.BaseStatePersistence">BaseStatePersistence</a>[<span title="pydantic_graph.persistence.StateT">StateT</span>, <span title="pydantic_graph.persistence.RunEndT">RunEndT</span>]</code></p>


        <p>Simple in memory state persistence that just hold the latest snapshot.</p>
<p>If no state persistence implementation is provided when running a graph, this is used by default.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_graph/pydantic_graph/persistence/in_mem.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">31</span>
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
<span class="normal">42</span>
<span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span>
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
<span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span>
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
<span class="normal">82</span></pre></div></td><td class="code"><div><pre id="__code_38"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_38 > code"></button><code><span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">SimpleStatePersistence</span><span class="p">(</span><span class="n">BaseStatePersistence</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""Simple in memory state persistence that just hold the latest snapshot.</span>

<span class="sd">    If no state persistence implementation is provided when running a graph, this is used by default.</span>
<span class="sd">    """</span>

    <span class="n">last_snapshot</span><span class="p">:</span> <span class="n">Snapshot</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="w">    </span><span class="sd">"""The last snapshot."""</span>

    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">snapshot_node</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">:</span> <span class="n">StateT</span><span class="p">,</span> <span class="n">next_node</span><span class="p">:</span> <span class="n">BaseNode</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">Any</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">last_snapshot</span> <span class="o">=</span> <span class="n">NodeSnapshot</span><span class="p">(</span><span class="n">state</span><span class="o">=</span><span class="n">state</span><span class="p">,</span> <span class="n">node</span><span class="o">=</span><span class="n">next_node</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">snapshot_node_if_new</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">snapshot_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">state</span><span class="p">:</span> <span class="n">StateT</span><span class="p">,</span> <span class="n">next_node</span><span class="p">:</span> <span class="n">BaseNode</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">Any</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">last_snapshot</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">last_snapshot</span><span class="o">.</span><span class="n">id</span> <span class="o">==</span> <span class="n">snapshot_id</span><span class="p">:</span>
            <span class="k">return</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">snapshot_node</span><span class="p">(</span><span class="n">state</span><span class="p">,</span> <span class="n">next_node</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">snapshot_end</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">:</span> <span class="n">StateT</span><span class="p">,</span> <span class="n">end</span><span class="p">:</span> <span class="n">End</span><span class="p">[</span><span class="n">RunEndT</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">last_snapshot</span> <span class="o">=</span> <span class="n">EndSnapshot</span><span class="p">(</span><span class="n">state</span><span class="o">=</span><span class="n">state</span><span class="p">,</span> <span class="n">result</span><span class="o">=</span><span class="n">end</span><span class="p">)</span>

    <span class="nd">@asynccontextmanager</span>
    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">record_run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">snapshot_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AsyncIterator</span><span class="p">[</span><span class="kc">None</span><span class="p">]:</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">last_snapshot</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">or</span> <span class="n">snapshot_id</span> <span class="o">!=</span> <span class="bp">self</span><span class="o">.</span><span class="n">last_snapshot</span><span class="o">.</span><span class="n">id</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">LookupError</span><span class="p">(</span><span class="sa">f</span><span class="s1">'No snapshot found with id=</span><span class="si">{</span><span class="n">snapshot_id</span><span class="si">!r}</span><span class="s1">'</span><span class="p">)</span>

        <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">last_snapshot</span><span class="p">,</span> <span class="n">NodeSnapshot</span><span class="p">),</span> <span class="s1">'Only NodeSnapshot can be recorded'</span>
        <span class="n">exceptions</span><span class="o">.</span><span class="n">GraphNodeStatusError</span><span class="o">.</span><span class="n">check</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">last_snapshot</span><span class="o">.</span><span class="n">status</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">last_snapshot</span><span class="o">.</span><span class="n">status</span> <span class="o">=</span> <span class="s1">'running'</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">last_snapshot</span><span class="o">.</span><span class="n">start_ts</span> <span class="o">=</span> <span class="n">_utils</span><span class="o">.</span><span class="n">now_utc</span><span class="p">()</span>

        <span class="n">start</span> <span class="o">=</span> <span class="n">perf_counter</span><span class="p">()</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="k">yield</span>
        <span class="k">except</span> <span class="ne">Exception</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">last_snapshot</span><span class="o">.</span><span class="n">duration</span> <span class="o">=</span> <span class="n">perf_counter</span><span class="p">()</span> <span class="o">-</span> <span class="n">start</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">last_snapshot</span><span class="o">.</span><span class="n">status</span> <span class="o">=</span> <span class="s1">'error'</span>
            <span class="k">raise</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">last_snapshot</span><span class="o">.</span><span class="n">duration</span> <span class="o">=</span> <span class="n">perf_counter</span><span class="p">()</span> <span class="o">-</span> <span class="n">start</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">last_snapshot</span><span class="o">.</span><span class="n">status</span> <span class="o">=</span> <span class="s1">'success'</span>

    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">load_next</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">NodeSnapshot</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">last_snapshot</span><span class="p">,</span> <span class="n">NodeSnapshot</span><span class="p">)</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">last_snapshot</span><span class="o">.</span><span class="n">status</span> <span class="o">==</span> <span class="s1">'created'</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">last_snapshot</span><span class="o">.</span><span class="n">status</span> <span class="o">=</span> <span class="s1">'pending'</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">last_snapshot</span>

    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">load_all</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">list</span><span class="p">[</span><span class="n">Snapshot</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]]:</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span><span class="s1">'load is not supported for SimpleStatePersistence'</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-attribute">



<h4 id="pydantic_graph.persistence.in_mem.SimpleStatePersistence.last_snapshot" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">last_snapshot</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_39"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_39 > code"></button><code><span class="n">last_snapshot</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.persistence.Snapshot" href="#pydantic_graph.persistence.Snapshot">Snapshot</a></span><span class="p">[</span><span class="n"><span title="pydantic_graph.persistence.StateT">StateT</span></span><span class="p">,</span> <span class="n"><span title="pydantic_graph.persistence.RunEndT">RunEndT</span></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The last snapshot.</p>
    </div>

</div>




  </div>

    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_graph.persistence.in_mem.FullStatePersistence" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">FullStatePersistence</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">
            <p class="doc doc-class-bases">
              Bases: <code><a class="autorefs autorefs-internal" title="pydantic_graph.persistence.BaseStatePersistence" href="#pydantic_graph.persistence.BaseStatePersistence">BaseStatePersistence</a>[<span title="pydantic_graph.persistence.StateT">StateT</span>, <span title="pydantic_graph.persistence.RunEndT">RunEndT</span>]</code></p>


        <p>In memory state persistence that hold a list of snapshots.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_graph/pydantic_graph/persistence/in_mem.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 85</span>
<span class="normal"> 86</span>
<span class="normal"> 87</span>
<span class="normal"> 88</span>
<span class="normal"> 89</span>
<span class="normal"> 90</span>
<span class="normal"> 91</span>
<span class="normal"> 92</span>
<span class="normal"> 93</span>
<span class="normal"> 94</span>
<span class="normal"> 95</span>
<span class="normal"> 96</span>
<span class="normal"> 97</span>
<span class="normal"> 98</span>
<span class="normal"> 99</span>
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
<span class="normal">123</span>
<span class="normal">124</span>
<span class="normal">125</span>
<span class="normal">126</span>
<span class="normal">127</span>
<span class="normal">128</span>
<span class="normal">129</span>
<span class="normal">130</span>
<span class="normal">131</span>
<span class="normal">132</span>
<span class="normal">133</span>
<span class="normal">134</span>
<span class="normal">135</span>
<span class="normal">136</span>
<span class="normal">137</span>
<span class="normal">138</span>
<span class="normal">139</span>
<span class="normal">140</span>
<span class="normal">141</span>
<span class="normal">142</span>
<span class="normal">143</span>
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
<span class="normal">172</span></pre></div></td><td class="code"><div><pre id="__code_40"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_40 > code"></button><code tabindex="0"><span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">FullStatePersistence</span><span class="p">(</span><span class="n">BaseStatePersistence</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""In memory state persistence that hold a list of snapshots."""</span>

    <span class="n">deep_copy</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
<span class="w">    </span><span class="sd">"""Whether to deep copy the state and nodes when storing them.</span>

<span class="sd">    Defaults to `True` so even if nodes or state are modified after the snapshot is taken,</span>
<span class="sd">    the persistence history will record the value at the time of the snapshot.</span>
<span class="sd">    """</span>
    <span class="n">history</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">Snapshot</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]]</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span><span class="n">default_factory</span><span class="o">=</span><span class="nb">list</span><span class="p">)</span>
<span class="w">    </span><span class="sd">"""List of snapshots taken during the graph run."""</span>
    <span class="n">_snapshots_type_adapter</span><span class="p">:</span> <span class="n">pydantic</span><span class="o">.</span><span class="n">TypeAdapter</span><span class="p">[</span><span class="nb">list</span><span class="p">[</span><span class="n">Snapshot</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]]]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">init</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="nb">repr</span><span class="o">=</span><span class="kc">False</span>
    <span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">snapshot_node</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">:</span> <span class="n">StateT</span><span class="p">,</span> <span class="n">next_node</span><span class="p">:</span> <span class="n">BaseNode</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">Any</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">snapshot</span> <span class="o">=</span> <span class="n">NodeSnapshot</span><span class="p">(</span>
            <span class="n">state</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_prep_state</span><span class="p">(</span><span class="n">state</span><span class="p">),</span>
            <span class="n">node</span><span class="o">=</span><span class="n">next_node</span><span class="o">.</span><span class="n">deep_copy</span><span class="p">()</span> <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">deep_copy</span> <span class="k">else</span> <span class="n">next_node</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">history</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">snapshot</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">snapshot_node_if_new</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">snapshot_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">state</span><span class="p">:</span> <span class="n">StateT</span><span class="p">,</span> <span class="n">next_node</span><span class="p">:</span> <span class="n">BaseNode</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">Any</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="nb">any</span><span class="p">(</span><span class="n">s</span><span class="o">.</span><span class="n">id</span> <span class="o">==</span> <span class="n">snapshot_id</span> <span class="k">for</span> <span class="n">s</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">history</span><span class="p">):</span>
            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">snapshot_node</span><span class="p">(</span><span class="n">state</span><span class="p">,</span> <span class="n">next_node</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">snapshot_end</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">:</span> <span class="n">StateT</span><span class="p">,</span> <span class="n">end</span><span class="p">:</span> <span class="n">End</span><span class="p">[</span><span class="n">RunEndT</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">snapshot</span> <span class="o">=</span> <span class="n">EndSnapshot</span><span class="p">(</span>
            <span class="n">state</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_prep_state</span><span class="p">(</span><span class="n">state</span><span class="p">),</span>
            <span class="n">result</span><span class="o">=</span><span class="n">end</span><span class="o">.</span><span class="n">deep_copy_data</span><span class="p">()</span> <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">deep_copy</span> <span class="k">else</span> <span class="n">end</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">history</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">snapshot</span><span class="p">)</span>

    <span class="nd">@asynccontextmanager</span>
    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">record_run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">snapshot_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AsyncIterator</span><span class="p">[</span><span class="kc">None</span><span class="p">]:</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">snapshot</span> <span class="o">=</span> <span class="nb">next</span><span class="p">(</span><span class="n">s</span> <span class="k">for</span> <span class="n">s</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">history</span> <span class="k">if</span> <span class="n">s</span><span class="o">.</span><span class="n">id</span> <span class="o">==</span> <span class="n">snapshot_id</span><span class="p">)</span>
        <span class="k">except</span> <span class="ne">StopIteration</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">LookupError</span><span class="p">(</span><span class="sa">f</span><span class="s1">'No snapshot found with id=</span><span class="si">{</span><span class="n">snapshot_id</span><span class="si">!r}</span><span class="s1">'</span><span class="p">)</span> <span class="kn">from</span><span class="w"> </span><span class="nn">e</span>

        <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">snapshot</span><span class="p">,</span> <span class="n">NodeSnapshot</span><span class="p">),</span> <span class="s1">'Only NodeSnapshot can be recorded'</span>
        <span class="n">exceptions</span><span class="o">.</span><span class="n">GraphNodeStatusError</span><span class="o">.</span><span class="n">check</span><span class="p">(</span><span class="n">snapshot</span><span class="o">.</span><span class="n">status</span><span class="p">)</span>
        <span class="n">snapshot</span><span class="o">.</span><span class="n">status</span> <span class="o">=</span> <span class="s1">'running'</span>
        <span class="n">snapshot</span><span class="o">.</span><span class="n">start_ts</span> <span class="o">=</span> <span class="n">_utils</span><span class="o">.</span><span class="n">now_utc</span><span class="p">()</span>
        <span class="n">start</span> <span class="o">=</span> <span class="n">perf_counter</span><span class="p">()</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="k">yield</span>
        <span class="k">except</span> <span class="ne">Exception</span><span class="p">:</span>
            <span class="n">snapshot</span><span class="o">.</span><span class="n">duration</span> <span class="o">=</span> <span class="n">perf_counter</span><span class="p">()</span> <span class="o">-</span> <span class="n">start</span>
            <span class="n">snapshot</span><span class="o">.</span><span class="n">status</span> <span class="o">=</span> <span class="s1">'error'</span>
            <span class="k">raise</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">snapshot</span><span class="o">.</span><span class="n">duration</span> <span class="o">=</span> <span class="n">perf_counter</span><span class="p">()</span> <span class="o">-</span> <span class="n">start</span>
            <span class="n">snapshot</span><span class="o">.</span><span class="n">status</span> <span class="o">=</span> <span class="s1">'success'</span>

    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">load_next</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">NodeSnapshot</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">snapshot</span> <span class="o">:=</span> <span class="nb">next</span><span class="p">((</span><span class="n">s</span> <span class="k">for</span> <span class="n">s</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">history</span> <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">s</span><span class="p">,</span> <span class="n">NodeSnapshot</span><span class="p">)</span> <span class="ow">and</span> <span class="n">s</span><span class="o">.</span><span class="n">status</span> <span class="o">==</span> <span class="s1">'created'</span><span class="p">),</span> <span class="kc">None</span><span class="p">):</span>
            <span class="n">snapshot</span><span class="o">.</span><span class="n">status</span> <span class="o">=</span> <span class="s1">'pending'</span>
            <span class="k">return</span> <span class="n">snapshot</span>

    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">load_all</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">list</span><span class="p">[</span><span class="n">Snapshot</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]]:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">history</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">should_set_types</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_snapshots_type_adapter</span> <span class="ow">is</span> <span class="kc">None</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">set_types</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state_type</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n">StateT</span><span class="p">],</span> <span class="n">run_end_type</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n">RunEndT</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_snapshots_type_adapter</span> <span class="o">=</span> <span class="n">build_snapshot_list_type_adapter</span><span class="p">(</span><span class="n">state_type</span><span class="p">,</span> <span class="n">run_end_type</span><span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">dump_json</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">indent</span><span class="p">:</span> <span class="nb">int</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bytes</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Dump the history to JSON bytes."""</span>
        <span class="k">assert</span> <span class="bp">self</span><span class="o">.</span><span class="n">_snapshots_type_adapter</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">,</span> <span class="s1">'type adapter must be set to use `dump_json`'</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_snapshots_type_adapter</span><span class="o">.</span><span class="n">dump_json</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">history</span><span class="p">,</span> <span class="n">indent</span><span class="o">=</span><span class="n">indent</span><span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">load_json</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">json_data</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="nb">bytes</span> <span class="o">|</span> <span class="nb">bytearray</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Load the history from JSON."""</span>
        <span class="k">assert</span> <span class="bp">self</span><span class="o">.</span><span class="n">_snapshots_type_adapter</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">,</span> <span class="s1">'type adapter must be set to use `load_json`'</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">history</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_snapshots_type_adapter</span><span class="o">.</span><span class="n">validate_json</span><span class="p">(</span><span class="n">json_data</span><span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">_prep_state</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">:</span> <span class="n">StateT</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">StateT</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Prepare state for snapshot, uses [`copy.deepcopy`][copy.deepcopy] by default."""</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">deep_copy</span> <span class="ow">or</span> <span class="n">state</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">state</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">state</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-attribute">



<h4 id="pydantic_graph.persistence.in_mem.FullStatePersistence.deep_copy" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">deep_copy</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_41"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_41 > code"></button><code><span class="n">deep_copy</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">True</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Whether to deep copy the state and nodes when storing them.</p>
<p>Defaults to <code>True</code> so even if nodes or state are modified after the snapshot is taken,
the persistence history will record the value at the time of the snapshot.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_graph.persistence.in_mem.FullStatePersistence.history" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">history</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_42"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_42 > code"></button><code><span class="n">history</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list">list</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.persistence.Snapshot" href="#pydantic_graph.persistence.Snapshot">Snapshot</a></span><span class="p">[</span><span class="n"><span title="pydantic_graph.persistence.StateT">StateT</span></span><span class="p">,</span> <span class="n"><span title="pydantic_graph.persistence.RunEndT">RunEndT</span></span><span class="p">]]</span> <span class="o">=</span> <span class="n"><a class="autorefs autorefs-external" title="dataclasses.field" href="https://docs.python.org/3/library/dataclasses.html#dataclasses.field">field</a></span><span class="p">(</span>
    <span class="n"><span title="dataclasses.field(default_factory)">default_factory</span></span><span class="o">=</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list">list</a></span>
<span class="p">)</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>List of snapshots taken during the graph run.</p>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_graph.persistence.in_mem.FullStatePersistence.dump_json" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">dump_json</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_43"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_43 > code"></button><code><span class="nf">dump_json</span><span class="p">(</span><span class="o">*</span><span class="p">,</span> <span class="n">indent</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#int">int</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#bytes">bytes</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Dump the history to JSON bytes.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_graph/pydantic_graph/persistence/in_mem.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">157</span>
<span class="normal">158</span>
<span class="normal">159</span>
<span class="normal">160</span></pre></div></td><td class="code"><div><pre id="__code_44"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_44 > code"></button><code><span class="k">def</span><span class="w"> </span><span class="nf">dump_json</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">indent</span><span class="p">:</span> <span class="nb">int</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bytes</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Dump the history to JSON bytes."""</span>
    <span class="k">assert</span> <span class="bp">self</span><span class="o">.</span><span class="n">_snapshots_type_adapter</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">,</span> <span class="s1">'type adapter must be set to use `dump_json`'</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_snapshots_type_adapter</span><span class="o">.</span><span class="n">dump_json</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">history</span><span class="p">,</span> <span class="n">indent</span><span class="o">=</span><span class="n">indent</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_graph.persistence.in_mem.FullStatePersistence.load_json" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">load_json</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_45"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_45 > code"></button><code><span class="nf">load_json</span><span class="p">(</span><span class="n">json_data</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#bytes">bytes</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#bytearray">bytearray</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Load the history from JSON.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_graph/pydantic_graph/persistence/in_mem.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">162</span>
<span class="normal">163</span>
<span class="normal">164</span>
<span class="normal">165</span></pre></div></td><td class="code"><div><pre id="__code_46"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_46 > code"></button><code><span class="k">def</span><span class="w"> </span><span class="nf">load_json</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">json_data</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="nb">bytes</span> <span class="o">|</span> <span class="nb">bytearray</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Load the history from JSON."""</span>
    <span class="k">assert</span> <span class="bp">self</span><span class="o">.</span><span class="n">_snapshots_type_adapter</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">,</span> <span class="s1">'type adapter must be set to use `load_json`'</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">history</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_snapshots_type_adapter</span><span class="o">.</span><span class="n">validate_json</span><span class="p">(</span><span class="n">json_data</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>








  </div>

    </div>

</div>




  </div>

    </div>

</div>

<div class="doc doc-object doc-module">



<a id="pydantic_graph.persistence.file"></a>
    <div class="doc doc-contents first">








  <div class="doc doc-children">















































<div class="doc doc-object doc-class">



<h3 id="pydantic_graph.persistence.file.FileStatePersistence" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">FileStatePersistence</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">
            <p class="doc doc-class-bases">
              Bases: <code><a class="autorefs autorefs-internal" title="pydantic_graph.persistence.BaseStatePersistence" href="#pydantic_graph.persistence.BaseStatePersistence">BaseStatePersistence</a>[<span title="pydantic_graph.persistence.StateT">StateT</span>, <span title="pydantic_graph.persistence.RunEndT">RunEndT</span>]</code></p>


        <p>File based state persistence that hold graph run state in a JSON file.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_graph/pydantic_graph/persistence/file.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 29</span>
<span class="normal"> 30</span>
<span class="normal"> 31</span>
<span class="normal"> 32</span>
<span class="normal"> 33</span>
<span class="normal"> 34</span>
<span class="normal"> 35</span>
<span class="normal"> 36</span>
<span class="normal"> 37</span>
<span class="normal"> 38</span>
<span class="normal"> 39</span>
<span class="normal"> 40</span>
<span class="normal"> 41</span>
<span class="normal"> 42</span>
<span class="normal"> 43</span>
<span class="normal"> 44</span>
<span class="normal"> 45</span>
<span class="normal"> 46</span>
<span class="normal"> 47</span>
<span class="normal"> 48</span>
<span class="normal"> 49</span>
<span class="normal"> 50</span>
<span class="normal"> 51</span>
<span class="normal"> 52</span>
<span class="normal"> 53</span>
<span class="normal"> 54</span>
<span class="normal"> 55</span>
<span class="normal"> 56</span>
<span class="normal"> 57</span>
<span class="normal"> 58</span>
<span class="normal"> 59</span>
<span class="normal"> 60</span>
<span class="normal"> 61</span>
<span class="normal"> 62</span>
<span class="normal"> 63</span>
<span class="normal"> 64</span>
<span class="normal"> 65</span>
<span class="normal"> 66</span>
<span class="normal"> 67</span>
<span class="normal"> 68</span>
<span class="normal"> 69</span>
<span class="normal"> 70</span>
<span class="normal"> 71</span>
<span class="normal"> 72</span>
<span class="normal"> 73</span>
<span class="normal"> 74</span>
<span class="normal"> 75</span>
<span class="normal"> 76</span>
<span class="normal"> 77</span>
<span class="normal"> 78</span>
<span class="normal"> 79</span>
<span class="normal"> 80</span>
<span class="normal"> 81</span>
<span class="normal"> 82</span>
<span class="normal"> 83</span>
<span class="normal"> 84</span>
<span class="normal"> 85</span>
<span class="normal"> 86</span>
<span class="normal"> 87</span>
<span class="normal"> 88</span>
<span class="normal"> 89</span>
<span class="normal"> 90</span>
<span class="normal"> 91</span>
<span class="normal"> 92</span>
<span class="normal"> 93</span>
<span class="normal"> 94</span>
<span class="normal"> 95</span>
<span class="normal"> 96</span>
<span class="normal"> 97</span>
<span class="normal"> 98</span>
<span class="normal"> 99</span>
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
<span class="normal">123</span>
<span class="normal">124</span>
<span class="normal">125</span>
<span class="normal">126</span>
<span class="normal">127</span>
<span class="normal">128</span>
<span class="normal">129</span>
<span class="normal">130</span>
<span class="normal">131</span>
<span class="normal">132</span>
<span class="normal">133</span>
<span class="normal">134</span>
<span class="normal">135</span>
<span class="normal">136</span>
<span class="normal">137</span>
<span class="normal">138</span>
<span class="normal">139</span>
<span class="normal">140</span>
<span class="normal">141</span>
<span class="normal">142</span>
<span class="normal">143</span>
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
<span class="normal">162</span></pre></div></td><td class="code"><div><pre id="__code_47"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_47 > code"></button><code tabindex="0"><span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">FileStatePersistence</span><span class="p">(</span><span class="n">BaseStatePersistence</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""File based state persistence that hold graph run state in a JSON file."""</span>

    <span class="n">json_file</span><span class="p">:</span> <span class="n">Path</span>
<span class="w">    </span><span class="sd">"""Path to the JSON file where the snapshots are stored.</span>

<span class="sd">    You should use a different file for each graph run, but a single file should be reused for multiple</span>
<span class="sd">    steps of the same run.</span>

<span class="sd">    For example if you have a run ID of the form `run_123abc`, you might create a `FileStatePersistence` thus:</span>

<span class="sd">    ```py</span>
<span class="sd">    from pathlib import Path</span>

<span class="sd">    from pydantic_graph import FullStatePersistence</span>

<span class="sd">    run_id = 'run_123abc'</span>
<span class="sd">    persistence = FullStatePersistence(Path('runs') / f'{run_id}.json')</span>
<span class="sd">    ```</span>
<span class="sd">    """</span>
    <span class="n">_snapshots_type_adapter</span><span class="p">:</span> <span class="n">pydantic</span><span class="o">.</span><span class="n">TypeAdapter</span><span class="p">[</span><span class="nb">list</span><span class="p">[</span><span class="n">Snapshot</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]]]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">init</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="nb">repr</span><span class="o">=</span><span class="kc">False</span>
    <span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">snapshot_node</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">:</span> <span class="n">StateT</span><span class="p">,</span> <span class="n">next_node</span><span class="p">:</span> <span class="n">BaseNode</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">Any</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_append_save</span><span class="p">(</span><span class="n">NodeSnapshot</span><span class="p">(</span><span class="n">state</span><span class="o">=</span><span class="n">state</span><span class="p">,</span> <span class="n">node</span><span class="o">=</span><span class="n">next_node</span><span class="p">))</span>

    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">snapshot_node_if_new</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">snapshot_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">state</span><span class="p">:</span> <span class="n">StateT</span><span class="p">,</span> <span class="n">next_node</span><span class="p">:</span> <span class="n">BaseNode</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">Any</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">async</span> <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_lock</span><span class="p">():</span>
            <span class="n">snapshots</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">load_all</span><span class="p">()</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="nb">any</span><span class="p">(</span><span class="n">s</span><span class="o">.</span><span class="n">id</span> <span class="o">==</span> <span class="n">snapshot_id</span> <span class="k">for</span> <span class="n">s</span> <span class="ow">in</span> <span class="n">snapshots</span><span class="p">):</span>
                <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_append_save</span><span class="p">(</span><span class="n">NodeSnapshot</span><span class="p">(</span><span class="n">state</span><span class="o">=</span><span class="n">state</span><span class="p">,</span> <span class="n">node</span><span class="o">=</span><span class="n">next_node</span><span class="p">),</span> <span class="n">lock</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">snapshot_end</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">:</span> <span class="n">StateT</span><span class="p">,</span> <span class="n">end</span><span class="p">:</span> <span class="n">End</span><span class="p">[</span><span class="n">RunEndT</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_append_save</span><span class="p">(</span><span class="n">EndSnapshot</span><span class="p">(</span><span class="n">state</span><span class="o">=</span><span class="n">state</span><span class="p">,</span> <span class="n">result</span><span class="o">=</span><span class="n">end</span><span class="p">))</span>

    <span class="nd">@asynccontextmanager</span>
    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">record_run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">snapshot_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AsyncIterator</span><span class="p">[</span><span class="kc">None</span><span class="p">]:</span>
        <span class="k">async</span> <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_lock</span><span class="p">():</span>
            <span class="n">snapshots</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">load_all</span><span class="p">()</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="n">snapshot</span> <span class="o">=</span> <span class="nb">next</span><span class="p">(</span><span class="n">s</span> <span class="k">for</span> <span class="n">s</span> <span class="ow">in</span> <span class="n">snapshots</span> <span class="k">if</span> <span class="n">s</span><span class="o">.</span><span class="n">id</span> <span class="o">==</span> <span class="n">snapshot_id</span><span class="p">)</span>
            <span class="k">except</span> <span class="ne">StopIteration</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">LookupError</span><span class="p">(</span><span class="sa">f</span><span class="s1">'No snapshot found with id=</span><span class="si">{</span><span class="n">snapshot_id</span><span class="si">!r}</span><span class="s1">'</span><span class="p">)</span> <span class="kn">from</span><span class="w"> </span><span class="nn">e</span>

            <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">snapshot</span><span class="p">,</span> <span class="n">NodeSnapshot</span><span class="p">),</span> <span class="s1">'Only NodeSnapshot can be recorded'</span>
            <span class="n">exceptions</span><span class="o">.</span><span class="n">GraphNodeStatusError</span><span class="o">.</span><span class="n">check</span><span class="p">(</span><span class="n">snapshot</span><span class="o">.</span><span class="n">status</span><span class="p">)</span>
            <span class="n">snapshot</span><span class="o">.</span><span class="n">status</span> <span class="o">=</span> <span class="s1">'running'</span>
            <span class="n">snapshot</span><span class="o">.</span><span class="n">start_ts</span> <span class="o">=</span> <span class="n">_utils</span><span class="o">.</span><span class="n">now_utc</span><span class="p">()</span>
            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="n">snapshots</span><span class="p">)</span>

        <span class="n">start</span> <span class="o">=</span> <span class="n">perf_counter</span><span class="p">()</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="k">yield</span>
        <span class="k">except</span> <span class="ne">Exception</span><span class="p">:</span>
            <span class="n">duration</span> <span class="o">=</span> <span class="n">perf_counter</span><span class="p">()</span> <span class="o">-</span> <span class="n">start</span>
            <span class="k">async</span> <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_lock</span><span class="p">():</span>
                <span class="k">await</span> <span class="n">_graph_utils</span><span class="o">.</span><span class="n">run_in_executor</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_after_run_sync</span><span class="p">,</span> <span class="n">snapshot_id</span><span class="p">,</span> <span class="n">duration</span><span class="p">,</span> <span class="s1">'error'</span><span class="p">)</span>
            <span class="k">raise</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">snapshot</span><span class="o">.</span><span class="n">duration</span> <span class="o">=</span> <span class="n">perf_counter</span><span class="p">()</span> <span class="o">-</span> <span class="n">start</span>
            <span class="k">async</span> <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_lock</span><span class="p">():</span>
                <span class="k">await</span> <span class="n">_graph_utils</span><span class="o">.</span><span class="n">run_in_executor</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_after_run_sync</span><span class="p">,</span> <span class="n">snapshot_id</span><span class="p">,</span> <span class="n">snapshot</span><span class="o">.</span><span class="n">duration</span><span class="p">,</span> <span class="s1">'success'</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">load_next</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">NodeSnapshot</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">async</span> <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_lock</span><span class="p">():</span>
            <span class="n">snapshots</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">load_all</span><span class="p">()</span>
            <span class="k">if</span> <span class="n">snapshot</span> <span class="o">:=</span> <span class="nb">next</span><span class="p">((</span><span class="n">s</span> <span class="k">for</span> <span class="n">s</span> <span class="ow">in</span> <span class="n">snapshots</span> <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">s</span><span class="p">,</span> <span class="n">NodeSnapshot</span><span class="p">)</span> <span class="ow">and</span> <span class="n">s</span><span class="o">.</span><span class="n">status</span> <span class="o">==</span> <span class="s1">'created'</span><span class="p">),</span> <span class="kc">None</span><span class="p">):</span>
                <span class="n">snapshot</span><span class="o">.</span><span class="n">status</span> <span class="o">=</span> <span class="s1">'pending'</span>
                <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="n">snapshots</span><span class="p">)</span>
                <span class="k">return</span> <span class="n">snapshot</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">should_set_types</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Whether types need to be set."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_snapshots_type_adapter</span> <span class="ow">is</span> <span class="kc">None</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">set_types</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state_type</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n">StateT</span><span class="p">],</span> <span class="n">run_end_type</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n">RunEndT</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_snapshots_type_adapter</span> <span class="o">=</span> <span class="n">build_snapshot_list_type_adapter</span><span class="p">(</span><span class="n">state_type</span><span class="p">,</span> <span class="n">run_end_type</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">load_all</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">list</span><span class="p">[</span><span class="n">Snapshot</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]]:</span>
        <span class="k">return</span> <span class="k">await</span> <span class="n">_graph_utils</span><span class="o">.</span><span class="n">run_in_executor</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_load_sync</span><span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">_load_sync</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">list</span><span class="p">[</span><span class="n">Snapshot</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]]:</span>
        <span class="k">assert</span> <span class="bp">self</span><span class="o">.</span><span class="n">_snapshots_type_adapter</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">,</span> <span class="s1">'snapshots type adapter must be set'</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">content</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">json_file</span><span class="o">.</span><span class="n">read_bytes</span><span class="p">()</span>
        <span class="k">except</span> <span class="ne">FileNotFoundError</span><span class="p">:</span>
            <span class="k">return</span> <span class="p">[]</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_snapshots_type_adapter</span><span class="o">.</span><span class="n">validate_json</span><span class="p">(</span><span class="n">content</span><span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">_after_run_sync</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">snapshot_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">duration</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span> <span class="n">status</span><span class="p">:</span> <span class="n">SnapshotStatus</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">snapshots</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_load_sync</span><span class="p">()</span>
        <span class="n">snapshot</span> <span class="o">=</span> <span class="nb">next</span><span class="p">(</span><span class="n">s</span> <span class="k">for</span> <span class="n">s</span> <span class="ow">in</span> <span class="n">snapshots</span> <span class="k">if</span> <span class="n">s</span><span class="o">.</span><span class="n">id</span> <span class="o">==</span> <span class="n">snapshot_id</span><span class="p">)</span>
        <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">snapshot</span><span class="p">,</span> <span class="n">NodeSnapshot</span><span class="p">),</span> <span class="s1">'Only NodeSnapshot can be recorded'</span>
        <span class="n">snapshot</span><span class="o">.</span><span class="n">duration</span> <span class="o">=</span> <span class="n">duration</span>
        <span class="n">snapshot</span><span class="o">.</span><span class="n">status</span> <span class="o">=</span> <span class="n">status</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_save_sync</span><span class="p">(</span><span class="n">snapshots</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">_save</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">snapshots</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">Snapshot</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">await</span> <span class="n">_graph_utils</span><span class="o">.</span><span class="n">run_in_executor</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_save_sync</span><span class="p">,</span> <span class="n">snapshots</span><span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">_save_sync</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">snapshots</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">Snapshot</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">assert</span> <span class="bp">self</span><span class="o">.</span><span class="n">_snapshots_type_adapter</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">,</span> <span class="s1">'snapshots type adapter must be set'</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">json_file</span><span class="o">.</span><span class="n">write_bytes</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_snapshots_type_adapter</span><span class="o">.</span><span class="n">dump_json</span><span class="p">(</span><span class="n">snapshots</span><span class="p">,</span> <span class="n">indent</span><span class="o">=</span><span class="mi">2</span><span class="p">))</span>

    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">_append_save</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">snapshot</span><span class="p">:</span> <span class="n">Snapshot</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">],</span> <span class="o">*</span><span class="p">,</span> <span class="n">lock</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">assert</span> <span class="bp">self</span><span class="o">.</span><span class="n">_snapshots_type_adapter</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">,</span> <span class="s1">'snapshots type adapter must be set'</span>
        <span class="k">async</span> <span class="k">with</span> <span class="n">AsyncExitStack</span><span class="p">()</span> <span class="k">as</span> <span class="n">stack</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">lock</span><span class="p">:</span>
                <span class="k">await</span> <span class="n">stack</span><span class="o">.</span><span class="n">enter_async_context</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_lock</span><span class="p">())</span>
            <span class="n">snapshots</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">load_all</span><span class="p">()</span>
            <span class="n">snapshots</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">snapshot</span><span class="p">)</span>
            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="n">snapshots</span><span class="p">)</span>

    <span class="nd">@asynccontextmanager</span>
    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">_lock</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">timeout</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="mf">1.0</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AsyncIterator</span><span class="p">[</span><span class="kc">None</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Lock a file by checking and writing a `.pydantic-graph-persistence-lock` to it.</span>

<span class="sd">        Args:</span>
<span class="sd">            timeout: how long to wait for the lock</span>

<span class="sd">        Returns: an async context manager that holds the lock</span>
<span class="sd">        """</span>
        <span class="n">lock_file</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">json_file</span><span class="o">.</span><span class="n">parent</span> <span class="o">/</span> <span class="sa">f</span><span class="s1">'</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">json_file</span><span class="o">.</span><span class="n">name</span><span class="si">}</span><span class="s1">.pydantic-graph-persistence-lock'</span>
        <span class="n">lock_id</span> <span class="o">=</span> <span class="n">secrets</span><span class="o">.</span><span class="n">token_urlsafe</span><span class="p">()</span><span class="o">.</span><span class="n">encode</span><span class="p">()</span>
        <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">wait_for</span><span class="p">(</span><span class="n">_get_lock</span><span class="p">(</span><span class="n">lock_file</span><span class="p">,</span> <span class="n">lock_id</span><span class="p">),</span> <span class="n">timeout</span><span class="o">=</span><span class="n">timeout</span><span class="p">)</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="k">yield</span>
        <span class="k">finally</span><span class="p">:</span>
            <span class="k">await</span> <span class="n">_graph_utils</span><span class="o">.</span><span class="n">run_in_executor</span><span class="p">(</span><span class="n">lock_file</span><span class="o">.</span><span class="n">unlink</span><span class="p">,</span> <span class="n">missing_ok</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-attribute">



<h4 id="pydantic_graph.persistence.file.FileStatePersistence.json_file" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">json_file</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_48"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_48 > code"></button><code><span class="n">json_file</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="pathlib.Path" href="https://docs.python.org/3/library/pathlib.html#pathlib.Path">Path</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Path to the JSON file where the snapshots are stored.</p>
<p>You should use a different file for each graph run, but a single file should be reused for multiple
steps of the same run.</p>
<p>For example if you have a run ID of the form <code>run_123abc</code>, you might create a <code>FileStatePersistence</code> thus:</p>
<div class="language-py highlight"><pre id="__code_49"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_49 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pathlib</span><span class="w"> </span><span class="kn">import</span> <span class="n">Path</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_graph</span><span class="w"> </span><span class="kn">import</span> <span class="n">FullStatePersistence</span>

<span class="n">run_id</span> <span class="o">=</span> <span class="s1">'run_123abc'</span>
<span class="n">persistence</span> <span class="o">=</span> <span class="n">FullStatePersistence</span><span class="p">(</span><span class="n">Path</span><span class="p">(</span><span class="s1">'runs'</span><span class="p">)</span> <span class="o">/</span> <span class="sa">f</span><span class="s1">'</span><span class="si">{</span><span class="n">run_id</span><span class="si">}</span><span class="s1">.json'</span><span class="p">)</span>
</code></pre></div>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_graph.persistence.file.FileStatePersistence.should_set_types" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">should_set_types</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_50"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_50 > code"></button><code><span class="nf">should_set_types</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Whether types need to be set.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_graph/pydantic_graph/persistence/file.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">104</span>
<span class="normal">105</span>
<span class="normal">106</span></pre></div></td><td class="code"><div><pre id="__code_51"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_51 > code"></button><code><span class="k">def</span><span class="w"> </span><span class="nf">should_set_types</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Whether types need to be set."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_snapshots_type_adapter</span> <span class="ow">is</span> <span class="kc">None</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
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
    
    
    <script id="__config" type="application/json">{"base": "../../..", "features": ["search.suggest", "search.highlight", "content.tabs.link", "content.code.annotate", "content.code.copy", "content.code.select", "navigation.path", "navigation.indexes", "navigation.sections", "navigation.tracking", "toc.follow"], "search": "../../../assets/javascripts/workers/search.f8cc74c7.min.js", "translations": {"clipboard.copied": "Copied to clipboard", "clipboard.copy": "Copy to clipboard", "search.result.more.one": "1 more on this page", "search.result.more.other": "# more on this page", "search.result.none": "No matching documents", "search.result.one": "1 matching document", "search.result.other": "# matching documents", "search.result.placeholder": "Type to start searching", "search.result.term.missing": "Missing", "select.version": "Select version"}}</script>
    
    
      <script src="../../../assets/javascripts/bundle.f1b6f286.min.js"></script>
      
        <script src="/flarelytics/client.js"></script>
      
        <script src="https://cdn.jsdelivr.net/npm/algoliasearch@5.20.0/dist/lite/builds/browser.umd.js"></script>
      
        <script src="https://cdn.jsdelivr.net/npm/instantsearch.js@4.77.3/dist/instantsearch.production.min.js"></script>
      
        <script src="/javascripts/algolia-search.js"></script>
      
    
  <script id="init-glightbox">const lightbox = GLightbox({"touchNavigation": true, "loop": false, "zoomable": true, "draggable": true, "openEffect": "zoom", "closeEffect": "zoom", "slideEffect": "slide"});
document$.subscribe(() => { lightbox.reload() });
</script>
</body></html>