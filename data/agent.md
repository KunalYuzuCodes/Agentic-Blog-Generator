<!DOCTYPE html><html lang="en" class="js-focus-visible js" data-js-focus-visible=""><head>
    
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width,initial-scale=1">
      
        <meta name="description" content="Agent Framework / shim to use Pydantic with LLMs">
      
      
      
        <link rel="canonical" href="https://ai.pydantic.dev/api/agent/">
      
      
        <link rel="prev" href="../../examples/question-graph/">
      
      
        <link rel="next" href="../tools/">
      
      
      <link rel="icon" href="../../favicon.ico">
      <meta name="generator" content="mkdocs-1.6.1, mkdocs-material-9.6.5">
    
    
      
        <title>pydantic_ai.agent - PydanticAI</title>
      
    
    
      <link rel="stylesheet" href="../../assets/stylesheets/main.8608ea7d.min.css">
      
        
        <link rel="stylesheet" href="../../assets/stylesheets/palette.06af60db.min.css">
      
      


    
    
      
    
    
      
        
        
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,300i,400,400i,700,700i%7CRoboto+Mono:400,400i,700,700i&amp;display=fallback">
        <style>:root{--md-text-font:"Roboto";--md-code-font:"Roboto Mono"}</style>
      
    
    
      <link rel="stylesheet" href="../../assets/_mkdocstrings.css">
    
      <link rel="stylesheet" href="../../extra/tweaks.css">
    
    <script>__md_scope=new URL("../..",location),__md_hash=e=>[...e].reduce(((e,_)=>(e<<5)-e+_.charCodeAt(0)),0),__md_get=(e,_=localStorage,t=__md_scope)=>JSON.parse(_.getItem(t.pathname+"."+e)),__md_set=(e,_,t=localStorage,a=__md_scope)=>{try{t.setItem(a.pathname+"."+e,JSON.stringify(_))}catch(e){}}</script>
    
      

    
    
      
        <meta property="og:type" content="website">
      
        <meta property="og:title" content="pydantic_ai.agent - PydanticAI">
      
        <meta property="og:description" content="Agent Framework / shim to use Pydantic with LLMs">
      
        <meta property="og:image" content="https://ai.pydantic.dev/assets/images/social/api/agent.png">
      
        <meta property="og:image:type" content="image/png">
      
        <meta property="og:image:width" content="1200">
      
        <meta property="og:image:height" content="630">
      
        <meta property="og:url" content="https://ai.pydantic.dev/api/agent/">
      
        <meta name="twitter:card" content="summary_large_image">
      
        <meta name="twitter:title" content="pydantic_ai.agent - PydanticAI">
      
        <meta name="twitter:description" content="Agent Framework / shim to use Pydantic with LLMs">
      
        <meta name="twitter:image" content="https://ai.pydantic.dev/assets/images/social/api/agent.png">
      
    
    
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
      
        
        <a href="#pydantic_aiagent" class="md-skip">
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
            
              pydantic_ai.agent
            
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
            
              
                
  
  
    
  
  
  
    <li class="md-nav__item md-nav__item--active">
      
      <input class="md-nav__toggle md-toggle" type="checkbox" id="__toc">
      
      
        
      
      
        <label class="md-nav__link md-nav__link--active" for="__toc">
          
  
  <span class="md-ellipsis">
    pydantic_ai.agent
    
  </span>
  

          <span class="md-nav__icon md-icon"></span>
        </label>
      
      <a href="./" class="md-nav__link md-nav__link--active">
        
  
  <span class="md-ellipsis">
    pydantic_ai.agent
    
  </span>
  

      </a>
      
        

<nav class="md-nav md-nav--secondary" aria-label="Table of contents">
  
  
  
    
  
  
    <label class="md-nav__title" for="__toc">
      <span class="md-nav__icon md-icon"></span>
      Table of contents
    </label>
    <ul class="md-nav__list" data-md-component="toc">
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.agent" class="md-nav__link">
    <span class="md-ellipsis">
      agent
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.agent.Agent" class="md-nav__link">
    <span class="md-ellipsis">
      Agent
    </span>
  </a>
  
    <nav class="md-nav" aria-label="Agent">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.Agent.model" class="md-nav__link">
    <span class="md-ellipsis">
      model
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.Agent.__init__" class="md-nav__link">
    <span class="md-ellipsis">
      __init__
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.Agent.end_strategy" class="md-nav__link">
    <span class="md-ellipsis">
      end_strategy
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.Agent.name" class="md-nav__link">
    <span class="md-ellipsis">
      name
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.Agent.model_settings" class="md-nav__link">
    <span class="md-ellipsis">
      model_settings
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.Agent.result_type" class="md-nav__link">
    <span class="md-ellipsis">
      result_type
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.Agent.instrument" class="md-nav__link">
    <span class="md-ellipsis">
      instrument
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.Agent.instrument_all" class="md-nav__link">
    <span class="md-ellipsis">
      instrument_all
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.Agent.run" class="md-nav__link">
    <span class="md-ellipsis">
      run
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.Agent.iter" class="md-nav__link">
    <span class="md-ellipsis">
      iter
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.Agent.run_sync" class="md-nav__link">
    <span class="md-ellipsis">
      run_sync
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.Agent.run_stream" class="md-nav__link">
    <span class="md-ellipsis">
      run_stream
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.Agent.override" class="md-nav__link">
    <span class="md-ellipsis">
      override
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.Agent.system_prompt" class="md-nav__link">
    <span class="md-ellipsis">
      system_prompt
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.Agent.result_validator" class="md-nav__link">
    <span class="md-ellipsis">
      result_validator
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.Agent.tool" class="md-nav__link">
    <span class="md-ellipsis">
      tool
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.Agent.tool_plain" class="md-nav__link">
    <span class="md-ellipsis">
      tool_plain
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.Agent.is_model_request_node" class="md-nav__link">
    <span class="md-ellipsis">
      is_model_request_node
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.Agent.is_call_tools_node" class="md-nav__link">
    <span class="md-ellipsis">
      is_call_tools_node
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.Agent.is_user_prompt_node" class="md-nav__link">
    <span class="md-ellipsis">
      is_user_prompt_node
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.Agent.is_end_node" class="md-nav__link">
    <span class="md-ellipsis">
      is_end_node
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.Agent.run_mcp_servers" class="md-nav__link">
    <span class="md-ellipsis">
      run_mcp_servers
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.agent.AgentRun" class="md-nav__link">
    <span class="md-ellipsis">
      AgentRun
    </span>
  </a>
  
    <nav class="md-nav" aria-label="AgentRun">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.AgentRun.ctx" class="md-nav__link">
    <span class="md-ellipsis">
      ctx
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.AgentRun.next_node" class="md-nav__link">
    <span class="md-ellipsis">
      next_node
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.AgentRun.result" class="md-nav__link">
    <span class="md-ellipsis">
      result
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.AgentRun.__aiter__" class="md-nav__link">
    <span class="md-ellipsis">
      __aiter__
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.AgentRun.__anext__" class="md-nav__link">
    <span class="md-ellipsis">
      __anext__
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.AgentRun.next" class="md-nav__link">
    <span class="md-ellipsis">
      next
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.AgentRun.usage" class="md-nav__link">
    <span class="md-ellipsis">
      usage
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.agent.AgentRunResult" class="md-nav__link">
    <span class="md-ellipsis">
      AgentRunResult
    </span>
  </a>
  
    <nav class="md-nav" aria-label="AgentRunResult">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.AgentRunResult.all_messages" class="md-nav__link">
    <span class="md-ellipsis">
      all_messages
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.AgentRunResult.all_messages_json" class="md-nav__link">
    <span class="md-ellipsis">
      all_messages_json
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.AgentRunResult.new_messages" class="md-nav__link">
    <span class="md-ellipsis">
      new_messages
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.AgentRunResult.new_messages_json" class="md-nav__link">
    <span class="md-ellipsis">
      new_messages_json
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.AgentRunResult.usage" class="md-nav__link">
    <span class="md-ellipsis">
      usage
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.agent.EndStrategy" class="md-nav__link">
    <span class="md-ellipsis">
      EndStrategy
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.agent.RunResultDataT" class="md-nav__link">
    <span class="md-ellipsis">
      RunResultDataT
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.agent.capture_run_messages" class="md-nav__link">
    <span class="md-ellipsis">
      capture_run_messages
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.agent.InstrumentationSettings" class="md-nav__link">
    <span class="md-ellipsis">
      InstrumentationSettings
    </span>
  </a>
  
    <nav class="md-nav" aria-label="InstrumentationSettings">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.InstrumentationSettings.__init__" class="md-nav__link">
    <span class="md-ellipsis">
      __init__
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
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../messages/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.messages
    
  </span>
  

      </a>
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
  <a href="#pydantic_ai.agent" class="md-nav__link">
    <span class="md-ellipsis">
      agent
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.agent.Agent" class="md-nav__link">
    <span class="md-ellipsis">
      Agent
    </span>
  </a>
  
    <nav class="md-nav" aria-label="Agent">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.Agent.model" class="md-nav__link">
    <span class="md-ellipsis">
      model
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.Agent.__init__" class="md-nav__link">
    <span class="md-ellipsis">
      __init__
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.Agent.end_strategy" class="md-nav__link">
    <span class="md-ellipsis">
      end_strategy
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.Agent.name" class="md-nav__link">
    <span class="md-ellipsis">
      name
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.Agent.model_settings" class="md-nav__link">
    <span class="md-ellipsis">
      model_settings
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.Agent.result_type" class="md-nav__link">
    <span class="md-ellipsis">
      result_type
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.Agent.instrument" class="md-nav__link">
    <span class="md-ellipsis">
      instrument
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.Agent.instrument_all" class="md-nav__link">
    <span class="md-ellipsis">
      instrument_all
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.Agent.run" class="md-nav__link">
    <span class="md-ellipsis">
      run
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.Agent.iter" class="md-nav__link">
    <span class="md-ellipsis">
      iter
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.Agent.run_sync" class="md-nav__link">
    <span class="md-ellipsis">
      run_sync
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.Agent.run_stream" class="md-nav__link">
    <span class="md-ellipsis">
      run_stream
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.Agent.override" class="md-nav__link">
    <span class="md-ellipsis">
      override
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.Agent.system_prompt" class="md-nav__link">
    <span class="md-ellipsis">
      system_prompt
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.Agent.result_validator" class="md-nav__link">
    <span class="md-ellipsis">
      result_validator
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.Agent.tool" class="md-nav__link">
    <span class="md-ellipsis">
      tool
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.Agent.tool_plain" class="md-nav__link">
    <span class="md-ellipsis">
      tool_plain
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.Agent.is_model_request_node" class="md-nav__link">
    <span class="md-ellipsis">
      is_model_request_node
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.Agent.is_call_tools_node" class="md-nav__link">
    <span class="md-ellipsis">
      is_call_tools_node
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.Agent.is_user_prompt_node" class="md-nav__link">
    <span class="md-ellipsis">
      is_user_prompt_node
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.Agent.is_end_node" class="md-nav__link">
    <span class="md-ellipsis">
      is_end_node
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.Agent.run_mcp_servers" class="md-nav__link">
    <span class="md-ellipsis">
      run_mcp_servers
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.agent.AgentRun" class="md-nav__link">
    <span class="md-ellipsis">
      AgentRun
    </span>
  </a>
  
    <nav class="md-nav" aria-label="AgentRun">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.AgentRun.ctx" class="md-nav__link">
    <span class="md-ellipsis">
      ctx
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.AgentRun.next_node" class="md-nav__link">
    <span class="md-ellipsis">
      next_node
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.AgentRun.result" class="md-nav__link">
    <span class="md-ellipsis">
      result
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.AgentRun.__aiter__" class="md-nav__link">
    <span class="md-ellipsis">
      __aiter__
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.AgentRun.__anext__" class="md-nav__link">
    <span class="md-ellipsis">
      __anext__
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.AgentRun.next" class="md-nav__link">
    <span class="md-ellipsis">
      next
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.AgentRun.usage" class="md-nav__link">
    <span class="md-ellipsis">
      usage
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.agent.AgentRunResult" class="md-nav__link">
    <span class="md-ellipsis">
      AgentRunResult
    </span>
  </a>
  
    <nav class="md-nav" aria-label="AgentRunResult">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.AgentRunResult.all_messages" class="md-nav__link">
    <span class="md-ellipsis">
      all_messages
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.AgentRunResult.all_messages_json" class="md-nav__link">
    <span class="md-ellipsis">
      all_messages_json
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.AgentRunResult.new_messages" class="md-nav__link">
    <span class="md-ellipsis">
      new_messages
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.AgentRunResult.new_messages_json" class="md-nav__link">
    <span class="md-ellipsis">
      new_messages_json
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.AgentRunResult.usage" class="md-nav__link">
    <span class="md-ellipsis">
      usage
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.agent.EndStrategy" class="md-nav__link">
    <span class="md-ellipsis">
      EndStrategy
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.agent.RunResultDataT" class="md-nav__link">
    <span class="md-ellipsis">
      RunResultDataT
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.agent.capture_run_messages" class="md-nav__link">
    <span class="md-ellipsis">
      capture_run_messages
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.agent.InstrumentationSettings" class="md-nav__link">
    <span class="md-ellipsis">
      InstrumentationSettings
    </span>
  </a>
  
    <nav class="md-nav" aria-label="InstrumentationSettings">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.agent.InstrumentationSettings.__init__" class="md-nav__link">
    <span class="md-ellipsis">
      __init__
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
                
                  


  
  


<h1 id="pydantic_aiagent"><code>pydantic_ai.agent</code></h1>


<div class="doc doc-object doc-module">



<a id="pydantic_ai.agent"></a>
    <div class="doc doc-contents first">








  <div class="doc doc-children">







<div class="doc doc-object doc-class">



<h3 id="pydantic_ai.agent.Agent" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">Agent</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">
            <p class="doc doc-class-bases">
              Bases: <code><a class="autorefs autorefs-external" title="typing.Generic" href="https://docs.python.org/3/library/typing.html#typing.Generic">Generic</a>[<a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a>, <a class="autorefs autorefs-internal" title="pydantic_ai.result.ResultDataT" href="../result/#pydantic_ai.result.ResultDataT">ResultDataT</a>]</code></p>


        <p>Class for defining "agents" - a way to have a specific type of "conversation" with an LLM.</p>
<p>Agents are generic in the dependency type they take <a class="autorefs autorefs-internal" href="../tools/#pydantic_ai.tools.AgentDepsT"><code>AgentDepsT</code></a>
and the result data type they return, <a class="autorefs autorefs-internal" href="../result/#pydantic_ai.result.ResultDataT"><code>ResultDataT</code></a>.</p>
<p>By default, if neither generic parameter is customised, agents have type <code>Agent[None, str]</code>.</p>
<p>Minimal usage example:</p>
<div class="language-python highlight"><pre id="__code_0"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_0 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>

<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="s1">'openai:gpt-4o'</span><span class="p">)</span>
<span class="n">result</span> <span class="o">=</span> <span class="n">agent</span><span class="o">.</span><span class="n">run_sync</span><span class="p">(</span><span class="s1">'What is the capital of France?'</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">result</span><span class="o">.</span><span class="n">data</span><span class="p">)</span>
<span class="c1">#&gt; Paris</span>
</code></pre></div>






              <details class="quote">
                <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/agent.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">  75</span>
<span class="normal">  76</span>
<span class="normal">  77</span>
<span class="normal">  78</span>
<span class="normal">  79</span>
<span class="normal">  80</span>
<span class="normal">  81</span>
<span class="normal">  82</span>
<span class="normal">  83</span>
<span class="normal">  84</span>
<span class="normal">  85</span>
<span class="normal">  86</span>
<span class="normal">  87</span>
<span class="normal">  88</span>
<span class="normal">  89</span>
<span class="normal">  90</span>
<span class="normal">  91</span>
<span class="normal">  92</span>
<span class="normal">  93</span>
<span class="normal">  94</span>
<span class="normal">  95</span>
<span class="normal">  96</span>
<span class="normal">  97</span>
<span class="normal">  98</span>
<span class="normal">  99</span>
<span class="normal"> 100</span>
<span class="normal"> 101</span>
<span class="normal"> 102</span>
<span class="normal"> 103</span>
<span class="normal"> 104</span>
<span class="normal"> 105</span>
<span class="normal"> 106</span>
<span class="normal"> 107</span>
<span class="normal"> 108</span>
<span class="normal"> 109</span>
<span class="normal"> 110</span>
<span class="normal"> 111</span>
<span class="normal"> 112</span>
<span class="normal"> 113</span>
<span class="normal"> 114</span>
<span class="normal"> 115</span>
<span class="normal"> 116</span>
<span class="normal"> 117</span>
<span class="normal"> 118</span>
<span class="normal"> 119</span>
<span class="normal"> 120</span>
<span class="normal"> 121</span>
<span class="normal"> 122</span>
<span class="normal"> 123</span>
<span class="normal"> 124</span>
<span class="normal"> 125</span>
<span class="normal"> 126</span>
<span class="normal"> 127</span>
<span class="normal"> 128</span>
<span class="normal"> 129</span>
<span class="normal"> 130</span>
<span class="normal"> 131</span>
<span class="normal"> 132</span>
<span class="normal"> 133</span>
<span class="normal"> 134</span>
<span class="normal"> 135</span>
<span class="normal"> 136</span>
<span class="normal"> 137</span>
<span class="normal"> 138</span>
<span class="normal"> 139</span>
<span class="normal"> 140</span>
<span class="normal"> 141</span>
<span class="normal"> 142</span>
<span class="normal"> 143</span>
<span class="normal"> 144</span>
<span class="normal"> 145</span>
<span class="normal"> 146</span>
<span class="normal"> 147</span>
<span class="normal"> 148</span>
<span class="normal"> 149</span>
<span class="normal"> 150</span>
<span class="normal"> 151</span>
<span class="normal"> 152</span>
<span class="normal"> 153</span>
<span class="normal"> 154</span>
<span class="normal"> 155</span>
<span class="normal"> 156</span>
<span class="normal"> 157</span>
<span class="normal"> 158</span>
<span class="normal"> 159</span>
<span class="normal"> 160</span>
<span class="normal"> 161</span>
<span class="normal"> 162</span>
<span class="normal"> 163</span>
<span class="normal"> 164</span>
<span class="normal"> 165</span>
<span class="normal"> 166</span>
<span class="normal"> 167</span>
<span class="normal"> 168</span>
<span class="normal"> 169</span>
<span class="normal"> 170</span>
<span class="normal"> 171</span>
<span class="normal"> 172</span>
<span class="normal"> 173</span>
<span class="normal"> 174</span>
<span class="normal"> 175</span>
<span class="normal"> 176</span>
<span class="normal"> 177</span>
<span class="normal"> 178</span>
<span class="normal"> 179</span>
<span class="normal"> 180</span>
<span class="normal"> 181</span>
<span class="normal"> 182</span>
<span class="normal"> 183</span>
<span class="normal"> 184</span>
<span class="normal"> 185</span>
<span class="normal"> 186</span>
<span class="normal"> 187</span>
<span class="normal"> 188</span>
<span class="normal"> 189</span>
<span class="normal"> 190</span>
<span class="normal"> 191</span>
<span class="normal"> 192</span>
<span class="normal"> 193</span>
<span class="normal"> 194</span>
<span class="normal"> 195</span>
<span class="normal"> 196</span>
<span class="normal"> 197</span>
<span class="normal"> 198</span>
<span class="normal"> 199</span>
<span class="normal"> 200</span>
<span class="normal"> 201</span>
<span class="normal"> 202</span>
<span class="normal"> 203</span>
<span class="normal"> 204</span>
<span class="normal"> 205</span>
<span class="normal"> 206</span>
<span class="normal"> 207</span>
<span class="normal"> 208</span>
<span class="normal"> 209</span>
<span class="normal"> 210</span>
<span class="normal"> 211</span>
<span class="normal"> 212</span>
<span class="normal"> 213</span>
<span class="normal"> 214</span>
<span class="normal"> 215</span>
<span class="normal"> 216</span>
<span class="normal"> 217</span>
<span class="normal"> 218</span>
<span class="normal"> 219</span>
<span class="normal"> 220</span>
<span class="normal"> 221</span>
<span class="normal"> 222</span>
<span class="normal"> 223</span>
<span class="normal"> 224</span>
<span class="normal"> 225</span>
<span class="normal"> 226</span>
<span class="normal"> 227</span>
<span class="normal"> 228</span>
<span class="normal"> 229</span>
<span class="normal"> 230</span>
<span class="normal"> 231</span>
<span class="normal"> 232</span>
<span class="normal"> 233</span>
<span class="normal"> 234</span>
<span class="normal"> 235</span>
<span class="normal"> 236</span>
<span class="normal"> 237</span>
<span class="normal"> 238</span>
<span class="normal"> 239</span>
<span class="normal"> 240</span>
<span class="normal"> 241</span>
<span class="normal"> 242</span>
<span class="normal"> 243</span>
<span class="normal"> 244</span>
<span class="normal"> 245</span>
<span class="normal"> 246</span>
<span class="normal"> 247</span>
<span class="normal"> 248</span>
<span class="normal"> 249</span>
<span class="normal"> 250</span>
<span class="normal"> 251</span>
<span class="normal"> 252</span>
<span class="normal"> 253</span>
<span class="normal"> 254</span>
<span class="normal"> 255</span>
<span class="normal"> 256</span>
<span class="normal"> 257</span>
<span class="normal"> 258</span>
<span class="normal"> 259</span>
<span class="normal"> 260</span>
<span class="normal"> 261</span>
<span class="normal"> 262</span>
<span class="normal"> 263</span>
<span class="normal"> 264</span>
<span class="normal"> 265</span>
<span class="normal"> 266</span>
<span class="normal"> 267</span>
<span class="normal"> 268</span>
<span class="normal"> 269</span>
<span class="normal"> 270</span>
<span class="normal"> 271</span>
<span class="normal"> 272</span>
<span class="normal"> 273</span>
<span class="normal"> 274</span>
<span class="normal"> 275</span>
<span class="normal"> 276</span>
<span class="normal"> 277</span>
<span class="normal"> 278</span>
<span class="normal"> 279</span>
<span class="normal"> 280</span>
<span class="normal"> 281</span>
<span class="normal"> 282</span>
<span class="normal"> 283</span>
<span class="normal"> 284</span>
<span class="normal"> 285</span>
<span class="normal"> 286</span>
<span class="normal"> 287</span>
<span class="normal"> 288</span>
<span class="normal"> 289</span>
<span class="normal"> 290</span>
<span class="normal"> 291</span>
<span class="normal"> 292</span>
<span class="normal"> 293</span>
<span class="normal"> 294</span>
<span class="normal"> 295</span>
<span class="normal"> 296</span>
<span class="normal"> 297</span>
<span class="normal"> 298</span>
<span class="normal"> 299</span>
<span class="normal"> 300</span>
<span class="normal"> 301</span>
<span class="normal"> 302</span>
<span class="normal"> 303</span>
<span class="normal"> 304</span>
<span class="normal"> 305</span>
<span class="normal"> 306</span>
<span class="normal"> 307</span>
<span class="normal"> 308</span>
<span class="normal"> 309</span>
<span class="normal"> 310</span>
<span class="normal"> 311</span>
<span class="normal"> 312</span>
<span class="normal"> 313</span>
<span class="normal"> 314</span>
<span class="normal"> 315</span>
<span class="normal"> 316</span>
<span class="normal"> 317</span>
<span class="normal"> 318</span>
<span class="normal"> 319</span>
<span class="normal"> 320</span>
<span class="normal"> 321</span>
<span class="normal"> 322</span>
<span class="normal"> 323</span>
<span class="normal"> 324</span>
<span class="normal"> 325</span>
<span class="normal"> 326</span>
<span class="normal"> 327</span>
<span class="normal"> 328</span>
<span class="normal"> 329</span>
<span class="normal"> 330</span>
<span class="normal"> 331</span>
<span class="normal"> 332</span>
<span class="normal"> 333</span>
<span class="normal"> 334</span>
<span class="normal"> 335</span>
<span class="normal"> 336</span>
<span class="normal"> 337</span>
<span class="normal"> 338</span>
<span class="normal"> 339</span>
<span class="normal"> 340</span>
<span class="normal"> 341</span>
<span class="normal"> 342</span>
<span class="normal"> 343</span>
<span class="normal"> 344</span>
<span class="normal"> 345</span>
<span class="normal"> 346</span>
<span class="normal"> 347</span>
<span class="normal"> 348</span>
<span class="normal"> 349</span>
<span class="normal"> 350</span>
<span class="normal"> 351</span>
<span class="normal"> 352</span>
<span class="normal"> 353</span>
<span class="normal"> 354</span>
<span class="normal"> 355</span>
<span class="normal"> 356</span>
<span class="normal"> 357</span>
<span class="normal"> 358</span>
<span class="normal"> 359</span>
<span class="normal"> 360</span>
<span class="normal"> 361</span>
<span class="normal"> 362</span>
<span class="normal"> 363</span>
<span class="normal"> 364</span>
<span class="normal"> 365</span>
<span class="normal"> 366</span>
<span class="normal"> 367</span>
<span class="normal"> 368</span>
<span class="normal"> 369</span>
<span class="normal"> 370</span>
<span class="normal"> 371</span>
<span class="normal"> 372</span>
<span class="normal"> 373</span>
<span class="normal"> 374</span>
<span class="normal"> 375</span>
<span class="normal"> 376</span>
<span class="normal"> 377</span>
<span class="normal"> 378</span>
<span class="normal"> 379</span>
<span class="normal"> 380</span>
<span class="normal"> 381</span>
<span class="normal"> 382</span>
<span class="normal"> 383</span>
<span class="normal"> 384</span>
<span class="normal"> 385</span>
<span class="normal"> 386</span>
<span class="normal"> 387</span>
<span class="normal"> 388</span>
<span class="normal"> 389</span>
<span class="normal"> 390</span>
<span class="normal"> 391</span>
<span class="normal"> 392</span>
<span class="normal"> 393</span>
<span class="normal"> 394</span>
<span class="normal"> 395</span>
<span class="normal"> 396</span>
<span class="normal"> 397</span>
<span class="normal"> 398</span>
<span class="normal"> 399</span>
<span class="normal"> 400</span>
<span class="normal"> 401</span>
<span class="normal"> 402</span>
<span class="normal"> 403</span>
<span class="normal"> 404</span>
<span class="normal"> 405</span>
<span class="normal"> 406</span>
<span class="normal"> 407</span>
<span class="normal"> 408</span>
<span class="normal"> 409</span>
<span class="normal"> 410</span>
<span class="normal"> 411</span>
<span class="normal"> 412</span>
<span class="normal"> 413</span>
<span class="normal"> 414</span>
<span class="normal"> 415</span>
<span class="normal"> 416</span>
<span class="normal"> 417</span>
<span class="normal"> 418</span>
<span class="normal"> 419</span>
<span class="normal"> 420</span>
<span class="normal"> 421</span>
<span class="normal"> 422</span>
<span class="normal"> 423</span>
<span class="normal"> 424</span>
<span class="normal"> 425</span>
<span class="normal"> 426</span>
<span class="normal"> 427</span>
<span class="normal"> 428</span>
<span class="normal"> 429</span>
<span class="normal"> 430</span>
<span class="normal"> 431</span>
<span class="normal"> 432</span>
<span class="normal"> 433</span>
<span class="normal"> 434</span>
<span class="normal"> 435</span>
<span class="normal"> 436</span>
<span class="normal"> 437</span>
<span class="normal"> 438</span>
<span class="normal"> 439</span>
<span class="normal"> 440</span>
<span class="normal"> 441</span>
<span class="normal"> 442</span>
<span class="normal"> 443</span>
<span class="normal"> 444</span>
<span class="normal"> 445</span>
<span class="normal"> 446</span>
<span class="normal"> 447</span>
<span class="normal"> 448</span>
<span class="normal"> 449</span>
<span class="normal"> 450</span>
<span class="normal"> 451</span>
<span class="normal"> 452</span>
<span class="normal"> 453</span>
<span class="normal"> 454</span>
<span class="normal"> 455</span>
<span class="normal"> 456</span>
<span class="normal"> 457</span>
<span class="normal"> 458</span>
<span class="normal"> 459</span>
<span class="normal"> 460</span>
<span class="normal"> 461</span>
<span class="normal"> 462</span>
<span class="normal"> 463</span>
<span class="normal"> 464</span>
<span class="normal"> 465</span>
<span class="normal"> 466</span>
<span class="normal"> 467</span>
<span class="normal"> 468</span>
<span class="normal"> 469</span>
<span class="normal"> 470</span>
<span class="normal"> 471</span>
<span class="normal"> 472</span>
<span class="normal"> 473</span>
<span class="normal"> 474</span>
<span class="normal"> 475</span>
<span class="normal"> 476</span>
<span class="normal"> 477</span>
<span class="normal"> 478</span>
<span class="normal"> 479</span>
<span class="normal"> 480</span>
<span class="normal"> 481</span>
<span class="normal"> 482</span>
<span class="normal"> 483</span>
<span class="normal"> 484</span>
<span class="normal"> 485</span>
<span class="normal"> 486</span>
<span class="normal"> 487</span>
<span class="normal"> 488</span>
<span class="normal"> 489</span>
<span class="normal"> 490</span>
<span class="normal"> 491</span>
<span class="normal"> 492</span>
<span class="normal"> 493</span>
<span class="normal"> 494</span>
<span class="normal"> 495</span>
<span class="normal"> 496</span>
<span class="normal"> 497</span>
<span class="normal"> 498</span>
<span class="normal"> 499</span>
<span class="normal"> 500</span>
<span class="normal"> 501</span>
<span class="normal"> 502</span>
<span class="normal"> 503</span>
<span class="normal"> 504</span>
<span class="normal"> 505</span>
<span class="normal"> 506</span>
<span class="normal"> 507</span>
<span class="normal"> 508</span>
<span class="normal"> 509</span>
<span class="normal"> 510</span>
<span class="normal"> 511</span>
<span class="normal"> 512</span>
<span class="normal"> 513</span>
<span class="normal"> 514</span>
<span class="normal"> 515</span>
<span class="normal"> 516</span>
<span class="normal"> 517</span>
<span class="normal"> 518</span>
<span class="normal"> 519</span>
<span class="normal"> 520</span>
<span class="normal"> 521</span>
<span class="normal"> 522</span>
<span class="normal"> 523</span>
<span class="normal"> 524</span>
<span class="normal"> 525</span>
<span class="normal"> 526</span>
<span class="normal"> 527</span>
<span class="normal"> 528</span>
<span class="normal"> 529</span>
<span class="normal"> 530</span>
<span class="normal"> 531</span>
<span class="normal"> 532</span>
<span class="normal"> 533</span>
<span class="normal"> 534</span>
<span class="normal"> 535</span>
<span class="normal"> 536</span>
<span class="normal"> 537</span>
<span class="normal"> 538</span>
<span class="normal"> 539</span>
<span class="normal"> 540</span>
<span class="normal"> 541</span>
<span class="normal"> 542</span>
<span class="normal"> 543</span>
<span class="normal"> 544</span>
<span class="normal"> 545</span>
<span class="normal"> 546</span>
<span class="normal"> 547</span>
<span class="normal"> 548</span>
<span class="normal"> 549</span>
<span class="normal"> 550</span>
<span class="normal"> 551</span>
<span class="normal"> 552</span>
<span class="normal"> 553</span>
<span class="normal"> 554</span>
<span class="normal"> 555</span>
<span class="normal"> 556</span>
<span class="normal"> 557</span>
<span class="normal"> 558</span>
<span class="normal"> 559</span>
<span class="normal"> 560</span>
<span class="normal"> 561</span>
<span class="normal"> 562</span>
<span class="normal"> 563</span>
<span class="normal"> 564</span>
<span class="normal"> 565</span>
<span class="normal"> 566</span>
<span class="normal"> 567</span>
<span class="normal"> 568</span>
<span class="normal"> 569</span>
<span class="normal"> 570</span>
<span class="normal"> 571</span>
<span class="normal"> 572</span>
<span class="normal"> 573</span>
<span class="normal"> 574</span>
<span class="normal"> 575</span>
<span class="normal"> 576</span>
<span class="normal"> 577</span>
<span class="normal"> 578</span>
<span class="normal"> 579</span>
<span class="normal"> 580</span>
<span class="normal"> 581</span>
<span class="normal"> 582</span>
<span class="normal"> 583</span>
<span class="normal"> 584</span>
<span class="normal"> 585</span>
<span class="normal"> 586</span>
<span class="normal"> 587</span>
<span class="normal"> 588</span>
<span class="normal"> 589</span>
<span class="normal"> 590</span>
<span class="normal"> 591</span>
<span class="normal"> 592</span>
<span class="normal"> 593</span>
<span class="normal"> 594</span>
<span class="normal"> 595</span>
<span class="normal"> 596</span>
<span class="normal"> 597</span>
<span class="normal"> 598</span>
<span class="normal"> 599</span>
<span class="normal"> 600</span>
<span class="normal"> 601</span>
<span class="normal"> 602</span>
<span class="normal"> 603</span>
<span class="normal"> 604</span>
<span class="normal"> 605</span>
<span class="normal"> 606</span>
<span class="normal"> 607</span>
<span class="normal"> 608</span>
<span class="normal"> 609</span>
<span class="normal"> 610</span>
<span class="normal"> 611</span>
<span class="normal"> 612</span>
<span class="normal"> 613</span>
<span class="normal"> 614</span>
<span class="normal"> 615</span>
<span class="normal"> 616</span>
<span class="normal"> 617</span>
<span class="normal"> 618</span>
<span class="normal"> 619</span>
<span class="normal"> 620</span>
<span class="normal"> 621</span>
<span class="normal"> 622</span>
<span class="normal"> 623</span>
<span class="normal"> 624</span>
<span class="normal"> 625</span>
<span class="normal"> 626</span>
<span class="normal"> 627</span>
<span class="normal"> 628</span>
<span class="normal"> 629</span>
<span class="normal"> 630</span>
<span class="normal"> 631</span>
<span class="normal"> 632</span>
<span class="normal"> 633</span>
<span class="normal"> 634</span>
<span class="normal"> 635</span>
<span class="normal"> 636</span>
<span class="normal"> 637</span>
<span class="normal"> 638</span>
<span class="normal"> 639</span>
<span class="normal"> 640</span>
<span class="normal"> 641</span>
<span class="normal"> 642</span>
<span class="normal"> 643</span>
<span class="normal"> 644</span>
<span class="normal"> 645</span>
<span class="normal"> 646</span>
<span class="normal"> 647</span>
<span class="normal"> 648</span>
<span class="normal"> 649</span>
<span class="normal"> 650</span>
<span class="normal"> 651</span>
<span class="normal"> 652</span>
<span class="normal"> 653</span>
<span class="normal"> 654</span>
<span class="normal"> 655</span>
<span class="normal"> 656</span>
<span class="normal"> 657</span>
<span class="normal"> 658</span>
<span class="normal"> 659</span>
<span class="normal"> 660</span>
<span class="normal"> 661</span>
<span class="normal"> 662</span>
<span class="normal"> 663</span>
<span class="normal"> 664</span>
<span class="normal"> 665</span>
<span class="normal"> 666</span>
<span class="normal"> 667</span>
<span class="normal"> 668</span>
<span class="normal"> 669</span>
<span class="normal"> 670</span>
<span class="normal"> 671</span>
<span class="normal"> 672</span>
<span class="normal"> 673</span>
<span class="normal"> 674</span>
<span class="normal"> 675</span>
<span class="normal"> 676</span>
<span class="normal"> 677</span>
<span class="normal"> 678</span>
<span class="normal"> 679</span>
<span class="normal"> 680</span>
<span class="normal"> 681</span>
<span class="normal"> 682</span>
<span class="normal"> 683</span>
<span class="normal"> 684</span>
<span class="normal"> 685</span>
<span class="normal"> 686</span>
<span class="normal"> 687</span>
<span class="normal"> 688</span>
<span class="normal"> 689</span>
<span class="normal"> 690</span>
<span class="normal"> 691</span>
<span class="normal"> 692</span>
<span class="normal"> 693</span>
<span class="normal"> 694</span>
<span class="normal"> 695</span>
<span class="normal"> 696</span>
<span class="normal"> 697</span>
<span class="normal"> 698</span>
<span class="normal"> 699</span>
<span class="normal"> 700</span>
<span class="normal"> 701</span>
<span class="normal"> 702</span>
<span class="normal"> 703</span>
<span class="normal"> 704</span>
<span class="normal"> 705</span>
<span class="normal"> 706</span>
<span class="normal"> 707</span>
<span class="normal"> 708</span>
<span class="normal"> 709</span>
<span class="normal"> 710</span>
<span class="normal"> 711</span>
<span class="normal"> 712</span>
<span class="normal"> 713</span>
<span class="normal"> 714</span>
<span class="normal"> 715</span>
<span class="normal"> 716</span>
<span class="normal"> 717</span>
<span class="normal"> 718</span>
<span class="normal"> 719</span>
<span class="normal"> 720</span>
<span class="normal"> 721</span>
<span class="normal"> 722</span>
<span class="normal"> 723</span>
<span class="normal"> 724</span>
<span class="normal"> 725</span>
<span class="normal"> 726</span>
<span class="normal"> 727</span>
<span class="normal"> 728</span>
<span class="normal"> 729</span>
<span class="normal"> 730</span>
<span class="normal"> 731</span>
<span class="normal"> 732</span>
<span class="normal"> 733</span>
<span class="normal"> 734</span>
<span class="normal"> 735</span>
<span class="normal"> 736</span>
<span class="normal"> 737</span>
<span class="normal"> 738</span>
<span class="normal"> 739</span>
<span class="normal"> 740</span>
<span class="normal"> 741</span>
<span class="normal"> 742</span>
<span class="normal"> 743</span>
<span class="normal"> 744</span>
<span class="normal"> 745</span>
<span class="normal"> 746</span>
<span class="normal"> 747</span>
<span class="normal"> 748</span>
<span class="normal"> 749</span>
<span class="normal"> 750</span>
<span class="normal"> 751</span>
<span class="normal"> 752</span>
<span class="normal"> 753</span>
<span class="normal"> 754</span>
<span class="normal"> 755</span>
<span class="normal"> 756</span>
<span class="normal"> 757</span>
<span class="normal"> 758</span>
<span class="normal"> 759</span>
<span class="normal"> 760</span>
<span class="normal"> 761</span>
<span class="normal"> 762</span>
<span class="normal"> 763</span>
<span class="normal"> 764</span>
<span class="normal"> 765</span>
<span class="normal"> 766</span>
<span class="normal"> 767</span>
<span class="normal"> 768</span>
<span class="normal"> 769</span>
<span class="normal"> 770</span>
<span class="normal"> 771</span>
<span class="normal"> 772</span>
<span class="normal"> 773</span>
<span class="normal"> 774</span>
<span class="normal"> 775</span>
<span class="normal"> 776</span>
<span class="normal"> 777</span>
<span class="normal"> 778</span>
<span class="normal"> 779</span>
<span class="normal"> 780</span>
<span class="normal"> 781</span>
<span class="normal"> 782</span>
<span class="normal"> 783</span>
<span class="normal"> 784</span>
<span class="normal"> 785</span>
<span class="normal"> 786</span>
<span class="normal"> 787</span>
<span class="normal"> 788</span>
<span class="normal"> 789</span>
<span class="normal"> 790</span>
<span class="normal"> 791</span>
<span class="normal"> 792</span>
<span class="normal"> 793</span>
<span class="normal"> 794</span>
<span class="normal"> 795</span>
<span class="normal"> 796</span>
<span class="normal"> 797</span>
<span class="normal"> 798</span>
<span class="normal"> 799</span>
<span class="normal"> 800</span>
<span class="normal"> 801</span>
<span class="normal"> 802</span>
<span class="normal"> 803</span>
<span class="normal"> 804</span>
<span class="normal"> 805</span>
<span class="normal"> 806</span>
<span class="normal"> 807</span>
<span class="normal"> 808</span>
<span class="normal"> 809</span>
<span class="normal"> 810</span>
<span class="normal"> 811</span>
<span class="normal"> 812</span>
<span class="normal"> 813</span>
<span class="normal"> 814</span>
<span class="normal"> 815</span>
<span class="normal"> 816</span>
<span class="normal"> 817</span>
<span class="normal"> 818</span>
<span class="normal"> 819</span>
<span class="normal"> 820</span>
<span class="normal"> 821</span>
<span class="normal"> 822</span>
<span class="normal"> 823</span>
<span class="normal"> 824</span>
<span class="normal"> 825</span>
<span class="normal"> 826</span>
<span class="normal"> 827</span>
<span class="normal"> 828</span>
<span class="normal"> 829</span>
<span class="normal"> 830</span>
<span class="normal"> 831</span>
<span class="normal"> 832</span>
<span class="normal"> 833</span>
<span class="normal"> 834</span>
<span class="normal"> 835</span>
<span class="normal"> 836</span>
<span class="normal"> 837</span>
<span class="normal"> 838</span>
<span class="normal"> 839</span>
<span class="normal"> 840</span>
<span class="normal"> 841</span>
<span class="normal"> 842</span>
<span class="normal"> 843</span>
<span class="normal"> 844</span>
<span class="normal"> 845</span>
<span class="normal"> 846</span>
<span class="normal"> 847</span>
<span class="normal"> 848</span>
<span class="normal"> 849</span>
<span class="normal"> 850</span>
<span class="normal"> 851</span>
<span class="normal"> 852</span>
<span class="normal"> 853</span>
<span class="normal"> 854</span>
<span class="normal"> 855</span>
<span class="normal"> 856</span>
<span class="normal"> 857</span>
<span class="normal"> 858</span>
<span class="normal"> 859</span>
<span class="normal"> 860</span>
<span class="normal"> 861</span>
<span class="normal"> 862</span>
<span class="normal"> 863</span>
<span class="normal"> 864</span>
<span class="normal"> 865</span>
<span class="normal"> 866</span>
<span class="normal"> 867</span>
<span class="normal"> 868</span>
<span class="normal"> 869</span>
<span class="normal"> 870</span>
<span class="normal"> 871</span>
<span class="normal"> 872</span>
<span class="normal"> 873</span>
<span class="normal"> 874</span>
<span class="normal"> 875</span>
<span class="normal"> 876</span>
<span class="normal"> 877</span>
<span class="normal"> 878</span>
<span class="normal"> 879</span>
<span class="normal"> 880</span>
<span class="normal"> 881</span>
<span class="normal"> 882</span>
<span class="normal"> 883</span>
<span class="normal"> 884</span>
<span class="normal"> 885</span>
<span class="normal"> 886</span>
<span class="normal"> 887</span>
<span class="normal"> 888</span>
<span class="normal"> 889</span>
<span class="normal"> 890</span>
<span class="normal"> 891</span>
<span class="normal"> 892</span>
<span class="normal"> 893</span>
<span class="normal"> 894</span>
<span class="normal"> 895</span>
<span class="normal"> 896</span>
<span class="normal"> 897</span>
<span class="normal"> 898</span>
<span class="normal"> 899</span>
<span class="normal"> 900</span>
<span class="normal"> 901</span>
<span class="normal"> 902</span>
<span class="normal"> 903</span>
<span class="normal"> 904</span>
<span class="normal"> 905</span>
<span class="normal"> 906</span>
<span class="normal"> 907</span>
<span class="normal"> 908</span>
<span class="normal"> 909</span>
<span class="normal"> 910</span>
<span class="normal"> 911</span>
<span class="normal"> 912</span>
<span class="normal"> 913</span>
<span class="normal"> 914</span>
<span class="normal"> 915</span>
<span class="normal"> 916</span>
<span class="normal"> 917</span>
<span class="normal"> 918</span>
<span class="normal"> 919</span>
<span class="normal"> 920</span>
<span class="normal"> 921</span>
<span class="normal"> 922</span>
<span class="normal"> 923</span>
<span class="normal"> 924</span>
<span class="normal"> 925</span>
<span class="normal"> 926</span>
<span class="normal"> 927</span>
<span class="normal"> 928</span>
<span class="normal"> 929</span>
<span class="normal"> 930</span>
<span class="normal"> 931</span>
<span class="normal"> 932</span>
<span class="normal"> 933</span>
<span class="normal"> 934</span>
<span class="normal"> 935</span>
<span class="normal"> 936</span>
<span class="normal"> 937</span>
<span class="normal"> 938</span>
<span class="normal"> 939</span>
<span class="normal"> 940</span>
<span class="normal"> 941</span>
<span class="normal"> 942</span>
<span class="normal"> 943</span>
<span class="normal"> 944</span>
<span class="normal"> 945</span>
<span class="normal"> 946</span>
<span class="normal"> 947</span>
<span class="normal"> 948</span>
<span class="normal"> 949</span>
<span class="normal"> 950</span>
<span class="normal"> 951</span>
<span class="normal"> 952</span>
<span class="normal"> 953</span>
<span class="normal"> 954</span>
<span class="normal"> 955</span>
<span class="normal"> 956</span>
<span class="normal"> 957</span>
<span class="normal"> 958</span>
<span class="normal"> 959</span>
<span class="normal"> 960</span>
<span class="normal"> 961</span>
<span class="normal"> 962</span>
<span class="normal"> 963</span>
<span class="normal"> 964</span>
<span class="normal"> 965</span>
<span class="normal"> 966</span>
<span class="normal"> 967</span>
<span class="normal"> 968</span>
<span class="normal"> 969</span>
<span class="normal"> 970</span>
<span class="normal"> 971</span>
<span class="normal"> 972</span>
<span class="normal"> 973</span>
<span class="normal"> 974</span>
<span class="normal"> 975</span>
<span class="normal"> 976</span>
<span class="normal"> 977</span>
<span class="normal"> 978</span>
<span class="normal"> 979</span>
<span class="normal"> 980</span>
<span class="normal"> 981</span>
<span class="normal"> 982</span>
<span class="normal"> 983</span>
<span class="normal"> 984</span>
<span class="normal"> 985</span>
<span class="normal"> 986</span>
<span class="normal"> 987</span>
<span class="normal"> 988</span>
<span class="normal"> 989</span>
<span class="normal"> 990</span>
<span class="normal"> 991</span>
<span class="normal"> 992</span>
<span class="normal"> 993</span>
<span class="normal"> 994</span>
<span class="normal"> 995</span>
<span class="normal"> 996</span>
<span class="normal"> 997</span>
<span class="normal"> 998</span>
<span class="normal"> 999</span>
<span class="normal">1000</span>
<span class="normal">1001</span>
<span class="normal">1002</span>
<span class="normal">1003</span>
<span class="normal">1004</span>
<span class="normal">1005</span>
<span class="normal">1006</span>
<span class="normal">1007</span>
<span class="normal">1008</span>
<span class="normal">1009</span>
<span class="normal">1010</span>
<span class="normal">1011</span>
<span class="normal">1012</span>
<span class="normal">1013</span>
<span class="normal">1014</span>
<span class="normal">1015</span>
<span class="normal">1016</span>
<span class="normal">1017</span>
<span class="normal">1018</span>
<span class="normal">1019</span>
<span class="normal">1020</span>
<span class="normal">1021</span>
<span class="normal">1022</span>
<span class="normal">1023</span>
<span class="normal">1024</span>
<span class="normal">1025</span>
<span class="normal">1026</span>
<span class="normal">1027</span>
<span class="normal">1028</span>
<span class="normal">1029</span>
<span class="normal">1030</span>
<span class="normal">1031</span>
<span class="normal">1032</span>
<span class="normal">1033</span>
<span class="normal">1034</span>
<span class="normal">1035</span>
<span class="normal">1036</span>
<span class="normal">1037</span>
<span class="normal">1038</span>
<span class="normal">1039</span>
<span class="normal">1040</span>
<span class="normal">1041</span>
<span class="normal">1042</span>
<span class="normal">1043</span>
<span class="normal">1044</span>
<span class="normal">1045</span>
<span class="normal">1046</span>
<span class="normal">1047</span>
<span class="normal">1048</span>
<span class="normal">1049</span>
<span class="normal">1050</span>
<span class="normal">1051</span>
<span class="normal">1052</span>
<span class="normal">1053</span>
<span class="normal">1054</span>
<span class="normal">1055</span>
<span class="normal">1056</span>
<span class="normal">1057</span>
<span class="normal">1058</span>
<span class="normal">1059</span>
<span class="normal">1060</span>
<span class="normal">1061</span>
<span class="normal">1062</span>
<span class="normal">1063</span>
<span class="normal">1064</span>
<span class="normal">1065</span>
<span class="normal">1066</span>
<span class="normal">1067</span>
<span class="normal">1068</span>
<span class="normal">1069</span>
<span class="normal">1070</span>
<span class="normal">1071</span>
<span class="normal">1072</span>
<span class="normal">1073</span>
<span class="normal">1074</span>
<span class="normal">1075</span>
<span class="normal">1076</span>
<span class="normal">1077</span>
<span class="normal">1078</span>
<span class="normal">1079</span>
<span class="normal">1080</span>
<span class="normal">1081</span>
<span class="normal">1082</span>
<span class="normal">1083</span>
<span class="normal">1084</span>
<span class="normal">1085</span>
<span class="normal">1086</span>
<span class="normal">1087</span>
<span class="normal">1088</span>
<span class="normal">1089</span>
<span class="normal">1090</span>
<span class="normal">1091</span>
<span class="normal">1092</span>
<span class="normal">1093</span>
<span class="normal">1094</span>
<span class="normal">1095</span>
<span class="normal">1096</span>
<span class="normal">1097</span>
<span class="normal">1098</span>
<span class="normal">1099</span>
<span class="normal">1100</span>
<span class="normal">1101</span>
<span class="normal">1102</span>
<span class="normal">1103</span>
<span class="normal">1104</span>
<span class="normal">1105</span>
<span class="normal">1106</span>
<span class="normal">1107</span>
<span class="normal">1108</span>
<span class="normal">1109</span>
<span class="normal">1110</span>
<span class="normal">1111</span>
<span class="normal">1112</span>
<span class="normal">1113</span>
<span class="normal">1114</span>
<span class="normal">1115</span>
<span class="normal">1116</span>
<span class="normal">1117</span>
<span class="normal">1118</span>
<span class="normal">1119</span>
<span class="normal">1120</span>
<span class="normal">1121</span>
<span class="normal">1122</span>
<span class="normal">1123</span>
<span class="normal">1124</span>
<span class="normal">1125</span>
<span class="normal">1126</span>
<span class="normal">1127</span>
<span class="normal">1128</span>
<span class="normal">1129</span>
<span class="normal">1130</span>
<span class="normal">1131</span>
<span class="normal">1132</span>
<span class="normal">1133</span>
<span class="normal">1134</span>
<span class="normal">1135</span>
<span class="normal">1136</span>
<span class="normal">1137</span>
<span class="normal">1138</span>
<span class="normal">1139</span>
<span class="normal">1140</span>
<span class="normal">1141</span>
<span class="normal">1142</span>
<span class="normal">1143</span>
<span class="normal">1144</span>
<span class="normal">1145</span>
<span class="normal">1146</span>
<span class="normal">1147</span>
<span class="normal">1148</span>
<span class="normal">1149</span>
<span class="normal">1150</span>
<span class="normal">1151</span>
<span class="normal">1152</span>
<span class="normal">1153</span>
<span class="normal">1154</span>
<span class="normal">1155</span>
<span class="normal">1156</span>
<span class="normal">1157</span>
<span class="normal">1158</span>
<span class="normal">1159</span>
<span class="normal">1160</span>
<span class="normal">1161</span>
<span class="normal">1162</span>
<span class="normal">1163</span>
<span class="normal">1164</span>
<span class="normal">1165</span>
<span class="normal">1166</span>
<span class="normal">1167</span>
<span class="normal">1168</span>
<span class="normal">1169</span>
<span class="normal">1170</span>
<span class="normal">1171</span>
<span class="normal">1172</span>
<span class="normal">1173</span>
<span class="normal">1174</span>
<span class="normal">1175</span>
<span class="normal">1176</span>
<span class="normal">1177</span>
<span class="normal">1178</span>
<span class="normal">1179</span>
<span class="normal">1180</span>
<span class="normal">1181</span>
<span class="normal">1182</span>
<span class="normal">1183</span>
<span class="normal">1184</span>
<span class="normal">1185</span>
<span class="normal">1186</span>
<span class="normal">1187</span>
<span class="normal">1188</span>
<span class="normal">1189</span>
<span class="normal">1190</span>
<span class="normal">1191</span>
<span class="normal">1192</span>
<span class="normal">1193</span>
<span class="normal">1194</span>
<span class="normal">1195</span>
<span class="normal">1196</span>
<span class="normal">1197</span>
<span class="normal">1198</span>
<span class="normal">1199</span>
<span class="normal">1200</span>
<span class="normal">1201</span>
<span class="normal">1202</span>
<span class="normal">1203</span>
<span class="normal">1204</span>
<span class="normal">1205</span>
<span class="normal">1206</span>
<span class="normal">1207</span>
<span class="normal">1208</span>
<span class="normal">1209</span>
<span class="normal">1210</span>
<span class="normal">1211</span>
<span class="normal">1212</span>
<span class="normal">1213</span>
<span class="normal">1214</span>
<span class="normal">1215</span>
<span class="normal">1216</span>
<span class="normal">1217</span>
<span class="normal">1218</span>
<span class="normal">1219</span>
<span class="normal">1220</span>
<span class="normal">1221</span>
<span class="normal">1222</span>
<span class="normal">1223</span>
<span class="normal">1224</span>
<span class="normal">1225</span>
<span class="normal">1226</span>
<span class="normal">1227</span>
<span class="normal">1228</span>
<span class="normal">1229</span>
<span class="normal">1230</span>
<span class="normal">1231</span>
<span class="normal">1232</span>
<span class="normal">1233</span>
<span class="normal">1234</span>
<span class="normal">1235</span>
<span class="normal">1236</span>
<span class="normal">1237</span>
<span class="normal">1238</span>
<span class="normal">1239</span>
<span class="normal">1240</span>
<span class="normal">1241</span>
<span class="normal">1242</span>
<span class="normal">1243</span>
<span class="normal">1244</span>
<span class="normal">1245</span>
<span class="normal">1246</span>
<span class="normal">1247</span>
<span class="normal">1248</span>
<span class="normal">1249</span>
<span class="normal">1250</span>
<span class="normal">1251</span>
<span class="normal">1252</span>
<span class="normal">1253</span>
<span class="normal">1254</span>
<span class="normal">1255</span>
<span class="normal">1256</span>
<span class="normal">1257</span>
<span class="normal">1258</span>
<span class="normal">1259</span>
<span class="normal">1260</span>
<span class="normal">1261</span>
<span class="normal">1262</span>
<span class="normal">1263</span>
<span class="normal">1264</span>
<span class="normal">1265</span>
<span class="normal">1266</span>
<span class="normal">1267</span>
<span class="normal">1268</span>
<span class="normal">1269</span>
<span class="normal">1270</span>
<span class="normal">1271</span>
<span class="normal">1272</span>
<span class="normal">1273</span>
<span class="normal">1274</span>
<span class="normal">1275</span>
<span class="normal">1276</span>
<span class="normal">1277</span>
<span class="normal">1278</span>
<span class="normal">1279</span>
<span class="normal">1280</span>
<span class="normal">1281</span>
<span class="normal">1282</span>
<span class="normal">1283</span>
<span class="normal">1284</span>
<span class="normal">1285</span>
<span class="normal">1286</span>
<span class="normal">1287</span>
<span class="normal">1288</span>
<span class="normal">1289</span>
<span class="normal">1290</span>
<span class="normal">1291</span>
<span class="normal">1292</span>
<span class="normal">1293</span>
<span class="normal">1294</span>
<span class="normal">1295</span>
<span class="normal">1296</span>
<span class="normal">1297</span>
<span class="normal">1298</span>
<span class="normal">1299</span>
<span class="normal">1300</span>
<span class="normal">1301</span>
<span class="normal">1302</span></pre></div></td><td class="code"><div><pre id="__code_1"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_1 > code"></button><code tabindex="0"><span class="nd">@final</span>
<span class="nd">@dataclasses</span><span class="o">.</span><span class="n">dataclass</span><span class="p">(</span><span class="n">init</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
<span class="k">class</span><span class="w"> </span><span class="nc">Agent</span><span class="p">(</span><span class="n">Generic</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">,</span> <span class="n">ResultDataT</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""Class for defining "agents" - a way to have a specific type of "conversation" with an LLM.</span>

<span class="sd">    Agents are generic in the dependency type they take [`AgentDepsT`][pydantic_ai.tools.AgentDepsT]</span>
<span class="sd">    and the result data type they return, [`ResultDataT`][pydantic_ai.result.ResultDataT].</span>

<span class="sd">    By default, if neither generic parameter is customised, agents have type `Agent[None, str]`.</span>

<span class="sd">    Minimal usage example:</span>

<span class="sd">    ```python</span>
<span class="sd">    from pydantic_ai import Agent</span>

<span class="sd">    agent = Agent('openai:gpt-4o')</span>
<span class="sd">    result = agent.run_sync('What is the capital of France?')</span>
<span class="sd">    print(result.data)</span>
<span class="sd">    #&gt; Paris</span>
<span class="sd">    ```</span>
<span class="sd">    """</span>

    <span class="n">model</span><span class="p">:</span> <span class="n">models</span><span class="o">.</span><span class="n">Model</span> <span class="o">|</span> <span class="n">models</span><span class="o">.</span><span class="n">KnownModelName</span> <span class="o">|</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span>
<span class="w">    </span><span class="sd">"""The default model configured for this agent.</span>

<span class="sd">    We allow str here since the actual list of allowed models changes frequently.</span>
<span class="sd">    """</span>

    <span class="n">name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span>
<span class="w">    </span><span class="sd">"""The name of the agent, used for logging.</span>

<span class="sd">    If `None`, we try to infer the agent name from the call frame when the agent is first run.</span>
<span class="sd">    """</span>
    <span class="n">end_strategy</span><span class="p">:</span> <span class="n">EndStrategy</span>
<span class="w">    </span><span class="sd">"""Strategy for handling tool calls when a final result is found."""</span>

    <span class="n">model_settings</span><span class="p">:</span> <span class="n">ModelSettings</span> <span class="o">|</span> <span class="kc">None</span>
<span class="w">    </span><span class="sd">"""Optional model request settings to use for this agents's runs, by default.</span>

<span class="sd">    Note, if `model_settings` is provided by `run`, `run_sync`, or `run_stream`, those settings will</span>
<span class="sd">    be merged with this value, with the runtime argument taking priority.</span>
<span class="sd">    """</span>

    <span class="n">result_type</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n">ResultDataT</span><span class="p">]</span> <span class="o">=</span> <span class="n">dataclasses</span><span class="o">.</span><span class="n">field</span><span class="p">(</span><span class="nb">repr</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    The type of the result data, used to validate the result data, defaults to `str`.</span>
<span class="sd">    """</span>

    <span class="n">instrument</span><span class="p">:</span> <span class="n">InstrumentationSettings</span> <span class="o">|</span> <span class="nb">bool</span> <span class="o">|</span> <span class="kc">None</span>
<span class="w">    </span><span class="sd">"""Options to automatically instrument with OpenTelemetry."""</span>

    <span class="n">_instrument_default</span><span class="p">:</span> <span class="n">ClassVar</span><span class="p">[</span><span class="n">InstrumentationSettings</span> <span class="o">|</span> <span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="kc">False</span>

    <span class="n">_deps_type</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">]</span> <span class="o">=</span> <span class="n">dataclasses</span><span class="o">.</span><span class="n">field</span><span class="p">(</span><span class="nb">repr</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
    <span class="n">_result_tool_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">dataclasses</span><span class="o">.</span><span class="n">field</span><span class="p">(</span><span class="nb">repr</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
    <span class="n">_result_tool_description</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="n">dataclasses</span><span class="o">.</span><span class="n">field</span><span class="p">(</span><span class="nb">repr</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
    <span class="n">_result_schema</span><span class="p">:</span> <span class="n">_result</span><span class="o">.</span><span class="n">ResultSchema</span><span class="p">[</span><span class="n">ResultDataT</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="n">dataclasses</span><span class="o">.</span><span class="n">field</span><span class="p">(</span><span class="nb">repr</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
    <span class="n">_result_validators</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">_result</span><span class="o">.</span><span class="n">ResultValidator</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">,</span> <span class="n">ResultDataT</span><span class="p">]]</span> <span class="o">=</span> <span class="n">dataclasses</span><span class="o">.</span><span class="n">field</span><span class="p">(</span><span class="nb">repr</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
    <span class="n">_system_prompts</span><span class="p">:</span> <span class="nb">tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="o">...</span><span class="p">]</span> <span class="o">=</span> <span class="n">dataclasses</span><span class="o">.</span><span class="n">field</span><span class="p">(</span><span class="nb">repr</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
    <span class="n">_system_prompt_functions</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">_system_prompt</span><span class="o">.</span><span class="n">SystemPromptRunner</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">]]</span> <span class="o">=</span> <span class="n">dataclasses</span><span class="o">.</span><span class="n">field</span><span class="p">(</span><span class="nb">repr</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
    <span class="n">_system_prompt_dynamic_functions</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">_system_prompt</span><span class="o">.</span><span class="n">SystemPromptRunner</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">]]</span> <span class="o">=</span> <span class="n">dataclasses</span><span class="o">.</span><span class="n">field</span><span class="p">(</span>
        <span class="nb">repr</span><span class="o">=</span><span class="kc">False</span>
    <span class="p">)</span>
    <span class="n">_function_tools</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Tool</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">]]</span> <span class="o">=</span> <span class="n">dataclasses</span><span class="o">.</span><span class="n">field</span><span class="p">(</span><span class="nb">repr</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
    <span class="n">_mcp_servers</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">MCPServer</span><span class="p">]</span> <span class="o">=</span> <span class="n">dataclasses</span><span class="o">.</span><span class="n">field</span><span class="p">(</span><span class="nb">repr</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
    <span class="n">_default_retries</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">dataclasses</span><span class="o">.</span><span class="n">field</span><span class="p">(</span><span class="nb">repr</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
    <span class="n">_max_result_retries</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">dataclasses</span><span class="o">.</span><span class="n">field</span><span class="p">(</span><span class="nb">repr</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
    <span class="n">_override_deps</span><span class="p">:</span> <span class="n">_utils</span><span class="o">.</span><span class="n">Option</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">]</span> <span class="o">=</span> <span class="n">dataclasses</span><span class="o">.</span><span class="n">field</span><span class="p">(</span><span class="n">default</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="nb">repr</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
    <span class="n">_override_model</span><span class="p">:</span> <span class="n">_utils</span><span class="o">.</span><span class="n">Option</span><span class="p">[</span><span class="n">models</span><span class="o">.</span><span class="n">Model</span><span class="p">]</span> <span class="o">=</span> <span class="n">dataclasses</span><span class="o">.</span><span class="n">field</span><span class="p">(</span><span class="n">default</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="nb">repr</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">model</span><span class="p">:</span> <span class="n">models</span><span class="o">.</span><span class="n">Model</span> <span class="o">|</span> <span class="n">models</span><span class="o">.</span><span class="n">KnownModelName</span> <span class="o">|</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">*</span><span class="p">,</span>
        <span class="n">result_type</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n">ResultDataT</span><span class="p">]</span> <span class="o">=</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">system_prompt</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="p">(),</span>
        <span class="n">deps_type</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">]</span> <span class="o">=</span> <span class="n">NoneType</span><span class="p">,</span>
        <span class="n">name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">model_settings</span><span class="p">:</span> <span class="n">ModelSettings</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">retries</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span>
        <span class="n">result_tool_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s1">'final_result'</span><span class="p">,</span>
        <span class="n">result_tool_description</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">result_retries</span><span class="p">:</span> <span class="nb">int</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">tools</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">Tool</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">]</span> <span class="o">|</span> <span class="n">ToolFuncEither</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">,</span> <span class="o">...</span><span class="p">]]</span> <span class="o">=</span> <span class="p">(),</span>
        <span class="n">mcp_servers</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">MCPServer</span><span class="p">]</span> <span class="o">=</span> <span class="p">(),</span>
        <span class="n">defer_model_check</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">end_strategy</span><span class="p">:</span> <span class="n">EndStrategy</span> <span class="o">=</span> <span class="s1">'early'</span><span class="p">,</span>
        <span class="n">instrument</span><span class="p">:</span> <span class="n">InstrumentationSettings</span> <span class="o">|</span> <span class="nb">bool</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">):</span>
<span class="w">        </span><span class="sd">"""Create an agent.</span>

<span class="sd">        Args:</span>
<span class="sd">            model: The default model to use for this agent, if not provide,</span>
<span class="sd">                you must provide the model when calling it. We allow str here since the actual list of allowed models changes frequently.</span>
<span class="sd">            result_type: The type of the result data, used to validate the result data, defaults to `str`.</span>
<span class="sd">            system_prompt: Static system prompts to use for this agent, you can also register system</span>
<span class="sd">                prompts via a function with [`system_prompt`][pydantic_ai.Agent.system_prompt].</span>
<span class="sd">            deps_type: The type used for dependency injection, this parameter exists solely to allow you to fully</span>
<span class="sd">                parameterize the agent, and therefore get the best out of static type checking.</span>
<span class="sd">                If you're not using deps, but want type checking to pass, you can set `deps=None` to satisfy Pyright</span>
<span class="sd">                or add a type hint `: Agent[None, &lt;return type&gt;]`.</span>
<span class="sd">            name: The name of the agent, used for logging. If `None`, we try to infer the agent name from the call frame</span>
<span class="sd">                when the agent is first run.</span>
<span class="sd">            model_settings: Optional model request settings to use for this agent's runs, by default.</span>
<span class="sd">            retries: The default number of retries to allow before raising an error.</span>
<span class="sd">            result_tool_name: The name of the tool to use for the final result.</span>
<span class="sd">            result_tool_description: The description of the final result tool.</span>
<span class="sd">            result_retries: The maximum number of retries to allow for result validation, defaults to `retries`.</span>
<span class="sd">            tools: Tools to register with the agent, you can also register tools via the decorators</span>
<span class="sd">                [`@agent.tool`][pydantic_ai.Agent.tool] and [`@agent.tool_plain`][pydantic_ai.Agent.tool_plain].</span>
<span class="sd">            mcp_servers: MCP servers to register with the agent. You should register a [`MCPServer`][pydantic_ai.mcp.MCPServer]</span>
<span class="sd">                for each server you want the agent to connect to.</span>
<span class="sd">            defer_model_check: by default, if you provide a [named][pydantic_ai.models.KnownModelName] model,</span>
<span class="sd">                it's evaluated to create a [`Model`][pydantic_ai.models.Model] instance immediately,</span>
<span class="sd">                which checks for the necessary environment variables. Set this to `false`</span>
<span class="sd">                to defer the evaluation until the first run. Useful if you want to</span>
<span class="sd">                [override the model][pydantic_ai.Agent.override] for testing.</span>
<span class="sd">            end_strategy: Strategy for handling tool calls that are requested alongside a final result.</span>
<span class="sd">                See [`EndStrategy`][pydantic_ai.agent.EndStrategy] for more information.</span>
<span class="sd">            instrument: Set to True to automatically instrument with OpenTelemetry,</span>
<span class="sd">                which will use Logfire if it's configured.</span>
<span class="sd">                Set to an instance of [`InstrumentationSettings`][pydantic_ai.agent.InstrumentationSettings] to customize.</span>
<span class="sd">                If this isn't set, then the last value set by</span>
<span class="sd">                [`Agent.instrument_all()`][pydantic_ai.Agent.instrument_all]</span>
<span class="sd">                will be used, which defaults to False.</span>
<span class="sd">                See the [Debugging and Monitoring guide](https://ai.pydantic.dev/logfire/) for more info.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">model</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">or</span> <span class="n">defer_model_check</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">model</span> <span class="o">=</span> <span class="n">model</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">model</span> <span class="o">=</span> <span class="n">models</span><span class="o">.</span><span class="n">infer_model</span><span class="p">(</span><span class="n">model</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">end_strategy</span> <span class="o">=</span> <span class="n">end_strategy</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="o">=</span> <span class="n">name</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">model_settings</span> <span class="o">=</span> <span class="n">model_settings</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">result_type</span> <span class="o">=</span> <span class="n">result_type</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">instrument</span> <span class="o">=</span> <span class="n">instrument</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_deps_type</span> <span class="o">=</span> <span class="n">deps_type</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_result_tool_name</span> <span class="o">=</span> <span class="n">result_tool_name</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_result_tool_description</span> <span class="o">=</span> <span class="n">result_tool_description</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_result_schema</span> <span class="o">=</span> <span class="n">_result</span><span class="o">.</span><span class="n">ResultSchema</span><span class="p">[</span><span class="n">result_type</span><span class="p">]</span><span class="o">.</span><span class="n">build</span><span class="p">(</span>
            <span class="n">result_type</span><span class="p">,</span> <span class="n">result_tool_name</span><span class="p">,</span> <span class="n">result_tool_description</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_result_validators</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_system_prompts</span> <span class="o">=</span> <span class="p">(</span><span class="n">system_prompt</span><span class="p">,)</span> <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">system_prompt</span><span class="p">,</span> <span class="nb">str</span><span class="p">)</span> <span class="k">else</span> <span class="nb">tuple</span><span class="p">(</span><span class="n">system_prompt</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_system_prompt_functions</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_system_prompt_dynamic_functions</span> <span class="o">=</span> <span class="p">{}</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_function_tools</span> <span class="o">=</span> <span class="p">{}</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_default_retries</span> <span class="o">=</span> <span class="n">retries</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_max_result_retries</span> <span class="o">=</span> <span class="n">result_retries</span> <span class="k">if</span> <span class="n">result_retries</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="k">else</span> <span class="n">retries</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_mcp_servers</span> <span class="o">=</span> <span class="n">mcp_servers</span>
        <span class="k">for</span> <span class="n">tool</span> <span class="ow">in</span> <span class="n">tools</span><span class="p">:</span>
            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">tool</span><span class="p">,</span> <span class="n">Tool</span><span class="p">):</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_register_tool</span><span class="p">(</span><span class="n">tool</span><span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_register_tool</span><span class="p">(</span><span class="n">Tool</span><span class="p">(</span><span class="n">tool</span><span class="p">))</span>

    <span class="nd">@staticmethod</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">instrument_all</span><span class="p">(</span><span class="n">instrument</span><span class="p">:</span> <span class="n">InstrumentationSettings</span> <span class="o">|</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Set the instrumentation options for all agents where `instrument` is not set."""</span>
        <span class="n">Agent</span><span class="o">.</span><span class="n">_instrument_default</span> <span class="o">=</span> <span class="n">instrument</span>

    <span class="nd">@overload</span>
    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">run</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">user_prompt</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">_messages</span><span class="o">.</span><span class="n">UserContent</span><span class="p">],</span>
        <span class="o">*</span><span class="p">,</span>
        <span class="n">result_type</span><span class="p">:</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">message_history</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">_messages</span><span class="o">.</span><span class="n">ModelMessage</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">model</span><span class="p">:</span> <span class="n">models</span><span class="o">.</span><span class="n">Model</span> <span class="o">|</span> <span class="n">models</span><span class="o">.</span><span class="n">KnownModelName</span> <span class="o">|</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">deps</span><span class="p">:</span> <span class="n">AgentDepsT</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">model_settings</span><span class="p">:</span> <span class="n">ModelSettings</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">usage_limits</span><span class="p">:</span> <span class="n">_usage</span><span class="o">.</span><span class="n">UsageLimits</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">usage</span><span class="p">:</span> <span class="n">_usage</span><span class="o">.</span><span class="n">Usage</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">infer_name</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AgentRunResult</span><span class="p">[</span><span class="n">ResultDataT</span><span class="p">]:</span> <span class="o">...</span>

    <span class="nd">@overload</span>
    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">run</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">user_prompt</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">_messages</span><span class="o">.</span><span class="n">UserContent</span><span class="p">],</span>
        <span class="o">*</span><span class="p">,</span>
        <span class="n">result_type</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n">RunResultDataT</span><span class="p">],</span>
        <span class="n">message_history</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">_messages</span><span class="o">.</span><span class="n">ModelMessage</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">model</span><span class="p">:</span> <span class="n">models</span><span class="o">.</span><span class="n">Model</span> <span class="o">|</span> <span class="n">models</span><span class="o">.</span><span class="n">KnownModelName</span> <span class="o">|</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">deps</span><span class="p">:</span> <span class="n">AgentDepsT</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">model_settings</span><span class="p">:</span> <span class="n">ModelSettings</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">usage_limits</span><span class="p">:</span> <span class="n">_usage</span><span class="o">.</span><span class="n">UsageLimits</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">usage</span><span class="p">:</span> <span class="n">_usage</span><span class="o">.</span><span class="n">Usage</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">infer_name</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AgentRunResult</span><span class="p">[</span><span class="n">RunResultDataT</span><span class="p">]:</span> <span class="o">...</span>

    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">run</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">user_prompt</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">_messages</span><span class="o">.</span><span class="n">UserContent</span><span class="p">],</span>
        <span class="o">*</span><span class="p">,</span>
        <span class="n">result_type</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n">RunResultDataT</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">message_history</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">_messages</span><span class="o">.</span><span class="n">ModelMessage</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">model</span><span class="p">:</span> <span class="n">models</span><span class="o">.</span><span class="n">Model</span> <span class="o">|</span> <span class="n">models</span><span class="o">.</span><span class="n">KnownModelName</span> <span class="o">|</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">deps</span><span class="p">:</span> <span class="n">AgentDepsT</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">model_settings</span><span class="p">:</span> <span class="n">ModelSettings</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">usage_limits</span><span class="p">:</span> <span class="n">_usage</span><span class="o">.</span><span class="n">UsageLimits</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">usage</span><span class="p">:</span> <span class="n">_usage</span><span class="o">.</span><span class="n">Usage</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">infer_name</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AgentRunResult</span><span class="p">[</span><span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Run the agent with a user prompt in async mode.</span>

<span class="sd">        This method builds an internal agent graph (using system prompts, tools and result schemas) and then</span>
<span class="sd">        runs the graph to completion. The result of the run is returned.</span>

<span class="sd">        Example:</span>
<span class="sd">        ```python</span>
<span class="sd">        from pydantic_ai import Agent</span>

<span class="sd">        agent = Agent('openai:gpt-4o')</span>

<span class="sd">        async def main():</span>
<span class="sd">            agent_run = await agent.run('What is the capital of France?')</span>
<span class="sd">            print(agent_run.data)</span>
<span class="sd">            #&gt; Paris</span>
<span class="sd">        ```</span>

<span class="sd">        Args:</span>
<span class="sd">            user_prompt: User input to start/continue the conversation.</span>
<span class="sd">            result_type: Custom result type to use for this run, `result_type` may only be used if the agent has no</span>
<span class="sd">                result validators since result validators would expect an argument that matches the agent's result type.</span>
<span class="sd">            message_history: History of the conversation so far.</span>
<span class="sd">            model: Optional model to use for this run, required if `model` was not set when creating the agent.</span>
<span class="sd">            deps: Optional dependencies to use for this run.</span>
<span class="sd">            model_settings: Optional settings to use for this model's request.</span>
<span class="sd">            usage_limits: Optional limits on model request count or token usage.</span>
<span class="sd">            usage: Optional usage to start with, useful for resuming a conversation or agents used in tools.</span>
<span class="sd">            infer_name: Whether to try to infer the agent name from the call frame if it's not set.</span>

<span class="sd">        Returns:</span>
<span class="sd">            The result of the run.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">infer_name</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_infer_name</span><span class="p">(</span><span class="n">inspect</span><span class="o">.</span><span class="n">currentframe</span><span class="p">())</span>
        <span class="k">async</span> <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">iter</span><span class="p">(</span>
            <span class="n">user_prompt</span><span class="o">=</span><span class="n">user_prompt</span><span class="p">,</span>
            <span class="n">result_type</span><span class="o">=</span><span class="n">result_type</span><span class="p">,</span>
            <span class="n">message_history</span><span class="o">=</span><span class="n">message_history</span><span class="p">,</span>
            <span class="n">model</span><span class="o">=</span><span class="n">model</span><span class="p">,</span>
            <span class="n">deps</span><span class="o">=</span><span class="n">deps</span><span class="p">,</span>
            <span class="n">model_settings</span><span class="o">=</span><span class="n">model_settings</span><span class="p">,</span>
            <span class="n">usage_limits</span><span class="o">=</span><span class="n">usage_limits</span><span class="p">,</span>
            <span class="n">usage</span><span class="o">=</span><span class="n">usage</span><span class="p">,</span>
        <span class="p">)</span> <span class="k">as</span> <span class="n">agent_run</span><span class="p">:</span>
            <span class="k">async</span> <span class="k">for</span> <span class="n">_</span> <span class="ow">in</span> <span class="n">agent_run</span><span class="p">:</span>
                <span class="k">pass</span>

        <span class="k">assert</span> <span class="n">agent_run</span><span class="o">.</span><span class="n">result</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">,</span> <span class="s1">'The graph run did not finish properly'</span>
        <span class="k">return</span> <span class="n">agent_run</span><span class="o">.</span><span class="n">result</span>

    <span class="nd">@asynccontextmanager</span>
    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">iter</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">user_prompt</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">_messages</span><span class="o">.</span><span class="n">UserContent</span><span class="p">],</span>
        <span class="o">*</span><span class="p">,</span>
        <span class="n">result_type</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n">RunResultDataT</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">message_history</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">_messages</span><span class="o">.</span><span class="n">ModelMessage</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">model</span><span class="p">:</span> <span class="n">models</span><span class="o">.</span><span class="n">Model</span> <span class="o">|</span> <span class="n">models</span><span class="o">.</span><span class="n">KnownModelName</span> <span class="o">|</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">deps</span><span class="p">:</span> <span class="n">AgentDepsT</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">model_settings</span><span class="p">:</span> <span class="n">ModelSettings</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">usage_limits</span><span class="p">:</span> <span class="n">_usage</span><span class="o">.</span><span class="n">UsageLimits</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">usage</span><span class="p">:</span> <span class="n">_usage</span><span class="o">.</span><span class="n">Usage</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">infer_name</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AsyncIterator</span><span class="p">[</span><span class="n">AgentRun</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""A contextmanager which can be used to iterate over the agent graph's nodes as they are executed.</span>

<span class="sd">        This method builds an internal agent graph (using system prompts, tools and result schemas) and then returns an</span>
<span class="sd">        `AgentRun` object. The `AgentRun` can be used to async-iterate over the nodes of the graph as they are</span>
<span class="sd">        executed. This is the API to use if you want to consume the outputs coming from each LLM model response, or the</span>
<span class="sd">        stream of events coming from the execution of tools.</span>

<span class="sd">        The `AgentRun` also provides methods to access the full message history, new messages, and usage statistics,</span>
<span class="sd">        and the final result of the run once it has completed.</span>

<span class="sd">        For more details, see the documentation of `AgentRun`.</span>

<span class="sd">        Example:</span>
<span class="sd">        ```python</span>
<span class="sd">        from pydantic_ai import Agent</span>

<span class="sd">        agent = Agent('openai:gpt-4o')</span>

<span class="sd">        async def main():</span>
<span class="sd">            nodes = []</span>
<span class="sd">            async with agent.iter('What is the capital of France?') as agent_run:</span>
<span class="sd">                async for node in agent_run:</span>
<span class="sd">                    nodes.append(node)</span>
<span class="sd">            print(nodes)</span>
<span class="sd">            '''</span>
<span class="sd">            [</span>
<span class="sd">                ModelRequestNode(</span>
<span class="sd">                    request=ModelRequest(</span>
<span class="sd">                        parts=[</span>
<span class="sd">                            UserPromptPart(</span>
<span class="sd">                                content='What is the capital of France?',</span>
<span class="sd">                                timestamp=datetime.datetime(...),</span>
<span class="sd">                                part_kind='user-prompt',</span>
<span class="sd">                            )</span>
<span class="sd">                        ],</span>
<span class="sd">                        kind='request',</span>
<span class="sd">                    )</span>
<span class="sd">                ),</span>
<span class="sd">                CallToolsNode(</span>
<span class="sd">                    model_response=ModelResponse(</span>
<span class="sd">                        parts=[TextPart(content='Paris', part_kind='text')],</span>
<span class="sd">                        model_name='gpt-4o',</span>
<span class="sd">                        timestamp=datetime.datetime(...),</span>
<span class="sd">                        kind='response',</span>
<span class="sd">                    )</span>
<span class="sd">                ),</span>
<span class="sd">                End(data=FinalResult(data='Paris', tool_name=None, tool_call_id=None)),</span>
<span class="sd">            ]</span>
<span class="sd">            '''</span>
<span class="sd">            print(agent_run.result.data)</span>
<span class="sd">            #&gt; Paris</span>
<span class="sd">        ```</span>

<span class="sd">        Args:</span>
<span class="sd">            user_prompt: User input to start/continue the conversation.</span>
<span class="sd">            result_type: Custom result type to use for this run, `result_type` may only be used if the agent has no</span>
<span class="sd">                result validators since result validators would expect an argument that matches the agent's result type.</span>
<span class="sd">            message_history: History of the conversation so far.</span>
<span class="sd">            model: Optional model to use for this run, required if `model` was not set when creating the agent.</span>
<span class="sd">            deps: Optional dependencies to use for this run.</span>
<span class="sd">            model_settings: Optional settings to use for this model's request.</span>
<span class="sd">            usage_limits: Optional limits on model request count or token usage.</span>
<span class="sd">            usage: Optional usage to start with, useful for resuming a conversation or agents used in tools.</span>
<span class="sd">            infer_name: Whether to try to infer the agent name from the call frame if it's not set.</span>

<span class="sd">        Returns:</span>
<span class="sd">            The result of the run.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">infer_name</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_infer_name</span><span class="p">(</span><span class="n">inspect</span><span class="o">.</span><span class="n">currentframe</span><span class="p">())</span>
        <span class="n">model_used</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_model</span><span class="p">(</span><span class="n">model</span><span class="p">)</span>
        <span class="k">del</span> <span class="n">model</span>

        <span class="n">deps</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_deps</span><span class="p">(</span><span class="n">deps</span><span class="p">)</span>
        <span class="n">new_message_index</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">message_history</span><span class="p">)</span> <span class="k">if</span> <span class="n">message_history</span> <span class="k">else</span> <span class="mi">0</span>
        <span class="n">result_schema</span><span class="p">:</span> <span class="n">_result</span><span class="o">.</span><span class="n">ResultSchema</span><span class="p">[</span><span class="n">RunResultDataT</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prepare_result_schema</span><span class="p">(</span><span class="n">result_type</span><span class="p">)</span>

        <span class="c1"># Build the graph</span>
        <span class="n">graph</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_build_graph</span><span class="p">(</span><span class="n">result_type</span><span class="p">)</span>

        <span class="c1"># Build the initial state</span>
        <span class="n">state</span> <span class="o">=</span> <span class="n">_agent_graph</span><span class="o">.</span><span class="n">GraphAgentState</span><span class="p">(</span>
            <span class="n">message_history</span><span class="o">=</span><span class="n">message_history</span><span class="p">[:]</span> <span class="k">if</span> <span class="n">message_history</span> <span class="k">else</span> <span class="p">[],</span>
            <span class="n">usage</span><span class="o">=</span><span class="n">usage</span> <span class="ow">or</span> <span class="n">_usage</span><span class="o">.</span><span class="n">Usage</span><span class="p">(),</span>
            <span class="n">retries</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
            <span class="n">run_step</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="c1"># We consider it a user error if a user tries to restrict the result type while having a result validator that</span>
        <span class="c1"># may change the result type from the restricted type to something else. Therefore, we consider the following</span>
        <span class="c1"># typecast reasonable, even though it is possible to violate it with otherwise-type-checked code.</span>
        <span class="n">result_validators</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="nb">list</span><span class="p">[</span><span class="n">_result</span><span class="o">.</span><span class="n">ResultValidator</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">,</span> <span class="n">RunResultDataT</span><span class="p">]],</span> <span class="bp">self</span><span class="o">.</span><span class="n">_result_validators</span><span class="p">)</span>

        <span class="c1"># TODO: Instead of this, copy the function tools to ensure they don't share current_retry state between agent</span>
        <span class="c1">#  runs. Requires some changes to `Tool` to make them copyable though.</span>
        <span class="k">for</span> <span class="n">v</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_function_tools</span><span class="o">.</span><span class="n">values</span><span class="p">():</span>
            <span class="n">v</span><span class="o">.</span><span class="n">current_retry</span> <span class="o">=</span> <span class="mi">0</span>

        <span class="n">model_settings</span> <span class="o">=</span> <span class="n">merge_model_settings</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">model_settings</span><span class="p">,</span> <span class="n">model_settings</span><span class="p">)</span>
        <span class="n">usage_limits</span> <span class="o">=</span> <span class="n">usage_limits</span> <span class="ow">or</span> <span class="n">_usage</span><span class="o">.</span><span class="n">UsageLimits</span><span class="p">()</span>

        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">model_used</span><span class="p">,</span> <span class="n">InstrumentedModel</span><span class="p">):</span>
            <span class="n">tracer</span> <span class="o">=</span> <span class="n">model_used</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">tracer</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">tracer</span> <span class="o">=</span> <span class="n">NoOpTracer</span><span class="p">()</span>
        <span class="n">agent_name</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="ow">or</span> <span class="s1">'agent'</span>
        <span class="n">run_span</span> <span class="o">=</span> <span class="n">tracer</span><span class="o">.</span><span class="n">start_span</span><span class="p">(</span>
            <span class="s1">'agent run'</span><span class="p">,</span>
            <span class="n">attributes</span><span class="o">=</span><span class="p">{</span>
                <span class="s1">'model_name'</span><span class="p">:</span> <span class="n">model_used</span><span class="o">.</span><span class="n">model_name</span> <span class="k">if</span> <span class="n">model_used</span> <span class="k">else</span> <span class="s1">'no-model'</span><span class="p">,</span>
                <span class="s1">'agent_name'</span><span class="p">:</span> <span class="n">agent_name</span><span class="p">,</span>
                <span class="s1">'logfire.msg'</span><span class="p">:</span> <span class="sa">f</span><span class="s1">'</span><span class="si">{</span><span class="n">agent_name</span><span class="si">}</span><span class="s1"> run'</span><span class="p">,</span>
            <span class="p">},</span>
        <span class="p">)</span>

        <span class="n">graph_deps</span> <span class="o">=</span> <span class="n">_agent_graph</span><span class="o">.</span><span class="n">GraphAgentDeps</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">,</span> <span class="n">RunResultDataT</span><span class="p">](</span>
            <span class="n">user_deps</span><span class="o">=</span><span class="n">deps</span><span class="p">,</span>
            <span class="n">prompt</span><span class="o">=</span><span class="n">user_prompt</span><span class="p">,</span>
            <span class="n">new_message_index</span><span class="o">=</span><span class="n">new_message_index</span><span class="p">,</span>
            <span class="n">model</span><span class="o">=</span><span class="n">model_used</span><span class="p">,</span>
            <span class="n">model_settings</span><span class="o">=</span><span class="n">model_settings</span><span class="p">,</span>
            <span class="n">usage_limits</span><span class="o">=</span><span class="n">usage_limits</span><span class="p">,</span>
            <span class="n">max_result_retries</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_max_result_retries</span><span class="p">,</span>
            <span class="n">end_strategy</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">end_strategy</span><span class="p">,</span>
            <span class="n">result_schema</span><span class="o">=</span><span class="n">result_schema</span><span class="p">,</span>
            <span class="n">result_tools</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_result_schema</span><span class="o">.</span><span class="n">tool_defs</span><span class="p">()</span> <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_result_schema</span> <span class="k">else</span> <span class="p">[],</span>
            <span class="n">result_validators</span><span class="o">=</span><span class="n">result_validators</span><span class="p">,</span>
            <span class="n">function_tools</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_function_tools</span><span class="p">,</span>
            <span class="n">mcp_servers</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_mcp_servers</span><span class="p">,</span>
            <span class="n">run_span</span><span class="o">=</span><span class="n">run_span</span><span class="p">,</span>
            <span class="n">tracer</span><span class="o">=</span><span class="n">tracer</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">start_node</span> <span class="o">=</span> <span class="n">_agent_graph</span><span class="o">.</span><span class="n">UserPromptNode</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">](</span>
            <span class="n">user_prompt</span><span class="o">=</span><span class="n">user_prompt</span><span class="p">,</span>
            <span class="n">system_prompts</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_system_prompts</span><span class="p">,</span>
            <span class="n">system_prompt_functions</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_system_prompt_functions</span><span class="p">,</span>
            <span class="n">system_prompt_dynamic_functions</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_system_prompt_dynamic_functions</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">async</span> <span class="k">with</span> <span class="n">graph</span><span class="o">.</span><span class="n">iter</span><span class="p">(</span>
            <span class="n">start_node</span><span class="p">,</span>
            <span class="n">state</span><span class="o">=</span><span class="n">state</span><span class="p">,</span>
            <span class="n">deps</span><span class="o">=</span><span class="n">graph_deps</span><span class="p">,</span>
            <span class="n">span</span><span class="o">=</span><span class="n">use_span</span><span class="p">(</span><span class="n">run_span</span><span class="p">,</span> <span class="n">end_on_exit</span><span class="o">=</span><span class="kc">True</span><span class="p">),</span>
            <span class="n">infer_name</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
        <span class="p">)</span> <span class="k">as</span> <span class="n">graph_run</span><span class="p">:</span>
            <span class="k">yield</span> <span class="n">AgentRun</span><span class="p">(</span><span class="n">graph_run</span><span class="p">)</span>

    <span class="nd">@overload</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">run_sync</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">user_prompt</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">_messages</span><span class="o">.</span><span class="n">UserContent</span><span class="p">],</span>
        <span class="o">*</span><span class="p">,</span>
        <span class="n">message_history</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">_messages</span><span class="o">.</span><span class="n">ModelMessage</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">model</span><span class="p">:</span> <span class="n">models</span><span class="o">.</span><span class="n">Model</span> <span class="o">|</span> <span class="n">models</span><span class="o">.</span><span class="n">KnownModelName</span> <span class="o">|</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">deps</span><span class="p">:</span> <span class="n">AgentDepsT</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">model_settings</span><span class="p">:</span> <span class="n">ModelSettings</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">usage_limits</span><span class="p">:</span> <span class="n">_usage</span><span class="o">.</span><span class="n">UsageLimits</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">usage</span><span class="p">:</span> <span class="n">_usage</span><span class="o">.</span><span class="n">Usage</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">infer_name</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AgentRunResult</span><span class="p">[</span><span class="n">ResultDataT</span><span class="p">]:</span> <span class="o">...</span>

    <span class="nd">@overload</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">run_sync</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">user_prompt</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">_messages</span><span class="o">.</span><span class="n">UserContent</span><span class="p">],</span>
        <span class="o">*</span><span class="p">,</span>
        <span class="n">result_type</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n">RunResultDataT</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">message_history</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">_messages</span><span class="o">.</span><span class="n">ModelMessage</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">model</span><span class="p">:</span> <span class="n">models</span><span class="o">.</span><span class="n">Model</span> <span class="o">|</span> <span class="n">models</span><span class="o">.</span><span class="n">KnownModelName</span> <span class="o">|</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">deps</span><span class="p">:</span> <span class="n">AgentDepsT</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">model_settings</span><span class="p">:</span> <span class="n">ModelSettings</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">usage_limits</span><span class="p">:</span> <span class="n">_usage</span><span class="o">.</span><span class="n">UsageLimits</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">usage</span><span class="p">:</span> <span class="n">_usage</span><span class="o">.</span><span class="n">Usage</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">infer_name</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AgentRunResult</span><span class="p">[</span><span class="n">RunResultDataT</span><span class="p">]:</span> <span class="o">...</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">run_sync</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">user_prompt</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">_messages</span><span class="o">.</span><span class="n">UserContent</span><span class="p">],</span>
        <span class="o">*</span><span class="p">,</span>
        <span class="n">result_type</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n">RunResultDataT</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">message_history</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">_messages</span><span class="o">.</span><span class="n">ModelMessage</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">model</span><span class="p">:</span> <span class="n">models</span><span class="o">.</span><span class="n">Model</span> <span class="o">|</span> <span class="n">models</span><span class="o">.</span><span class="n">KnownModelName</span> <span class="o">|</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">deps</span><span class="p">:</span> <span class="n">AgentDepsT</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">model_settings</span><span class="p">:</span> <span class="n">ModelSettings</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">usage_limits</span><span class="p">:</span> <span class="n">_usage</span><span class="o">.</span><span class="n">UsageLimits</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">usage</span><span class="p">:</span> <span class="n">_usage</span><span class="o">.</span><span class="n">Usage</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">infer_name</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AgentRunResult</span><span class="p">[</span><span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Synchronously run the agent with a user prompt.</span>

<span class="sd">        This is a convenience method that wraps [`self.run`][pydantic_ai.Agent.run] with `loop.run_until_complete(...)`.</span>
<span class="sd">        You therefore can't use this method inside async code or if there's an active event loop.</span>

<span class="sd">        Example:</span>
<span class="sd">        ```python</span>
<span class="sd">        from pydantic_ai import Agent</span>

<span class="sd">        agent = Agent('openai:gpt-4o')</span>

<span class="sd">        result_sync = agent.run_sync('What is the capital of Italy?')</span>
<span class="sd">        print(result_sync.data)</span>
<span class="sd">        #&gt; Rome</span>
<span class="sd">        ```</span>

<span class="sd">        Args:</span>
<span class="sd">            user_prompt: User input to start/continue the conversation.</span>
<span class="sd">            result_type: Custom result type to use for this run, `result_type` may only be used if the agent has no</span>
<span class="sd">                result validators since result validators would expect an argument that matches the agent's result type.</span>
<span class="sd">            message_history: History of the conversation so far.</span>
<span class="sd">            model: Optional model to use for this run, required if `model` was not set when creating the agent.</span>
<span class="sd">            deps: Optional dependencies to use for this run.</span>
<span class="sd">            model_settings: Optional settings to use for this model's request.</span>
<span class="sd">            usage_limits: Optional limits on model request count or token usage.</span>
<span class="sd">            usage: Optional usage to start with, useful for resuming a conversation or agents used in tools.</span>
<span class="sd">            infer_name: Whether to try to infer the agent name from the call frame if it's not set.</span>

<span class="sd">        Returns:</span>
<span class="sd">            The result of the run.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">infer_name</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_infer_name</span><span class="p">(</span><span class="n">inspect</span><span class="o">.</span><span class="n">currentframe</span><span class="p">())</span>
        <span class="k">return</span> <span class="n">get_event_loop</span><span class="p">()</span><span class="o">.</span><span class="n">run_until_complete</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">run</span><span class="p">(</span>
                <span class="n">user_prompt</span><span class="p">,</span>
                <span class="n">result_type</span><span class="o">=</span><span class="n">result_type</span><span class="p">,</span>
                <span class="n">message_history</span><span class="o">=</span><span class="n">message_history</span><span class="p">,</span>
                <span class="n">model</span><span class="o">=</span><span class="n">model</span><span class="p">,</span>
                <span class="n">deps</span><span class="o">=</span><span class="n">deps</span><span class="p">,</span>
                <span class="n">model_settings</span><span class="o">=</span><span class="n">model_settings</span><span class="p">,</span>
                <span class="n">usage_limits</span><span class="o">=</span><span class="n">usage_limits</span><span class="p">,</span>
                <span class="n">usage</span><span class="o">=</span><span class="n">usage</span><span class="p">,</span>
                <span class="n">infer_name</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="p">)</span>

    <span class="nd">@overload</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">run_stream</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">user_prompt</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">_messages</span><span class="o">.</span><span class="n">UserContent</span><span class="p">],</span>
        <span class="o">*</span><span class="p">,</span>
        <span class="n">result_type</span><span class="p">:</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">message_history</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">_messages</span><span class="o">.</span><span class="n">ModelMessage</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">model</span><span class="p">:</span> <span class="n">models</span><span class="o">.</span><span class="n">Model</span> <span class="o">|</span> <span class="n">models</span><span class="o">.</span><span class="n">KnownModelName</span> <span class="o">|</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">deps</span><span class="p">:</span> <span class="n">AgentDepsT</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">model_settings</span><span class="p">:</span> <span class="n">ModelSettings</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">usage_limits</span><span class="p">:</span> <span class="n">_usage</span><span class="o">.</span><span class="n">UsageLimits</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">usage</span><span class="p">:</span> <span class="n">_usage</span><span class="o">.</span><span class="n">Usage</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">infer_name</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AbstractAsyncContextManager</span><span class="p">[</span><span class="n">result</span><span class="o">.</span><span class="n">StreamedRunResult</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">,</span> <span class="n">ResultDataT</span><span class="p">]]:</span> <span class="o">...</span>

    <span class="nd">@overload</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">run_stream</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">user_prompt</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">_messages</span><span class="o">.</span><span class="n">UserContent</span><span class="p">],</span>
        <span class="o">*</span><span class="p">,</span>
        <span class="n">result_type</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n">RunResultDataT</span><span class="p">],</span>
        <span class="n">message_history</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">_messages</span><span class="o">.</span><span class="n">ModelMessage</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">model</span><span class="p">:</span> <span class="n">models</span><span class="o">.</span><span class="n">Model</span> <span class="o">|</span> <span class="n">models</span><span class="o">.</span><span class="n">KnownModelName</span> <span class="o">|</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">deps</span><span class="p">:</span> <span class="n">AgentDepsT</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">model_settings</span><span class="p">:</span> <span class="n">ModelSettings</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">usage_limits</span><span class="p">:</span> <span class="n">_usage</span><span class="o">.</span><span class="n">UsageLimits</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">usage</span><span class="p">:</span> <span class="n">_usage</span><span class="o">.</span><span class="n">Usage</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">infer_name</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AbstractAsyncContextManager</span><span class="p">[</span><span class="n">result</span><span class="o">.</span><span class="n">StreamedRunResult</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">,</span> <span class="n">RunResultDataT</span><span class="p">]]:</span> <span class="o">...</span>

    <span class="nd">@asynccontextmanager</span>
    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">run_stream</span><span class="p">(</span>  <span class="c1"># noqa C901</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">user_prompt</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">_messages</span><span class="o">.</span><span class="n">UserContent</span><span class="p">],</span>
        <span class="o">*</span><span class="p">,</span>
        <span class="n">result_type</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n">RunResultDataT</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">message_history</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">_messages</span><span class="o">.</span><span class="n">ModelMessage</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">model</span><span class="p">:</span> <span class="n">models</span><span class="o">.</span><span class="n">Model</span> <span class="o">|</span> <span class="n">models</span><span class="o">.</span><span class="n">KnownModelName</span> <span class="o">|</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">deps</span><span class="p">:</span> <span class="n">AgentDepsT</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">model_settings</span><span class="p">:</span> <span class="n">ModelSettings</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">usage_limits</span><span class="p">:</span> <span class="n">_usage</span><span class="o">.</span><span class="n">UsageLimits</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">usage</span><span class="p">:</span> <span class="n">_usage</span><span class="o">.</span><span class="n">Usage</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">infer_name</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AsyncIterator</span><span class="p">[</span><span class="n">result</span><span class="o">.</span><span class="n">StreamedRunResult</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""Run the agent with a user prompt in async mode, returning a streamed response.</span>

<span class="sd">        Example:</span>
<span class="sd">        ```python</span>
<span class="sd">        from pydantic_ai import Agent</span>

<span class="sd">        agent = Agent('openai:gpt-4o')</span>

<span class="sd">        async def main():</span>
<span class="sd">            async with agent.run_stream('What is the capital of the UK?') as response:</span>
<span class="sd">                print(await response.get_data())</span>
<span class="sd">                #&gt; London</span>
<span class="sd">        ```</span>

<span class="sd">        Args:</span>
<span class="sd">            user_prompt: User input to start/continue the conversation.</span>
<span class="sd">            result_type: Custom result type to use for this run, `result_type` may only be used if the agent has no</span>
<span class="sd">                result validators since result validators would expect an argument that matches the agent's result type.</span>
<span class="sd">            message_history: History of the conversation so far.</span>
<span class="sd">            model: Optional model to use for this run, required if `model` was not set when creating the agent.</span>
<span class="sd">            deps: Optional dependencies to use for this run.</span>
<span class="sd">            model_settings: Optional settings to use for this model's request.</span>
<span class="sd">            usage_limits: Optional limits on model request count or token usage.</span>
<span class="sd">            usage: Optional usage to start with, useful for resuming a conversation or agents used in tools.</span>
<span class="sd">            infer_name: Whether to try to infer the agent name from the call frame if it's not set.</span>

<span class="sd">        Returns:</span>
<span class="sd">            The result of the run.</span>
<span class="sd">        """</span>
        <span class="c1"># TODO: We need to deprecate this now that we have the `iter` method.</span>
        <span class="c1">#   Before that, though, we should add an event for when we reach the final result of the stream.</span>
        <span class="k">if</span> <span class="n">infer_name</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="c1"># f_back because `asynccontextmanager` adds one frame</span>
            <span class="k">if</span> <span class="n">frame</span> <span class="o">:=</span> <span class="n">inspect</span><span class="o">.</span><span class="n">currentframe</span><span class="p">():</span>  <span class="c1"># pragma: no branch</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_infer_name</span><span class="p">(</span><span class="n">frame</span><span class="o">.</span><span class="n">f_back</span><span class="p">)</span>

        <span class="n">yielded</span> <span class="o">=</span> <span class="kc">False</span>
        <span class="k">async</span> <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">iter</span><span class="p">(</span>
            <span class="n">user_prompt</span><span class="p">,</span>
            <span class="n">result_type</span><span class="o">=</span><span class="n">result_type</span><span class="p">,</span>
            <span class="n">message_history</span><span class="o">=</span><span class="n">message_history</span><span class="p">,</span>
            <span class="n">model</span><span class="o">=</span><span class="n">model</span><span class="p">,</span>
            <span class="n">deps</span><span class="o">=</span><span class="n">deps</span><span class="p">,</span>
            <span class="n">model_settings</span><span class="o">=</span><span class="n">model_settings</span><span class="p">,</span>
            <span class="n">usage_limits</span><span class="o">=</span><span class="n">usage_limits</span><span class="p">,</span>
            <span class="n">usage</span><span class="o">=</span><span class="n">usage</span><span class="p">,</span>
            <span class="n">infer_name</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
        <span class="p">)</span> <span class="k">as</span> <span class="n">agent_run</span><span class="p">:</span>
            <span class="n">first_node</span> <span class="o">=</span> <span class="n">agent_run</span><span class="o">.</span><span class="n">next_node</span>  <span class="c1"># start with the first node</span>
            <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">first_node</span><span class="p">,</span> <span class="n">_agent_graph</span><span class="o">.</span><span class="n">UserPromptNode</span><span class="p">)</span>  <span class="c1"># the first node should be a user prompt node</span>
            <span class="n">node</span> <span class="o">=</span> <span class="n">first_node</span>
            <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">is_model_request_node</span><span class="p">(</span><span class="n">node</span><span class="p">):</span>
                    <span class="n">graph_ctx</span> <span class="o">=</span> <span class="n">agent_run</span><span class="o">.</span><span class="n">ctx</span>
                    <span class="k">async</span> <span class="k">with</span> <span class="n">node</span><span class="o">.</span><span class="n">_stream</span><span class="p">(</span><span class="n">graph_ctx</span><span class="p">)</span> <span class="k">as</span> <span class="n">streamed_response</span><span class="p">:</span>  <span class="c1"># pyright: ignore[reportPrivateUsage]</span>

                        <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">stream_to_final</span><span class="p">(</span>
                            <span class="n">s</span><span class="p">:</span> <span class="n">models</span><span class="o">.</span><span class="n">StreamedResponse</span><span class="p">,</span>
                        <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">FinalResult</span><span class="p">[</span><span class="n">models</span><span class="o">.</span><span class="n">StreamedResponse</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span><span class="p">:</span>
                            <span class="n">result_schema</span> <span class="o">=</span> <span class="n">graph_ctx</span><span class="o">.</span><span class="n">deps</span><span class="o">.</span><span class="n">result_schema</span>
                            <span class="k">async</span> <span class="k">for</span> <span class="n">maybe_part_event</span> <span class="ow">in</span> <span class="n">streamed_response</span><span class="p">:</span>
                                <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">maybe_part_event</span><span class="p">,</span> <span class="n">_messages</span><span class="o">.</span><span class="n">PartStartEvent</span><span class="p">):</span>
                                    <span class="n">new_part</span> <span class="o">=</span> <span class="n">maybe_part_event</span><span class="o">.</span><span class="n">part</span>
                                    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">new_part</span><span class="p">,</span> <span class="n">_messages</span><span class="o">.</span><span class="n">TextPart</span><span class="p">):</span>
                                        <span class="k">if</span> <span class="n">_agent_graph</span><span class="o">.</span><span class="n">allow_text_result</span><span class="p">(</span><span class="n">result_schema</span><span class="p">):</span>
                                            <span class="k">return</span> <span class="n">FinalResult</span><span class="p">(</span><span class="n">s</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
                                    <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">new_part</span><span class="p">,</span> <span class="n">_messages</span><span class="o">.</span><span class="n">ToolCallPart</span><span class="p">)</span> <span class="ow">and</span> <span class="n">result_schema</span><span class="p">:</span>
                                        <span class="k">for</span> <span class="n">call</span><span class="p">,</span> <span class="n">_</span> <span class="ow">in</span> <span class="n">result_schema</span><span class="o">.</span><span class="n">find_tool</span><span class="p">([</span><span class="n">new_part</span><span class="p">]):</span>
                                            <span class="k">return</span> <span class="n">FinalResult</span><span class="p">(</span><span class="n">s</span><span class="p">,</span> <span class="n">call</span><span class="o">.</span><span class="n">tool_name</span><span class="p">,</span> <span class="n">call</span><span class="o">.</span><span class="n">tool_call_id</span><span class="p">)</span>
                            <span class="k">return</span> <span class="kc">None</span>

                        <span class="n">final_result_details</span> <span class="o">=</span> <span class="k">await</span> <span class="n">stream_to_final</span><span class="p">(</span><span class="n">streamed_response</span><span class="p">)</span>
                        <span class="k">if</span> <span class="n">final_result_details</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                            <span class="k">if</span> <span class="n">yielded</span><span class="p">:</span>
                                <span class="k">raise</span> <span class="n">exceptions</span><span class="o">.</span><span class="n">AgentRunError</span><span class="p">(</span><span class="s1">'Agent run produced final results'</span><span class="p">)</span>
                            <span class="n">yielded</span> <span class="o">=</span> <span class="kc">True</span>

                            <span class="n">messages</span> <span class="o">=</span> <span class="n">graph_ctx</span><span class="o">.</span><span class="n">state</span><span class="o">.</span><span class="n">message_history</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>

                            <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">on_complete</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">                                </span><span class="sd">"""Called when the stream has completed.</span>

<span class="sd">                                The model response will have been added to messages by now</span>
<span class="sd">                                by `StreamedRunResult._marked_completed`.</span>
<span class="sd">                                """</span>
                                <span class="n">last_message</span> <span class="o">=</span> <span class="n">messages</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>
                                <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">last_message</span><span class="p">,</span> <span class="n">_messages</span><span class="o">.</span><span class="n">ModelResponse</span><span class="p">)</span>
                                <span class="n">tool_calls</span> <span class="o">=</span> <span class="p">[</span>
                                    <span class="n">part</span> <span class="k">for</span> <span class="n">part</span> <span class="ow">in</span> <span class="n">last_message</span><span class="o">.</span><span class="n">parts</span> <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">part</span><span class="p">,</span> <span class="n">_messages</span><span class="o">.</span><span class="n">ToolCallPart</span><span class="p">)</span>
                                <span class="p">]</span>

                                <span class="n">parts</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">_messages</span><span class="o">.</span><span class="n">ModelRequestPart</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
                                <span class="k">async</span> <span class="k">for</span> <span class="n">_event</span> <span class="ow">in</span> <span class="n">_agent_graph</span><span class="o">.</span><span class="n">process_function_tools</span><span class="p">(</span>
                                    <span class="n">tool_calls</span><span class="p">,</span>
                                    <span class="n">final_result_details</span><span class="o">.</span><span class="n">tool_name</span><span class="p">,</span>
                                    <span class="n">final_result_details</span><span class="o">.</span><span class="n">tool_call_id</span><span class="p">,</span>
                                    <span class="n">graph_ctx</span><span class="p">,</span>
                                    <span class="n">parts</span><span class="p">,</span>
                                <span class="p">):</span>
                                    <span class="k">pass</span>
                                <span class="c1"># TODO: Should we do something here related to the retry count?</span>
                                <span class="c1">#   Maybe we should move the incrementing of the retry count to where we actually make a request?</span>
                                <span class="c1"># if any(isinstance(part, _messages.RetryPromptPart) for part in parts):</span>
                                <span class="c1">#     ctx.state.increment_retries(ctx.deps.max_result_retries)</span>
                                <span class="k">if</span> <span class="n">parts</span><span class="p">:</span>
                                    <span class="n">messages</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">_messages</span><span class="o">.</span><span class="n">ModelRequest</span><span class="p">(</span><span class="n">parts</span><span class="p">))</span>

                            <span class="k">yield</span> <span class="n">StreamedRunResult</span><span class="p">(</span>
                                <span class="n">messages</span><span class="p">,</span>
                                <span class="n">graph_ctx</span><span class="o">.</span><span class="n">deps</span><span class="o">.</span><span class="n">new_message_index</span><span class="p">,</span>
                                <span class="n">graph_ctx</span><span class="o">.</span><span class="n">deps</span><span class="o">.</span><span class="n">usage_limits</span><span class="p">,</span>
                                <span class="n">streamed_response</span><span class="p">,</span>
                                <span class="n">graph_ctx</span><span class="o">.</span><span class="n">deps</span><span class="o">.</span><span class="n">result_schema</span><span class="p">,</span>
                                <span class="n">_agent_graph</span><span class="o">.</span><span class="n">build_run_context</span><span class="p">(</span><span class="n">graph_ctx</span><span class="p">),</span>
                                <span class="n">graph_ctx</span><span class="o">.</span><span class="n">deps</span><span class="o">.</span><span class="n">result_validators</span><span class="p">,</span>
                                <span class="n">final_result_details</span><span class="o">.</span><span class="n">tool_name</span><span class="p">,</span>
                                <span class="n">on_complete</span><span class="p">,</span>
                            <span class="p">)</span>
                            <span class="k">break</span>
                <span class="n">next_node</span> <span class="o">=</span> <span class="k">await</span> <span class="n">agent_run</span><span class="o">.</span><span class="n">next</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
                <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">next_node</span><span class="p">,</span> <span class="n">_agent_graph</span><span class="o">.</span><span class="n">AgentNode</span><span class="p">):</span>
                    <span class="k">raise</span> <span class="n">exceptions</span><span class="o">.</span><span class="n">AgentRunError</span><span class="p">(</span><span class="s1">'Should have produced a StreamedRunResult before getting here'</span><span class="p">)</span>
                <span class="n">node</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">_agent_graph</span><span class="o">.</span><span class="n">AgentNode</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span> <span class="n">next_node</span><span class="p">)</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="n">yielded</span><span class="p">:</span>
            <span class="k">raise</span> <span class="n">exceptions</span><span class="o">.</span><span class="n">AgentRunError</span><span class="p">(</span><span class="s1">'Agent run finished without producing a final result'</span><span class="p">)</span>

    <span class="nd">@contextmanager</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">override</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="o">*</span><span class="p">,</span>
        <span class="n">deps</span><span class="p">:</span> <span class="n">AgentDepsT</span> <span class="o">|</span> <span class="n">_utils</span><span class="o">.</span><span class="n">Unset</span> <span class="o">=</span> <span class="n">_utils</span><span class="o">.</span><span class="n">UNSET</span><span class="p">,</span>
        <span class="n">model</span><span class="p">:</span> <span class="n">models</span><span class="o">.</span><span class="n">Model</span> <span class="o">|</span> <span class="n">models</span><span class="o">.</span><span class="n">KnownModelName</span> <span class="o">|</span> <span class="nb">str</span> <span class="o">|</span> <span class="n">_utils</span><span class="o">.</span><span class="n">Unset</span> <span class="o">=</span> <span class="n">_utils</span><span class="o">.</span><span class="n">UNSET</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Iterator</span><span class="p">[</span><span class="kc">None</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Context manager to temporarily override agent dependencies and model.</span>

<span class="sd">        This is particularly useful when testing.</span>
<span class="sd">        You can find an example of this [here](../testing.md#overriding-model-via-pytest-fixtures).</span>

<span class="sd">        Args:</span>
<span class="sd">            deps: The dependencies to use instead of the dependencies passed to the agent run.</span>
<span class="sd">            model: The model to use instead of the model passed to the agent run.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">_utils</span><span class="o">.</span><span class="n">is_set</span><span class="p">(</span><span class="n">deps</span><span class="p">):</span>
            <span class="n">override_deps_before</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_override_deps</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_override_deps</span> <span class="o">=</span> <span class="n">_utils</span><span class="o">.</span><span class="n">Some</span><span class="p">(</span><span class="n">deps</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">override_deps_before</span> <span class="o">=</span> <span class="n">_utils</span><span class="o">.</span><span class="n">UNSET</span>

        <span class="k">if</span> <span class="n">_utils</span><span class="o">.</span><span class="n">is_set</span><span class="p">(</span><span class="n">model</span><span class="p">):</span>
            <span class="n">override_model_before</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_override_model</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_override_model</span> <span class="o">=</span> <span class="n">_utils</span><span class="o">.</span><span class="n">Some</span><span class="p">(</span><span class="n">models</span><span class="o">.</span><span class="n">infer_model</span><span class="p">(</span><span class="n">model</span><span class="p">))</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">override_model_before</span> <span class="o">=</span> <span class="n">_utils</span><span class="o">.</span><span class="n">UNSET</span>

        <span class="k">try</span><span class="p">:</span>
            <span class="k">yield</span>
        <span class="k">finally</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">_utils</span><span class="o">.</span><span class="n">is_set</span><span class="p">(</span><span class="n">override_deps_before</span><span class="p">):</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_override_deps</span> <span class="o">=</span> <span class="n">override_deps_before</span>
            <span class="k">if</span> <span class="n">_utils</span><span class="o">.</span><span class="n">is_set</span><span class="p">(</span><span class="n">override_model_before</span><span class="p">):</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_override_model</span> <span class="o">=</span> <span class="n">override_model_before</span>

    <span class="nd">@overload</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">system_prompt</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">func</span><span class="p">:</span> <span class="n">Callable</span><span class="p">[[</span><span class="n">RunContext</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">]],</span> <span class="nb">str</span><span class="p">],</span> <span class="o">/</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Callable</span><span class="p">[[</span><span class="n">RunContext</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">]],</span> <span class="nb">str</span><span class="p">]:</span> <span class="o">...</span>

    <span class="nd">@overload</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">system_prompt</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">func</span><span class="p">:</span> <span class="n">Callable</span><span class="p">[[</span><span class="n">RunContext</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">]],</span> <span class="n">Awaitable</span><span class="p">[</span><span class="nb">str</span><span class="p">]],</span> <span class="o">/</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Callable</span><span class="p">[[</span><span class="n">RunContext</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">]],</span> <span class="n">Awaitable</span><span class="p">[</span><span class="nb">str</span><span class="p">]]:</span> <span class="o">...</span>

    <span class="nd">@overload</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">system_prompt</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">func</span><span class="p">:</span> <span class="n">Callable</span><span class="p">[[],</span> <span class="nb">str</span><span class="p">],</span> <span class="o">/</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Callable</span><span class="p">[[],</span> <span class="nb">str</span><span class="p">]:</span> <span class="o">...</span>

    <span class="nd">@overload</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">system_prompt</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">func</span><span class="p">:</span> <span class="n">Callable</span><span class="p">[[],</span> <span class="n">Awaitable</span><span class="p">[</span><span class="nb">str</span><span class="p">]],</span> <span class="o">/</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Callable</span><span class="p">[[],</span> <span class="n">Awaitable</span><span class="p">[</span><span class="nb">str</span><span class="p">]]:</span> <span class="o">...</span>

    <span class="nd">@overload</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">system_prompt</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="o">/</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">dynamic</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Callable</span><span class="p">[[</span><span class="n">_system_prompt</span><span class="o">.</span><span class="n">SystemPromptFunc</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">]],</span> <span class="n">_system_prompt</span><span class="o">.</span><span class="n">SystemPromptFunc</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">]]:</span> <span class="o">...</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">system_prompt</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">func</span><span class="p">:</span> <span class="n">_system_prompt</span><span class="o">.</span><span class="n">SystemPromptFunc</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">/</span><span class="p">,</span>
        <span class="o">*</span><span class="p">,</span>
        <span class="n">dynamic</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="p">(</span>
        <span class="n">Callable</span><span class="p">[[</span><span class="n">_system_prompt</span><span class="o">.</span><span class="n">SystemPromptFunc</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">]],</span> <span class="n">_system_prompt</span><span class="o">.</span><span class="n">SystemPromptFunc</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">]]</span>
        <span class="o">|</span> <span class="n">_system_prompt</span><span class="o">.</span><span class="n">SystemPromptFunc</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">]</span>
    <span class="p">):</span>
<span class="w">        </span><span class="sd">"""Decorator to register a system prompt function.</span>

<span class="sd">        Optionally takes [`RunContext`][pydantic_ai.tools.RunContext] as its only argument.</span>
<span class="sd">        Can decorate a sync or async functions.</span>

<span class="sd">        The decorator can be used either bare (`agent.system_prompt`) or as a function call</span>
<span class="sd">        (`agent.system_prompt(...)`), see the examples below.</span>

<span class="sd">        Overloads for every possible signature of `system_prompt` are included so the decorator doesn't obscure</span>
<span class="sd">        the type of the function, see `tests/typed_agent.py` for tests.</span>

<span class="sd">        Args:</span>
<span class="sd">            func: The function to decorate</span>
<span class="sd">            dynamic: If True, the system prompt will be reevaluated even when `messages_history` is provided,</span>
<span class="sd">                see [`SystemPromptPart.dynamic_ref`][pydantic_ai.messages.SystemPromptPart.dynamic_ref]</span>

<span class="sd">        Example:</span>
<span class="sd">        ```python</span>
<span class="sd">        from pydantic_ai import Agent, RunContext</span>

<span class="sd">        agent = Agent('test', deps_type=str)</span>

<span class="sd">        @agent.system_prompt</span>
<span class="sd">        def simple_system_prompt() -&gt; str:</span>
<span class="sd">            return 'foobar'</span>

<span class="sd">        @agent.system_prompt(dynamic=True)</span>
<span class="sd">        async def async_system_prompt(ctx: RunContext[str]) -&gt; str:</span>
<span class="sd">            return f'{ctx.deps} is the best'</span>
<span class="sd">        ```</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">func</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>

            <span class="k">def</span><span class="w"> </span><span class="nf">decorator</span><span class="p">(</span>
                <span class="n">func_</span><span class="p">:</span> <span class="n">_system_prompt</span><span class="o">.</span><span class="n">SystemPromptFunc</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">],</span>
            <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">_system_prompt</span><span class="o">.</span><span class="n">SystemPromptFunc</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">]:</span>
                <span class="n">runner</span> <span class="o">=</span> <span class="n">_system_prompt</span><span class="o">.</span><span class="n">SystemPromptRunner</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">](</span><span class="n">func_</span><span class="p">,</span> <span class="n">dynamic</span><span class="o">=</span><span class="n">dynamic</span><span class="p">)</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_system_prompt_functions</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">runner</span><span class="p">)</span>
                <span class="k">if</span> <span class="n">dynamic</span><span class="p">:</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">_system_prompt_dynamic_functions</span><span class="p">[</span><span class="n">func_</span><span class="o">.</span><span class="vm">__qualname__</span><span class="p">]</span> <span class="o">=</span> <span class="n">runner</span>
                <span class="k">return</span> <span class="n">func_</span>

            <span class="k">return</span> <span class="n">decorator</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">assert</span> <span class="ow">not</span> <span class="n">dynamic</span><span class="p">,</span> <span class="s2">"dynamic can't be True in this case"</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_system_prompt_functions</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">_system_prompt</span><span class="o">.</span><span class="n">SystemPromptRunner</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">](</span><span class="n">func</span><span class="p">,</span> <span class="n">dynamic</span><span class="o">=</span><span class="n">dynamic</span><span class="p">))</span>
            <span class="k">return</span> <span class="n">func</span>

    <span class="nd">@overload</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">result_validator</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">func</span><span class="p">:</span> <span class="n">Callable</span><span class="p">[[</span><span class="n">RunContext</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">],</span> <span class="n">ResultDataT</span><span class="p">],</span> <span class="n">ResultDataT</span><span class="p">],</span> <span class="o">/</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Callable</span><span class="p">[[</span><span class="n">RunContext</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">],</span> <span class="n">ResultDataT</span><span class="p">],</span> <span class="n">ResultDataT</span><span class="p">]:</span> <span class="o">...</span>

    <span class="nd">@overload</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">result_validator</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">func</span><span class="p">:</span> <span class="n">Callable</span><span class="p">[[</span><span class="n">RunContext</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">],</span> <span class="n">ResultDataT</span><span class="p">],</span> <span class="n">Awaitable</span><span class="p">[</span><span class="n">ResultDataT</span><span class="p">]],</span> <span class="o">/</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Callable</span><span class="p">[[</span><span class="n">RunContext</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">],</span> <span class="n">ResultDataT</span><span class="p">],</span> <span class="n">Awaitable</span><span class="p">[</span><span class="n">ResultDataT</span><span class="p">]]:</span> <span class="o">...</span>

    <span class="nd">@overload</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">result_validator</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">func</span><span class="p">:</span> <span class="n">Callable</span><span class="p">[[</span><span class="n">ResultDataT</span><span class="p">],</span> <span class="n">ResultDataT</span><span class="p">],</span> <span class="o">/</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Callable</span><span class="p">[[</span><span class="n">ResultDataT</span><span class="p">],</span> <span class="n">ResultDataT</span><span class="p">]:</span> <span class="o">...</span>

    <span class="nd">@overload</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">result_validator</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">func</span><span class="p">:</span> <span class="n">Callable</span><span class="p">[[</span><span class="n">ResultDataT</span><span class="p">],</span> <span class="n">Awaitable</span><span class="p">[</span><span class="n">ResultDataT</span><span class="p">]],</span> <span class="o">/</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Callable</span><span class="p">[[</span><span class="n">ResultDataT</span><span class="p">],</span> <span class="n">Awaitable</span><span class="p">[</span><span class="n">ResultDataT</span><span class="p">]]:</span> <span class="o">...</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">result_validator</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">func</span><span class="p">:</span> <span class="n">_result</span><span class="o">.</span><span class="n">ResultValidatorFunc</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">,</span> <span class="n">ResultDataT</span><span class="p">],</span> <span class="o">/</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">_result</span><span class="o">.</span><span class="n">ResultValidatorFunc</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">,</span> <span class="n">ResultDataT</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Decorator to register a result validator function.</span>

<span class="sd">        Optionally takes [`RunContext`][pydantic_ai.tools.RunContext] as its first argument.</span>
<span class="sd">        Can decorate a sync or async functions.</span>

<span class="sd">        Overloads for every possible signature of `result_validator` are included so the decorator doesn't obscure</span>
<span class="sd">        the type of the function, see `tests/typed_agent.py` for tests.</span>

<span class="sd">        Example:</span>
<span class="sd">        ```python</span>
<span class="sd">        from pydantic_ai import Agent, ModelRetry, RunContext</span>

<span class="sd">        agent = Agent('test', deps_type=str)</span>

<span class="sd">        @agent.result_validator</span>
<span class="sd">        def result_validator_simple(data: str) -&gt; str:</span>
<span class="sd">            if 'wrong' in data:</span>
<span class="sd">                raise ModelRetry('wrong response')</span>
<span class="sd">            return data</span>

<span class="sd">        @agent.result_validator</span>
<span class="sd">        async def result_validator_deps(ctx: RunContext[str], data: str) -&gt; str:</span>
<span class="sd">            if ctx.deps in data:</span>
<span class="sd">                raise ModelRetry('wrong response')</span>
<span class="sd">            return data</span>

<span class="sd">        result = agent.run_sync('foobar', deps='spam')</span>
<span class="sd">        print(result.data)</span>
<span class="sd">        #&gt; success (no tool calls)</span>
<span class="sd">        ```</span>
<span class="sd">        """</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_result_validators</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">_result</span><span class="o">.</span><span class="n">ResultValidator</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">,</span> <span class="n">Any</span><span class="p">](</span><span class="n">func</span><span class="p">))</span>
        <span class="k">return</span> <span class="n">func</span>

    <span class="nd">@overload</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">tool</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">func</span><span class="p">:</span> <span class="n">ToolFuncContext</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">,</span> <span class="n">ToolParams</span><span class="p">],</span> <span class="o">/</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ToolFuncContext</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">,</span> <span class="n">ToolParams</span><span class="p">]:</span> <span class="o">...</span>

    <span class="nd">@overload</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">tool</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="o">/</span><span class="p">,</span>
        <span class="o">*</span><span class="p">,</span>
        <span class="n">name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">retries</span><span class="p">:</span> <span class="nb">int</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">prepare</span><span class="p">:</span> <span class="n">ToolPrepareFunc</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">docstring_format</span><span class="p">:</span> <span class="n">DocstringFormat</span> <span class="o">=</span> <span class="s1">'auto'</span><span class="p">,</span>
        <span class="n">require_parameter_descriptions</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">schema_generator</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n">GenerateJsonSchema</span><span class="p">]</span> <span class="o">=</span> <span class="n">GenerateToolJsonSchema</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Callable</span><span class="p">[[</span><span class="n">ToolFuncContext</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">,</span> <span class="n">ToolParams</span><span class="p">]],</span> <span class="n">ToolFuncContext</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">,</span> <span class="n">ToolParams</span><span class="p">]]:</span> <span class="o">...</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">tool</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">func</span><span class="p">:</span> <span class="n">ToolFuncContext</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">,</span> <span class="n">ToolParams</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">/</span><span class="p">,</span>
        <span class="o">*</span><span class="p">,</span>
        <span class="n">name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">retries</span><span class="p">:</span> <span class="nb">int</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">prepare</span><span class="p">:</span> <span class="n">ToolPrepareFunc</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">docstring_format</span><span class="p">:</span> <span class="n">DocstringFormat</span> <span class="o">=</span> <span class="s1">'auto'</span><span class="p">,</span>
        <span class="n">require_parameter_descriptions</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">schema_generator</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n">GenerateJsonSchema</span><span class="p">]</span> <span class="o">=</span> <span class="n">GenerateToolJsonSchema</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Decorator to register a tool function which takes [`RunContext`][pydantic_ai.tools.RunContext] as its first argument.</span>

<span class="sd">        Can decorate a sync or async functions.</span>

<span class="sd">        The docstring is inspected to extract both the tool description and description of each parameter,</span>
<span class="sd">        [learn more](../tools.md#function-tools-and-schema).</span>

<span class="sd">        We can't add overloads for every possible signature of tool, since the return type is a recursive union</span>
<span class="sd">        so the signature of functions decorated with `@agent.tool` is obscured.</span>

<span class="sd">        Example:</span>
<span class="sd">        ```python</span>
<span class="sd">        from pydantic_ai import Agent, RunContext</span>

<span class="sd">        agent = Agent('test', deps_type=int)</span>

<span class="sd">        @agent.tool</span>
<span class="sd">        def foobar(ctx: RunContext[int], x: int) -&gt; int:</span>
<span class="sd">            return ctx.deps + x</span>

<span class="sd">        @agent.tool(retries=2)</span>
<span class="sd">        async def spam(ctx: RunContext[str], y: float) -&gt; float:</span>
<span class="sd">            return ctx.deps + y</span>

<span class="sd">        result = agent.run_sync('foobar', deps=1)</span>
<span class="sd">        print(result.data)</span>
<span class="sd">        #&gt; {"foobar":1,"spam":1.0}</span>
<span class="sd">        ```</span>

<span class="sd">        Args:</span>
<span class="sd">            func: The tool function to register.</span>
<span class="sd">            name: The name of the tool, defaults to the function name.</span>
<span class="sd">            retries: The number of retries to allow for this tool, defaults to the agent's default retries,</span>
<span class="sd">                which defaults to 1.</span>
<span class="sd">            prepare: custom method to prepare the tool definition for each step, return `None` to omit this</span>
<span class="sd">                tool from a given step. This is useful if you want to customise a tool at call time,</span>
<span class="sd">                or omit it completely from a step. See [`ToolPrepareFunc`][pydantic_ai.tools.ToolPrepareFunc].</span>
<span class="sd">            docstring_format: The format of the docstring, see [`DocstringFormat`][pydantic_ai.tools.DocstringFormat].</span>
<span class="sd">                Defaults to `'auto'`, such that the format is inferred from the structure of the docstring.</span>
<span class="sd">            require_parameter_descriptions: If True, raise an error if a parameter description is missing. Defaults to False.</span>
<span class="sd">            schema_generator: The JSON schema generator class to use for this tool. Defaults to `GenerateToolJsonSchema`.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">func</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>

            <span class="k">def</span><span class="w"> </span><span class="nf">tool_decorator</span><span class="p">(</span>
                <span class="n">func_</span><span class="p">:</span> <span class="n">ToolFuncContext</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">,</span> <span class="n">ToolParams</span><span class="p">],</span>
            <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ToolFuncContext</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">,</span> <span class="n">ToolParams</span><span class="p">]:</span>
                <span class="c1"># noinspection PyTypeChecker</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_register_function</span><span class="p">(</span>
                    <span class="n">func_</span><span class="p">,</span>
                    <span class="kc">True</span><span class="p">,</span>
                    <span class="n">name</span><span class="p">,</span>
                    <span class="n">retries</span><span class="p">,</span>
                    <span class="n">prepare</span><span class="p">,</span>
                    <span class="n">docstring_format</span><span class="p">,</span>
                    <span class="n">require_parameter_descriptions</span><span class="p">,</span>
                    <span class="n">schema_generator</span><span class="p">,</span>
                <span class="p">)</span>
                <span class="k">return</span> <span class="n">func_</span>

            <span class="k">return</span> <span class="n">tool_decorator</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="c1"># noinspection PyTypeChecker</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_register_function</span><span class="p">(</span>
                <span class="n">func</span><span class="p">,</span> <span class="kc">True</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span> <span class="n">retries</span><span class="p">,</span> <span class="n">prepare</span><span class="p">,</span> <span class="n">docstring_format</span><span class="p">,</span> <span class="n">require_parameter_descriptions</span><span class="p">,</span> <span class="n">schema_generator</span>
            <span class="p">)</span>
            <span class="k">return</span> <span class="n">func</span>

    <span class="nd">@overload</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">tool_plain</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">func</span><span class="p">:</span> <span class="n">ToolFuncPlain</span><span class="p">[</span><span class="n">ToolParams</span><span class="p">],</span> <span class="o">/</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ToolFuncPlain</span><span class="p">[</span><span class="n">ToolParams</span><span class="p">]:</span> <span class="o">...</span>

    <span class="nd">@overload</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">tool_plain</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="o">/</span><span class="p">,</span>
        <span class="o">*</span><span class="p">,</span>
        <span class="n">name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">retries</span><span class="p">:</span> <span class="nb">int</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">prepare</span><span class="p">:</span> <span class="n">ToolPrepareFunc</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">docstring_format</span><span class="p">:</span> <span class="n">DocstringFormat</span> <span class="o">=</span> <span class="s1">'auto'</span><span class="p">,</span>
        <span class="n">require_parameter_descriptions</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">schema_generator</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n">GenerateJsonSchema</span><span class="p">]</span> <span class="o">=</span> <span class="n">GenerateToolJsonSchema</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Callable</span><span class="p">[[</span><span class="n">ToolFuncPlain</span><span class="p">[</span><span class="n">ToolParams</span><span class="p">]],</span> <span class="n">ToolFuncPlain</span><span class="p">[</span><span class="n">ToolParams</span><span class="p">]]:</span> <span class="o">...</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">tool_plain</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">func</span><span class="p">:</span> <span class="n">ToolFuncPlain</span><span class="p">[</span><span class="n">ToolParams</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">/</span><span class="p">,</span>
        <span class="o">*</span><span class="p">,</span>
        <span class="n">name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">retries</span><span class="p">:</span> <span class="nb">int</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">prepare</span><span class="p">:</span> <span class="n">ToolPrepareFunc</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">docstring_format</span><span class="p">:</span> <span class="n">DocstringFormat</span> <span class="o">=</span> <span class="s1">'auto'</span><span class="p">,</span>
        <span class="n">require_parameter_descriptions</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">schema_generator</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n">GenerateJsonSchema</span><span class="p">]</span> <span class="o">=</span> <span class="n">GenerateToolJsonSchema</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Decorator to register a tool function which DOES NOT take `RunContext` as an argument.</span>

<span class="sd">        Can decorate a sync or async functions.</span>

<span class="sd">        The docstring is inspected to extract both the tool description and description of each parameter,</span>
<span class="sd">        [learn more](../tools.md#function-tools-and-schema).</span>

<span class="sd">        We can't add overloads for every possible signature of tool, since the return type is a recursive union</span>
<span class="sd">        so the signature of functions decorated with `@agent.tool` is obscured.</span>

<span class="sd">        Example:</span>
<span class="sd">        ```python</span>
<span class="sd">        from pydantic_ai import Agent, RunContext</span>

<span class="sd">        agent = Agent('test')</span>

<span class="sd">        @agent.tool</span>
<span class="sd">        def foobar(ctx: RunContext[int]) -&gt; int:</span>
<span class="sd">            return 123</span>

<span class="sd">        @agent.tool(retries=2)</span>
<span class="sd">        async def spam(ctx: RunContext[str]) -&gt; float:</span>
<span class="sd">            return 3.14</span>

<span class="sd">        result = agent.run_sync('foobar', deps=1)</span>
<span class="sd">        print(result.data)</span>
<span class="sd">        #&gt; {"foobar":123,"spam":3.14}</span>
<span class="sd">        ```</span>

<span class="sd">        Args:</span>
<span class="sd">            func: The tool function to register.</span>
<span class="sd">            name: The name of the tool, defaults to the function name.</span>
<span class="sd">            retries: The number of retries to allow for this tool, defaults to the agent's default retries,</span>
<span class="sd">                which defaults to 1.</span>
<span class="sd">            prepare: custom method to prepare the tool definition for each step, return `None` to omit this</span>
<span class="sd">                tool from a given step. This is useful if you want to customise a tool at call time,</span>
<span class="sd">                or omit it completely from a step. See [`ToolPrepareFunc`][pydantic_ai.tools.ToolPrepareFunc].</span>
<span class="sd">            docstring_format: The format of the docstring, see [`DocstringFormat`][pydantic_ai.tools.DocstringFormat].</span>
<span class="sd">                Defaults to `'auto'`, such that the format is inferred from the structure of the docstring.</span>
<span class="sd">            require_parameter_descriptions: If True, raise an error if a parameter description is missing. Defaults to False.</span>
<span class="sd">            schema_generator: The JSON schema generator class to use for this tool. Defaults to `GenerateToolJsonSchema`.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">func</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>

            <span class="k">def</span><span class="w"> </span><span class="nf">tool_decorator</span><span class="p">(</span><span class="n">func_</span><span class="p">:</span> <span class="n">ToolFuncPlain</span><span class="p">[</span><span class="n">ToolParams</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">ToolFuncPlain</span><span class="p">[</span><span class="n">ToolParams</span><span class="p">]:</span>
                <span class="c1"># noinspection PyTypeChecker</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_register_function</span><span class="p">(</span>
                    <span class="n">func_</span><span class="p">,</span>
                    <span class="kc">False</span><span class="p">,</span>
                    <span class="n">name</span><span class="p">,</span>
                    <span class="n">retries</span><span class="p">,</span>
                    <span class="n">prepare</span><span class="p">,</span>
                    <span class="n">docstring_format</span><span class="p">,</span>
                    <span class="n">require_parameter_descriptions</span><span class="p">,</span>
                    <span class="n">schema_generator</span><span class="p">,</span>
                <span class="p">)</span>
                <span class="k">return</span> <span class="n">func_</span>

            <span class="k">return</span> <span class="n">tool_decorator</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_register_function</span><span class="p">(</span>
                <span class="n">func</span><span class="p">,</span> <span class="kc">False</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span> <span class="n">retries</span><span class="p">,</span> <span class="n">prepare</span><span class="p">,</span> <span class="n">docstring_format</span><span class="p">,</span> <span class="n">require_parameter_descriptions</span><span class="p">,</span> <span class="n">schema_generator</span>
            <span class="p">)</span>
            <span class="k">return</span> <span class="n">func</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">_register_function</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">func</span><span class="p">:</span> <span class="n">ToolFuncEither</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">,</span> <span class="n">ToolParams</span><span class="p">],</span>
        <span class="n">takes_ctx</span><span class="p">:</span> <span class="nb">bool</span><span class="p">,</span>
        <span class="n">name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">retries</span><span class="p">:</span> <span class="nb">int</span> <span class="o">|</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">prepare</span><span class="p">:</span> <span class="n">ToolPrepareFunc</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">docstring_format</span><span class="p">:</span> <span class="n">DocstringFormat</span><span class="p">,</span>
        <span class="n">require_parameter_descriptions</span><span class="p">:</span> <span class="nb">bool</span><span class="p">,</span>
        <span class="n">schema_generator</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n">GenerateJsonSchema</span><span class="p">],</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Private utility to register a function as a tool."""</span>
        <span class="n">retries_</span> <span class="o">=</span> <span class="n">retries</span> <span class="k">if</span> <span class="n">retries</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="k">else</span> <span class="bp">self</span><span class="o">.</span><span class="n">_default_retries</span>
        <span class="n">tool</span> <span class="o">=</span> <span class="n">Tool</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">](</span>
            <span class="n">func</span><span class="p">,</span>
            <span class="n">takes_ctx</span><span class="o">=</span><span class="n">takes_ctx</span><span class="p">,</span>
            <span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="p">,</span>
            <span class="n">max_retries</span><span class="o">=</span><span class="n">retries_</span><span class="p">,</span>
            <span class="n">prepare</span><span class="o">=</span><span class="n">prepare</span><span class="p">,</span>
            <span class="n">docstring_format</span><span class="o">=</span><span class="n">docstring_format</span><span class="p">,</span>
            <span class="n">require_parameter_descriptions</span><span class="o">=</span><span class="n">require_parameter_descriptions</span><span class="p">,</span>
            <span class="n">schema_generator</span><span class="o">=</span><span class="n">schema_generator</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_register_tool</span><span class="p">(</span><span class="n">tool</span><span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">_register_tool</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tool</span><span class="p">:</span> <span class="n">Tool</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Private utility to register a tool instance."""</span>
        <span class="k">if</span> <span class="n">tool</span><span class="o">.</span><span class="n">max_retries</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="c1"># noinspection PyTypeChecker</span>
            <span class="n">tool</span> <span class="o">=</span> <span class="n">dataclasses</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="n">tool</span><span class="p">,</span> <span class="n">max_retries</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_default_retries</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">tool</span><span class="o">.</span><span class="n">name</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_function_tools</span><span class="p">:</span>
            <span class="k">raise</span> <span class="n">exceptions</span><span class="o">.</span><span class="n">UserError</span><span class="p">(</span><span class="sa">f</span><span class="s1">'Tool name conflicts with existing tool: </span><span class="si">{</span><span class="n">tool</span><span class="o">.</span><span class="n">name</span><span class="si">!r}</span><span class="s1">'</span><span class="p">)</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_result_schema</span> <span class="ow">and</span> <span class="n">tool</span><span class="o">.</span><span class="n">name</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_result_schema</span><span class="o">.</span><span class="n">tools</span><span class="p">:</span>
            <span class="k">raise</span> <span class="n">exceptions</span><span class="o">.</span><span class="n">UserError</span><span class="p">(</span><span class="sa">f</span><span class="s1">'Tool name conflicts with result schema name: </span><span class="si">{</span><span class="n">tool</span><span class="o">.</span><span class="n">name</span><span class="si">!r}</span><span class="s1">'</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_function_tools</span><span class="p">[</span><span class="n">tool</span><span class="o">.</span><span class="n">name</span><span class="p">]</span> <span class="o">=</span> <span class="n">tool</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">_get_model</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">model</span><span class="p">:</span> <span class="n">models</span><span class="o">.</span><span class="n">Model</span> <span class="o">|</span> <span class="n">models</span><span class="o">.</span><span class="n">KnownModelName</span> <span class="o">|</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">models</span><span class="o">.</span><span class="n">Model</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Create a model configured for this agent.</span>

<span class="sd">        Args:</span>
<span class="sd">            model: model to use for this run, required if `model` was not set when creating the agent.</span>

<span class="sd">        Returns:</span>
<span class="sd">            The model used</span>
<span class="sd">        """</span>
        <span class="n">model_</span><span class="p">:</span> <span class="n">models</span><span class="o">.</span><span class="n">Model</span>
        <span class="k">if</span> <span class="n">some_model</span> <span class="o">:=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_override_model</span><span class="p">:</span>
            <span class="c1"># we don't want `override()` to cover up errors from the model not being defined, hence this check</span>
            <span class="k">if</span> <span class="n">model</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">model</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                <span class="k">raise</span> <span class="n">exceptions</span><span class="o">.</span><span class="n">UserError</span><span class="p">(</span>
                    <span class="s1">'`model` must either be set on the agent or included when calling it. '</span>
                    <span class="s1">'(Even when `override(model=...)` is customizing the model that will actually be called)'</span>
                <span class="p">)</span>
            <span class="n">model_</span> <span class="o">=</span> <span class="n">some_model</span><span class="o">.</span><span class="n">value</span>
        <span class="k">elif</span> <span class="n">model</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">model_</span> <span class="o">=</span> <span class="n">models</span><span class="o">.</span><span class="n">infer_model</span><span class="p">(</span><span class="n">model</span><span class="p">)</span>
        <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">model</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="c1"># noinspection PyTypeChecker</span>
            <span class="n">model_</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">model</span> <span class="o">=</span> <span class="n">models</span><span class="o">.</span><span class="n">infer_model</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">model</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="n">exceptions</span><span class="o">.</span><span class="n">UserError</span><span class="p">(</span><span class="s1">'`model` must either be set on the agent or included when calling it.'</span><span class="p">)</span>

        <span class="n">instrument</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">instrument</span>
        <span class="k">if</span> <span class="n">instrument</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">instrument</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_instrument_default</span>

        <span class="k">if</span> <span class="n">instrument</span> <span class="ow">and</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">model_</span><span class="p">,</span> <span class="n">InstrumentedModel</span><span class="p">):</span>
            <span class="k">if</span> <span class="n">instrument</span> <span class="ow">is</span> <span class="kc">True</span><span class="p">:</span>
                <span class="n">instrument</span> <span class="o">=</span> <span class="n">InstrumentationSettings</span><span class="p">()</span>

            <span class="n">model_</span> <span class="o">=</span> <span class="n">InstrumentedModel</span><span class="p">(</span><span class="n">model_</span><span class="p">,</span> <span class="n">instrument</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">model_</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">_get_deps</span><span class="p">(</span><span class="bp">self</span><span class="p">:</span> <span class="n">Agent</span><span class="p">[</span><span class="n">T</span><span class="p">,</span> <span class="n">ResultDataT</span><span class="p">],</span> <span class="n">deps</span><span class="p">:</span> <span class="n">T</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">T</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get deps for a run.</span>

<span class="sd">        If we've overridden deps via `_override_deps`, use that, otherwise use the deps passed to the call.</span>

<span class="sd">        We could do runtime type checking of deps against `self._deps_type`, but that's a slippery slope.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">some_deps</span> <span class="o">:=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_override_deps</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">some_deps</span><span class="o">.</span><span class="n">value</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">deps</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">_infer_name</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">function_frame</span><span class="p">:</span> <span class="n">FrameType</span> <span class="o">|</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Infer the agent name from the call frame.</span>

<span class="sd">        Usage should be `self._infer_name(inspect.currentframe())`.</span>
<span class="sd">        """</span>
        <span class="k">assert</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">,</span> <span class="s1">'Name already set'</span>
        <span class="k">if</span> <span class="n">function_frame</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>  <span class="c1"># pragma: no branch</span>
            <span class="k">if</span> <span class="n">parent_frame</span> <span class="o">:=</span> <span class="n">function_frame</span><span class="o">.</span><span class="n">f_back</span><span class="p">:</span>  <span class="c1"># pragma: no branch</span>
                <span class="k">for</span> <span class="n">name</span><span class="p">,</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">parent_frame</span><span class="o">.</span><span class="n">f_locals</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
                    <span class="k">if</span> <span class="n">item</span> <span class="ow">is</span> <span class="bp">self</span><span class="p">:</span>
                        <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="o">=</span> <span class="n">name</span>
                        <span class="k">return</span>
                <span class="k">if</span> <span class="n">parent_frame</span><span class="o">.</span><span class="n">f_locals</span> <span class="o">!=</span> <span class="n">parent_frame</span><span class="o">.</span><span class="n">f_globals</span><span class="p">:</span>
                    <span class="c1"># if we couldn't find the agent in locals and globals are a different dict, try globals</span>
                    <span class="k">for</span> <span class="n">name</span><span class="p">,</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">parent_frame</span><span class="o">.</span><span class="n">f_globals</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
                        <span class="k">if</span> <span class="n">item</span> <span class="ow">is</span> <span class="bp">self</span><span class="p">:</span>
                            <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="o">=</span> <span class="n">name</span>
                            <span class="k">return</span>

    <span class="nd">@property</span>
    <span class="nd">@deprecated</span><span class="p">(</span>
        <span class="s1">'The `last_run_messages` attribute has been removed, use `capture_run_messages` instead.'</span><span class="p">,</span> <span class="n">category</span><span class="o">=</span><span class="kc">None</span>
    <span class="p">)</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">last_run_messages</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">list</span><span class="p">[</span><span class="n">_messages</span><span class="o">.</span><span class="n">ModelMessage</span><span class="p">]:</span>
        <span class="k">raise</span> <span class="ne">AttributeError</span><span class="p">(</span><span class="s1">'The `last_run_messages` attribute has been removed, use `capture_run_messages` instead.'</span><span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">_build_graph</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">result_type</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n">RunResultDataT</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Graph</span><span class="p">[</span><span class="n">_agent_graph</span><span class="o">.</span><span class="n">GraphAgentState</span><span class="p">,</span> <span class="n">_agent_graph</span><span class="o">.</span><span class="n">GraphAgentDeps</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span> <span class="n">FinalResult</span><span class="p">[</span><span class="n">Any</span><span class="p">]]:</span>
        <span class="k">return</span> <span class="n">_agent_graph</span><span class="o">.</span><span class="n">build_agent_graph</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_deps_type</span><span class="p">,</span> <span class="n">result_type</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">result_type</span><span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">_prepare_result_schema</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">result_type</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n">RunResultDataT</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">_result</span><span class="o">.</span><span class="n">ResultSchema</span><span class="p">[</span><span class="n">RunResultDataT</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">result_type</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_result_validators</span><span class="p">:</span>
                <span class="k">raise</span> <span class="n">exceptions</span><span class="o">.</span><span class="n">UserError</span><span class="p">(</span><span class="s1">'Cannot set a custom run `result_type` when the agent has result validators'</span><span class="p">)</span>
            <span class="k">return</span> <span class="n">_result</span><span class="o">.</span><span class="n">ResultSchema</span><span class="p">[</span><span class="n">result_type</span><span class="p">]</span><span class="o">.</span><span class="n">build</span><span class="p">(</span>
                <span class="n">result_type</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_result_tool_name</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_result_tool_description</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_result_schema</span>  <span class="c1"># pyright: ignore[reportReturnType]</span>

    <span class="nd">@staticmethod</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">is_model_request_node</span><span class="p">(</span>
        <span class="n">node</span><span class="p">:</span> <span class="n">_agent_graph</span><span class="o">.</span><span class="n">AgentNode</span><span class="p">[</span><span class="n">T</span><span class="p">,</span> <span class="n">S</span><span class="p">]</span> <span class="o">|</span> <span class="n">End</span><span class="p">[</span><span class="n">result</span><span class="o">.</span><span class="n">FinalResult</span><span class="p">[</span><span class="n">S</span><span class="p">]],</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TypeGuard</span><span class="p">[</span><span class="n">_agent_graph</span><span class="o">.</span><span class="n">ModelRequestNode</span><span class="p">[</span><span class="n">T</span><span class="p">,</span> <span class="n">S</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""Check if the node is a `ModelRequestNode`, narrowing the type if it is.</span>

<span class="sd">        This method preserves the generic parameters while narrowing the type, unlike a direct call to `isinstance`.</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">node</span><span class="p">,</span> <span class="n">_agent_graph</span><span class="o">.</span><span class="n">ModelRequestNode</span><span class="p">)</span>

    <span class="nd">@staticmethod</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">is_call_tools_node</span><span class="p">(</span>
        <span class="n">node</span><span class="p">:</span> <span class="n">_agent_graph</span><span class="o">.</span><span class="n">AgentNode</span><span class="p">[</span><span class="n">T</span><span class="p">,</span> <span class="n">S</span><span class="p">]</span> <span class="o">|</span> <span class="n">End</span><span class="p">[</span><span class="n">result</span><span class="o">.</span><span class="n">FinalResult</span><span class="p">[</span><span class="n">S</span><span class="p">]],</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TypeGuard</span><span class="p">[</span><span class="n">_agent_graph</span><span class="o">.</span><span class="n">CallToolsNode</span><span class="p">[</span><span class="n">T</span><span class="p">,</span> <span class="n">S</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""Check if the node is a `CallToolsNode`, narrowing the type if it is.</span>

<span class="sd">        This method preserves the generic parameters while narrowing the type, unlike a direct call to `isinstance`.</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">node</span><span class="p">,</span> <span class="n">_agent_graph</span><span class="o">.</span><span class="n">CallToolsNode</span><span class="p">)</span>

    <span class="nd">@staticmethod</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">is_user_prompt_node</span><span class="p">(</span>
        <span class="n">node</span><span class="p">:</span> <span class="n">_agent_graph</span><span class="o">.</span><span class="n">AgentNode</span><span class="p">[</span><span class="n">T</span><span class="p">,</span> <span class="n">S</span><span class="p">]</span> <span class="o">|</span> <span class="n">End</span><span class="p">[</span><span class="n">result</span><span class="o">.</span><span class="n">FinalResult</span><span class="p">[</span><span class="n">S</span><span class="p">]],</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TypeGuard</span><span class="p">[</span><span class="n">_agent_graph</span><span class="o">.</span><span class="n">UserPromptNode</span><span class="p">[</span><span class="n">T</span><span class="p">,</span> <span class="n">S</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""Check if the node is a `UserPromptNode`, narrowing the type if it is.</span>

<span class="sd">        This method preserves the generic parameters while narrowing the type, unlike a direct call to `isinstance`.</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">node</span><span class="p">,</span> <span class="n">_agent_graph</span><span class="o">.</span><span class="n">UserPromptNode</span><span class="p">)</span>

    <span class="nd">@staticmethod</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">is_end_node</span><span class="p">(</span>
        <span class="n">node</span><span class="p">:</span> <span class="n">_agent_graph</span><span class="o">.</span><span class="n">AgentNode</span><span class="p">[</span><span class="n">T</span><span class="p">,</span> <span class="n">S</span><span class="p">]</span> <span class="o">|</span> <span class="n">End</span><span class="p">[</span><span class="n">result</span><span class="o">.</span><span class="n">FinalResult</span><span class="p">[</span><span class="n">S</span><span class="p">]],</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TypeGuard</span><span class="p">[</span><span class="n">End</span><span class="p">[</span><span class="n">result</span><span class="o">.</span><span class="n">FinalResult</span><span class="p">[</span><span class="n">S</span><span class="p">]]]:</span>
<span class="w">        </span><span class="sd">"""Check if the node is a `End`, narrowing the type if it is.</span>

<span class="sd">        This method preserves the generic parameters while narrowing the type, unlike a direct call to `isinstance`.</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">node</span><span class="p">,</span> <span class="n">End</span><span class="p">)</span>

    <span class="nd">@asynccontextmanager</span>
    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">run_mcp_servers</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AsyncIterator</span><span class="p">[</span><span class="kc">None</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Run [`MCPServerStdio`s][pydantic_ai.mcp.MCPServerStdio] so they can be used by the agent.</span>

<span class="sd">        Returns: a context manager to start and shutdown the servers.</span>
<span class="sd">        """</span>
        <span class="n">exit_stack</span> <span class="o">=</span> <span class="n">AsyncExitStack</span><span class="p">()</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">mcp_server</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_mcp_servers</span><span class="p">:</span>
                <span class="k">await</span> <span class="n">exit_stack</span><span class="o">.</span><span class="n">enter_async_context</span><span class="p">(</span><span class="n">mcp_server</span><span class="p">)</span>
            <span class="k">yield</span>
        <span class="k">finally</span><span class="p">:</span>
            <span class="k">await</span> <span class="n">exit_stack</span><span class="o">.</span><span class="n">aclose</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.agent.Agent.model" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">model</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_2"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_2 > code"></button><code><span class="n">model</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.Model" href="../models/base/#pydantic_ai.models.Model">Model</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.KnownModelName" href="../models/base/#pydantic_ai.models.KnownModelName">KnownModelName</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The default model configured for this agent.</p>
<p>We allow str here since the actual list of allowed models changes frequently.</p>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.agent.Agent.__init__" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">__init__</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_3"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_3 > code"></button><code><span class="fm">__init__</span><span class="p">(</span>
    <span class="nf">model</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.Model" href="../models/base/#pydantic_ai.models.Model">Model</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.KnownModelName" href="../models/base/#pydantic_ai.models.KnownModelName">KnownModelName</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">result_type</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type">type</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.result.ResultDataT" href="../result/#pydantic_ai.result.ResultDataT">ResultDataT</a></span><span class="p">]</span> <span class="o">=</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span><span class="p">,</span>
    <span class="n">system_prompt</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="collections.abc.Sequence" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence">Sequence</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">(),</span>
    <span class="n">deps_type</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type">type</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span><span class="p">]</span> <span class="o">=</span> <span class="n"><span title="pydantic_ai.agent.NoneType">NoneType</span></span><span class="p">,</span>
    <span class="n">name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">model_settings</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.settings.ModelSettings" href="../settings/#pydantic_ai.settings.ModelSettings">ModelSettings</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">retries</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#int">int</a></span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span>
    <span class="n">result_tool_name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">=</span> <span class="s2">"final_result"</span><span class="p">,</span>
    <span class="n">result_tool_description</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">result_retries</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#int">int</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">tools</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="collections.abc.Sequence" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence">Sequence</a></span><span class="p">[</span>
        <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.Tool" href="../tools/#pydantic_ai.tools.Tool">Tool</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span><span class="p">]</span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.ToolFuncEither" href="../tools/#pydantic_ai.tools.ToolFuncEither">ToolFuncEither</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span><span class="p">,</span> <span class="o">...</span><span class="p">]</span>
    <span class="p">]</span> <span class="o">=</span> <span class="p">(),</span>
    <span class="n">mcp_servers</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="collections.abc.Sequence" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence">Sequence</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.mcp.MCPServer" href="../mcp/#pydantic_ai.mcp.MCPServer">MCPServer</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">(),</span>
    <span class="n">defer_model_check</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">end_strategy</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.agent.EndStrategy" href="#pydantic_ai.agent.EndStrategy">EndStrategy</a></span> <span class="o">=</span> <span class="s2">"early"</span><span class="p">,</span>
    <span class="n">instrument</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.instrumented.InstrumentationSettings" href="../models/instrumented/#pydantic_ai.models.instrumented.InstrumentationSettings">InstrumentationSettings</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Create an agent.</p>


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
                <code>model</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_ai.models.Model" href="../models/base/#pydantic_ai.models.Model">Model</a> | <a class="autorefs autorefs-internal" title="pydantic_ai.models.KnownModelName" href="../models/base/#pydantic_ai.models.KnownModelName">KnownModelName</a> | <a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The default model to use for this agent, if not provide,
you must provide the model when calling it. We allow str here since the actual list of allowed models changes frequently.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>result_type</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type">type</a>[<a class="autorefs autorefs-internal" title="pydantic_ai.result.ResultDataT" href="../result/#pydantic_ai.result.ResultDataT">ResultDataT</a>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The type of the result data, used to validate the result data, defaults to <code>str</code>.</p>
              </div>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>system_prompt</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a> | <a class="autorefs autorefs-external" title="collections.abc.Sequence" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence">Sequence</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Static system prompts to use for this agent, you can also register system
prompts via a function with <a class="autorefs autorefs-internal" href="#pydantic_ai.agent.Agent.system_prompt"><code>system_prompt</code></a>.</p>
              </div>
            </td>
            <td>
                  <code>()</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>deps_type</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type">type</a>[<a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The type used for dependency injection, this parameter exists solely to allow you to fully
parameterize the agent, and therefore get the best out of static type checking.
If you're not using deps, but want type checking to pass, you can set <code>deps=None</code> to satisfy Pyright
or add a type hint <code>: Agent[None, &lt;return type&gt;]</code>.</p>
              </div>
            </td>
            <td>
                  <code><span title="pydantic_ai.agent.NoneType">NoneType</span></code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>name</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The name of the agent, used for logging. If <code>None</code>, we try to infer the agent name from the call frame
when the agent is first run.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>model_settings</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_ai.settings.ModelSettings" href="../settings/#pydantic_ai.settings.ModelSettings">ModelSettings</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Optional model request settings to use for this agent's runs, by default.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>retries</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#int">int</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The default number of retries to allow before raising an error.</p>
              </div>
            </td>
            <td>
                  <code>1</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>result_tool_name</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The name of the tool to use for the final result.</p>
              </div>
            </td>
            <td>
                  <code>'final_result'</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>result_tool_description</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The description of the final result tool.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>result_retries</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#int">int</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The maximum number of retries to allow for result validation, defaults to <code>retries</code>.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>tools</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" title="collections.abc.Sequence" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence">Sequence</a>[<a class="autorefs autorefs-internal" title="pydantic_ai.tools.Tool" href="../tools/#pydantic_ai.tools.Tool">Tool</a>[<a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a>] | <a class="autorefs autorefs-internal" title="pydantic_ai.tools.ToolFuncEither" href="../tools/#pydantic_ai.tools.ToolFuncEither">ToolFuncEither</a>[<a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a>, ...]]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Tools to register with the agent, you can also register tools via the decorators
<a class="autorefs autorefs-internal" href="#pydantic_ai.agent.Agent.tool"><code>@agent.tool</code></a> and <a class="autorefs autorefs-internal" href="#pydantic_ai.agent.Agent.tool_plain"><code>@agent.tool_plain</code></a>.</p>
              </div>
            </td>
            <td>
                  <code>()</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>mcp_servers</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" title="collections.abc.Sequence" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence">Sequence</a>[<a class="autorefs autorefs-internal" title="pydantic_ai.mcp.MCPServer" href="../mcp/#pydantic_ai.mcp.MCPServer">MCPServer</a>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>MCP servers to register with the agent. You should register a <a class="autorefs autorefs-internal" href="../mcp/#pydantic_ai.mcp.MCPServer"><code>MCPServer</code></a>
for each server you want the agent to connect to.</p>
              </div>
            </td>
            <td>
                  <code>()</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>defer_model_check</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>by default, if you provide a <a class="autorefs autorefs-internal" href="../models/base/#pydantic_ai.models.KnownModelName">named</a> model,
it's evaluated to create a <a class="autorefs autorefs-internal" href="../models/base/#pydantic_ai.models.Model"><code>Model</code></a> instance immediately,
which checks for the necessary environment variables. Set this to <code>false</code>
to defer the evaluation until the first run. Useful if you want to
<a class="autorefs autorefs-internal" href="#pydantic_ai.agent.Agent.override">override the model</a> for testing.</p>
              </div>
            </td>
            <td>
                  <code>False</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>end_strategy</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_ai.agent.EndStrategy" href="#pydantic_ai.agent.EndStrategy">EndStrategy</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Strategy for handling tool calls that are requested alongside a final result.
See <a class="autorefs autorefs-internal" href="#pydantic_ai.agent.EndStrategy"><code>EndStrategy</code></a> for more information.</p>
              </div>
            </td>
            <td>
                  <code>'early'</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>instrument</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_ai.models.instrumented.InstrumentationSettings" href="../models/instrumented/#pydantic_ai.models.instrumented.InstrumentationSettings">InstrumentationSettings</a> | <a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Set to True to automatically instrument with OpenTelemetry,
which will use Logfire if it's configured.
Set to an instance of <a class="autorefs autorefs-internal" href="#pydantic_ai.agent.InstrumentationSettings"><code>InstrumentationSettings</code></a> to customize.
If this isn't set, then the last value set by
<a class="autorefs autorefs-internal" href="#pydantic_ai.agent.Agent.instrument_all"><code>Agent.instrument_all()</code></a>
will be used, which defaults to False.
See the <a href="https://ai.pydantic.dev/logfire/">Debugging and Monitoring guide</a> for more info.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/agent.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">145</span>
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
<span class="normal">225</span>
<span class="normal">226</span>
<span class="normal">227</span>
<span class="normal">228</span>
<span class="normal">229</span>
<span class="normal">230</span>
<span class="normal">231</span>
<span class="normal">232</span>
<span class="normal">233</span>
<span class="normal">234</span>
<span class="normal">235</span></pre></div></td><td class="code"><div><pre id="__code_4"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_4 > code"></button><code tabindex="0"><span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">model</span><span class="p">:</span> <span class="n">models</span><span class="o">.</span><span class="n">Model</span> <span class="o">|</span> <span class="n">models</span><span class="o">.</span><span class="n">KnownModelName</span> <span class="o">|</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">result_type</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n">ResultDataT</span><span class="p">]</span> <span class="o">=</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">system_prompt</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="p">(),</span>
    <span class="n">deps_type</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">]</span> <span class="o">=</span> <span class="n">NoneType</span><span class="p">,</span>
    <span class="n">name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">model_settings</span><span class="p">:</span> <span class="n">ModelSettings</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">retries</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span>
    <span class="n">result_tool_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s1">'final_result'</span><span class="p">,</span>
    <span class="n">result_tool_description</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">result_retries</span><span class="p">:</span> <span class="nb">int</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">tools</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">Tool</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">]</span> <span class="o">|</span> <span class="n">ToolFuncEither</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">,</span> <span class="o">...</span><span class="p">]]</span> <span class="o">=</span> <span class="p">(),</span>
    <span class="n">mcp_servers</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">MCPServer</span><span class="p">]</span> <span class="o">=</span> <span class="p">(),</span>
    <span class="n">defer_model_check</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">end_strategy</span><span class="p">:</span> <span class="n">EndStrategy</span> <span class="o">=</span> <span class="s1">'early'</span><span class="p">,</span>
    <span class="n">instrument</span><span class="p">:</span> <span class="n">InstrumentationSettings</span> <span class="o">|</span> <span class="nb">bool</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">):</span>
<span class="w">    </span><span class="sd">"""Create an agent.</span>

<span class="sd">    Args:</span>
<span class="sd">        model: The default model to use for this agent, if not provide,</span>
<span class="sd">            you must provide the model when calling it. We allow str here since the actual list of allowed models changes frequently.</span>
<span class="sd">        result_type: The type of the result data, used to validate the result data, defaults to `str`.</span>
<span class="sd">        system_prompt: Static system prompts to use for this agent, you can also register system</span>
<span class="sd">            prompts via a function with [`system_prompt`][pydantic_ai.Agent.system_prompt].</span>
<span class="sd">        deps_type: The type used for dependency injection, this parameter exists solely to allow you to fully</span>
<span class="sd">            parameterize the agent, and therefore get the best out of static type checking.</span>
<span class="sd">            If you're not using deps, but want type checking to pass, you can set `deps=None` to satisfy Pyright</span>
<span class="sd">            or add a type hint `: Agent[None, &lt;return type&gt;]`.</span>
<span class="sd">        name: The name of the agent, used for logging. If `None`, we try to infer the agent name from the call frame</span>
<span class="sd">            when the agent is first run.</span>
<span class="sd">        model_settings: Optional model request settings to use for this agent's runs, by default.</span>
<span class="sd">        retries: The default number of retries to allow before raising an error.</span>
<span class="sd">        result_tool_name: The name of the tool to use for the final result.</span>
<span class="sd">        result_tool_description: The description of the final result tool.</span>
<span class="sd">        result_retries: The maximum number of retries to allow for result validation, defaults to `retries`.</span>
<span class="sd">        tools: Tools to register with the agent, you can also register tools via the decorators</span>
<span class="sd">            [`@agent.tool`][pydantic_ai.Agent.tool] and [`@agent.tool_plain`][pydantic_ai.Agent.tool_plain].</span>
<span class="sd">        mcp_servers: MCP servers to register with the agent. You should register a [`MCPServer`][pydantic_ai.mcp.MCPServer]</span>
<span class="sd">            for each server you want the agent to connect to.</span>
<span class="sd">        defer_model_check: by default, if you provide a [named][pydantic_ai.models.KnownModelName] model,</span>
<span class="sd">            it's evaluated to create a [`Model`][pydantic_ai.models.Model] instance immediately,</span>
<span class="sd">            which checks for the necessary environment variables. Set this to `false`</span>
<span class="sd">            to defer the evaluation until the first run. Useful if you want to</span>
<span class="sd">            [override the model][pydantic_ai.Agent.override] for testing.</span>
<span class="sd">        end_strategy: Strategy for handling tool calls that are requested alongside a final result.</span>
<span class="sd">            See [`EndStrategy`][pydantic_ai.agent.EndStrategy] for more information.</span>
<span class="sd">        instrument: Set to True to automatically instrument with OpenTelemetry,</span>
<span class="sd">            which will use Logfire if it's configured.</span>
<span class="sd">            Set to an instance of [`InstrumentationSettings`][pydantic_ai.agent.InstrumentationSettings] to customize.</span>
<span class="sd">            If this isn't set, then the last value set by</span>
<span class="sd">            [`Agent.instrument_all()`][pydantic_ai.Agent.instrument_all]</span>
<span class="sd">            will be used, which defaults to False.</span>
<span class="sd">            See the [Debugging and Monitoring guide](https://ai.pydantic.dev/logfire/) for more info.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="n">model</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">or</span> <span class="n">defer_model_check</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">model</span> <span class="o">=</span> <span class="n">model</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">model</span> <span class="o">=</span> <span class="n">models</span><span class="o">.</span><span class="n">infer_model</span><span class="p">(</span><span class="n">model</span><span class="p">)</span>

    <span class="bp">self</span><span class="o">.</span><span class="n">end_strategy</span> <span class="o">=</span> <span class="n">end_strategy</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="o">=</span> <span class="n">name</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">model_settings</span> <span class="o">=</span> <span class="n">model_settings</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">result_type</span> <span class="o">=</span> <span class="n">result_type</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">instrument</span> <span class="o">=</span> <span class="n">instrument</span>

    <span class="bp">self</span><span class="o">.</span><span class="n">_deps_type</span> <span class="o">=</span> <span class="n">deps_type</span>

    <span class="bp">self</span><span class="o">.</span><span class="n">_result_tool_name</span> <span class="o">=</span> <span class="n">result_tool_name</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_result_tool_description</span> <span class="o">=</span> <span class="n">result_tool_description</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_result_schema</span> <span class="o">=</span> <span class="n">_result</span><span class="o">.</span><span class="n">ResultSchema</span><span class="p">[</span><span class="n">result_type</span><span class="p">]</span><span class="o">.</span><span class="n">build</span><span class="p">(</span>
        <span class="n">result_type</span><span class="p">,</span> <span class="n">result_tool_name</span><span class="p">,</span> <span class="n">result_tool_description</span>
    <span class="p">)</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_result_validators</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="bp">self</span><span class="o">.</span><span class="n">_system_prompts</span> <span class="o">=</span> <span class="p">(</span><span class="n">system_prompt</span><span class="p">,)</span> <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">system_prompt</span><span class="p">,</span> <span class="nb">str</span><span class="p">)</span> <span class="k">else</span> <span class="nb">tuple</span><span class="p">(</span><span class="n">system_prompt</span><span class="p">)</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_system_prompt_functions</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_system_prompt_dynamic_functions</span> <span class="o">=</span> <span class="p">{}</span>

    <span class="bp">self</span><span class="o">.</span><span class="n">_function_tools</span> <span class="o">=</span> <span class="p">{}</span>

    <span class="bp">self</span><span class="o">.</span><span class="n">_default_retries</span> <span class="o">=</span> <span class="n">retries</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_max_result_retries</span> <span class="o">=</span> <span class="n">result_retries</span> <span class="k">if</span> <span class="n">result_retries</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="k">else</span> <span class="n">retries</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_mcp_servers</span> <span class="o">=</span> <span class="n">mcp_servers</span>
    <span class="k">for</span> <span class="n">tool</span> <span class="ow">in</span> <span class="n">tools</span><span class="p">:</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">tool</span><span class="p">,</span> <span class="n">Tool</span><span class="p">):</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_register_tool</span><span class="p">(</span><span class="n">tool</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_register_tool</span><span class="p">(</span><span class="n">Tool</span><span class="p">(</span><span class="n">tool</span><span class="p">))</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.agent.Agent.end_strategy" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">end_strategy</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_5"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_5 > code"></button><code><span class="n">end_strategy</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.agent.EndStrategy" href="#pydantic_ai.agent.EndStrategy">EndStrategy</a></span> <span class="o">=</span> <span class="n"><span title="pydantic_ai.agent.Agent(end_strategy)">end_strategy</span></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Strategy for handling tool calls when a final result is found.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.agent.Agent.name" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">name</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_6"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_6 > code"></button><code><span class="n">name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="n"><span title="pydantic_ai.agent.Agent(name)">name</span></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The name of the agent, used for logging.</p>
<p>If <code>None</code>, we try to infer the agent name from the call frame when the agent is first run.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.agent.Agent.model_settings" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">model_settings</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_7"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_7 > code"></button><code><span class="n">model_settings</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.settings.ModelSettings" href="../settings/#pydantic_ai.settings.ModelSettings">ModelSettings</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="n"><span title="pydantic_ai.agent.Agent(model_settings)">model_settings</span></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Optional model request settings to use for this agents's runs, by default.</p>
<p>Note, if <code>model_settings</code> is provided by <code>run</code>, <code>run_sync</code>, or <code>run_stream</code>, those settings will
be merged with this value, with the runtime argument taking priority.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.agent.Agent.result_type" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">result_type</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_8"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_8 > code"></button><code><span class="n">result_type</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type">type</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.result.ResultDataT" href="../result/#pydantic_ai.result.ResultDataT">ResultDataT</a></span><span class="p">]</span> <span class="o">=</span> <span class="n"><span title="pydantic_ai.agent.Agent(result_type)">result_type</span></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The type of the result data, used to validate the result data, defaults to <code>str</code>.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.agent.Agent.instrument" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">instrument</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_9"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_9 > code"></button><code><span class="n">instrument</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.instrumented.InstrumentationSettings" href="../models/instrumented/#pydantic_ai.models.instrumented.InstrumentationSettings">InstrumentationSettings</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="p">(</span>
    <span class="n"><span title="pydantic_ai.agent.Agent(instrument)">instrument</span></span>
<span class="p">)</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Options to automatically instrument with OpenTelemetry.</p>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.agent.Agent.instrument_all" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">instrument_all</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-staticmethod"><code>staticmethod</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_10"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_10 > code"></button><code><span class="nf">instrument_all</span><span class="p">(</span>
    <span class="n">instrument</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.instrumented.InstrumentationSettings" href="../models/instrumented/#pydantic_ai.models.instrumented.InstrumentationSettings">InstrumentationSettings</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Set the instrumentation options for all agents where <code>instrument</code> is not set.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/agent.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">237</span>
<span class="normal">238</span>
<span class="normal">239</span>
<span class="normal">240</span></pre></div></td><td class="code"><div><pre id="__code_11"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_11 > code"></button><code><span class="nd">@staticmethod</span>
<span class="k">def</span><span class="w"> </span><span class="nf">instrument_all</span><span class="p">(</span><span class="n">instrument</span><span class="p">:</span> <span class="n">InstrumentationSettings</span> <span class="o">|</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Set the instrumentation options for all agents where `instrument` is not set."""</span>
    <span class="n">Agent</span><span class="o">.</span><span class="n">_instrument_default</span> <span class="o">=</span> <span class="n">instrument</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.agent.Agent.run" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">run</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-async"><code>async</code></small>
  </span>

</h4>
          <div class="doc-overloads">
<div class="language-python doc-signature highlight"><pre id="__code_12"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_12 > code"></button><code><span class="nf">run</span><span class="p">(</span>
    <span class="n">user_prompt</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="collections.abc.Sequence" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence">Sequence</a></span><span class="p">[</span><span class="n"><span title="pydantic_ai.messages.UserContent">UserContent</span></span><span class="p">],</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">result_type</span><span class="p">:</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">message_history</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list">list</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ModelMessage" href="../messages/#pydantic_ai.messages.ModelMessage">ModelMessage</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">model</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.Model" href="../models/base/#pydantic_ai.models.Model">Model</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.KnownModelName" href="../models/base/#pydantic_ai.models.KnownModelName">KnownModelName</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">deps</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">model_settings</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.settings.ModelSettings" href="../settings/#pydantic_ai.settings.ModelSettings">ModelSettings</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">usage_limits</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.usage.UsageLimits" href="../usage/#pydantic_ai.usage.UsageLimits">UsageLimits</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">usage</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.usage.Usage" href="../usage/#pydantic_ai.usage.Usage">Usage</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">infer_name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">True</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.agent.AgentRunResult" href="#pydantic_ai.agent.AgentRunResult">AgentRunResult</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.result.ResultDataT" href="../result/#pydantic_ai.result.ResultDataT">ResultDataT</a></span><span class="p">]</span>
</code></pre></div><div class="language-python doc-signature highlight"><pre id="__code_13"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_13 > code"></button><code><span class="nf">run</span><span class="p">(</span>
    <span class="n">user_prompt</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="collections.abc.Sequence" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence">Sequence</a></span><span class="p">[</span><span class="n"><span title="pydantic_ai.messages.UserContent">UserContent</span></span><span class="p">],</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">result_type</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type">type</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.agent.RunResultDataT" href="#pydantic_ai.agent.RunResultDataT">RunResultDataT</a></span><span class="p">],</span>
    <span class="n">message_history</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list">list</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ModelMessage" href="../messages/#pydantic_ai.messages.ModelMessage">ModelMessage</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">model</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.Model" href="../models/base/#pydantic_ai.models.Model">Model</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.KnownModelName" href="../models/base/#pydantic_ai.models.KnownModelName">KnownModelName</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">deps</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">model_settings</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.settings.ModelSettings" href="../settings/#pydantic_ai.settings.ModelSettings">ModelSettings</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">usage_limits</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.usage.UsageLimits" href="../usage/#pydantic_ai.usage.UsageLimits">UsageLimits</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">usage</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.usage.Usage" href="../usage/#pydantic_ai.usage.Usage">Usage</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">infer_name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">True</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.agent.AgentRunResult" href="#pydantic_ai.agent.AgentRunResult">AgentRunResult</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.agent.RunResultDataT" href="#pydantic_ai.agent.RunResultDataT">RunResultDataT</a></span><span class="p">]</span>
</code></pre></div>          </div>
<div class="language-python doc-signature highlight"><pre id="__code_14"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_14 > code"></button><code><span class="nf">run</span><span class="p">(</span>
    <span class="n">user_prompt</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="collections.abc.Sequence" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence">Sequence</a></span><span class="p">[</span><span class="n"><span title="pydantic_ai.messages.UserContent">UserContent</span></span><span class="p">],</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">result_type</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type">type</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.agent.RunResultDataT" href="#pydantic_ai.agent.RunResultDataT">RunResultDataT</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">message_history</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list">list</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ModelMessage" href="../messages/#pydantic_ai.messages.ModelMessage">ModelMessage</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">model</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.Model" href="../models/base/#pydantic_ai.models.Model">Model</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.KnownModelName" href="../models/base/#pydantic_ai.models.KnownModelName">KnownModelName</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">deps</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">model_settings</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.settings.ModelSettings" href="../settings/#pydantic_ai.settings.ModelSettings">ModelSettings</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">usage_limits</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.usage.UsageLimits" href="../usage/#pydantic_ai.usage.UsageLimits">UsageLimits</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">usage</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.usage.Usage" href="../usage/#pydantic_ai.usage.Usage">Usage</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">infer_name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">True</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.agent.AgentRunResult" href="#pydantic_ai.agent.AgentRunResult">AgentRunResult</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a></span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Run the agent with a user prompt in async mode.</p>
<p>This method builds an internal agent graph (using system prompts, tools and result schemas) and then
runs the graph to completion. The result of the run is returned.</p>
<p>Example:
</p><div class="language-python highlight"><pre id="__code_15"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_15 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>

<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="s1">'openai:gpt-4o'</span><span class="p">)</span>

<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">main</span><span class="p">():</span>
    <span class="n">agent_run</span> <span class="o">=</span> <span class="k">await</span> <span class="n">agent</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="s1">'What is the capital of France?'</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">agent_run</span><span class="o">.</span><span class="n">data</span><span class="p">)</span>
    <span class="c1">#&gt; Paris</span>
</code></pre></div><p></p>


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
                <code>user_prompt</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a> | <a class="autorefs autorefs-external" title="collections.abc.Sequence" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence">Sequence</a>[<span title="pydantic_ai.messages.UserContent">UserContent</span>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>User input to start/continue the conversation.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>result_type</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type">type</a>[<a class="autorefs autorefs-internal" title="pydantic_ai.agent.RunResultDataT" href="#pydantic_ai.agent.RunResultDataT">RunResultDataT</a>] | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Custom result type to use for this run, <code>result_type</code> may only be used if the agent has no
result validators since result validators would expect an argument that matches the agent's result type.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>message_history</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list">list</a>[<a class="autorefs autorefs-internal" title="pydantic_ai.messages.ModelMessage" href="../messages/#pydantic_ai.messages.ModelMessage">ModelMessage</a>] | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>History of the conversation so far.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>model</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_ai.models.Model" href="../models/base/#pydantic_ai.models.Model">Model</a> | <a class="autorefs autorefs-internal" title="pydantic_ai.models.KnownModelName" href="../models/base/#pydantic_ai.models.KnownModelName">KnownModelName</a> | <a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Optional model to use for this run, required if <code>model</code> was not set when creating the agent.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>deps</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Optional dependencies to use for this run.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>model_settings</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_ai.settings.ModelSettings" href="../settings/#pydantic_ai.settings.ModelSettings">ModelSettings</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Optional settings to use for this model's request.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>usage_limits</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_ai.usage.UsageLimits" href="../usage/#pydantic_ai.usage.UsageLimits">UsageLimits</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Optional limits on model request count or token usage.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>usage</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_ai.usage.Usage" href="../usage/#pydantic_ai.usage.Usage">Usage</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Optional usage to start with, useful for resuming a conversation or agents used in tools.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>infer_name</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Whether to try to infer the agent name from the call frame if it's not set.</p>
              </div>
            </td>
            <td>
                  <code>True</code>
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
                  <code><a class="autorefs autorefs-internal" title="pydantic_ai.agent.AgentRunResult" href="#pydantic_ai.agent.AgentRunResult">AgentRunResult</a>[<a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The result of the run.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/agent.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">272</span>
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
<span class="normal">299</span>
<span class="normal">300</span>
<span class="normal">301</span>
<span class="normal">302</span>
<span class="normal">303</span>
<span class="normal">304</span>
<span class="normal">305</span>
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
<span class="normal">333</span></pre></div></td><td class="code"><div><pre id="__code_16"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_16 > code"></button><code tabindex="0"><span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">run</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">user_prompt</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">_messages</span><span class="o">.</span><span class="n">UserContent</span><span class="p">],</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">result_type</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n">RunResultDataT</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">message_history</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">_messages</span><span class="o">.</span><span class="n">ModelMessage</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">model</span><span class="p">:</span> <span class="n">models</span><span class="o">.</span><span class="n">Model</span> <span class="o">|</span> <span class="n">models</span><span class="o">.</span><span class="n">KnownModelName</span> <span class="o">|</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">deps</span><span class="p">:</span> <span class="n">AgentDepsT</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">model_settings</span><span class="p">:</span> <span class="n">ModelSettings</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">usage_limits</span><span class="p">:</span> <span class="n">_usage</span><span class="o">.</span><span class="n">UsageLimits</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">usage</span><span class="p">:</span> <span class="n">_usage</span><span class="o">.</span><span class="n">Usage</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">infer_name</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AgentRunResult</span><span class="p">[</span><span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Run the agent with a user prompt in async mode.</span>

<span class="sd">    This method builds an internal agent graph (using system prompts, tools and result schemas) and then</span>
<span class="sd">    runs the graph to completion. The result of the run is returned.</span>

<span class="sd">    Example:</span>
<span class="sd">    ```python</span>
<span class="sd">    from pydantic_ai import Agent</span>

<span class="sd">    agent = Agent('openai:gpt-4o')</span>

<span class="sd">    async def main():</span>
<span class="sd">        agent_run = await agent.run('What is the capital of France?')</span>
<span class="sd">        print(agent_run.data)</span>
<span class="sd">        #&gt; Paris</span>
<span class="sd">    ```</span>

<span class="sd">    Args:</span>
<span class="sd">        user_prompt: User input to start/continue the conversation.</span>
<span class="sd">        result_type: Custom result type to use for this run, `result_type` may only be used if the agent has no</span>
<span class="sd">            result validators since result validators would expect an argument that matches the agent's result type.</span>
<span class="sd">        message_history: History of the conversation so far.</span>
<span class="sd">        model: Optional model to use for this run, required if `model` was not set when creating the agent.</span>
<span class="sd">        deps: Optional dependencies to use for this run.</span>
<span class="sd">        model_settings: Optional settings to use for this model's request.</span>
<span class="sd">        usage_limits: Optional limits on model request count or token usage.</span>
<span class="sd">        usage: Optional usage to start with, useful for resuming a conversation or agents used in tools.</span>
<span class="sd">        infer_name: Whether to try to infer the agent name from the call frame if it's not set.</span>

<span class="sd">    Returns:</span>
<span class="sd">        The result of the run.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="n">infer_name</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_infer_name</span><span class="p">(</span><span class="n">inspect</span><span class="o">.</span><span class="n">currentframe</span><span class="p">())</span>
    <span class="k">async</span> <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">iter</span><span class="p">(</span>
        <span class="n">user_prompt</span><span class="o">=</span><span class="n">user_prompt</span><span class="p">,</span>
        <span class="n">result_type</span><span class="o">=</span><span class="n">result_type</span><span class="p">,</span>
        <span class="n">message_history</span><span class="o">=</span><span class="n">message_history</span><span class="p">,</span>
        <span class="n">model</span><span class="o">=</span><span class="n">model</span><span class="p">,</span>
        <span class="n">deps</span><span class="o">=</span><span class="n">deps</span><span class="p">,</span>
        <span class="n">model_settings</span><span class="o">=</span><span class="n">model_settings</span><span class="p">,</span>
        <span class="n">usage_limits</span><span class="o">=</span><span class="n">usage_limits</span><span class="p">,</span>
        <span class="n">usage</span><span class="o">=</span><span class="n">usage</span><span class="p">,</span>
    <span class="p">)</span> <span class="k">as</span> <span class="n">agent_run</span><span class="p">:</span>
        <span class="k">async</span> <span class="k">for</span> <span class="n">_</span> <span class="ow">in</span> <span class="n">agent_run</span><span class="p">:</span>
            <span class="k">pass</span>

    <span class="k">assert</span> <span class="n">agent_run</span><span class="o">.</span><span class="n">result</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">,</span> <span class="s1">'The graph run did not finish properly'</span>
    <span class="k">return</span> <span class="n">agent_run</span><span class="o">.</span><span class="n">result</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.agent.Agent.iter" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">iter</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-async"><code>async</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_17"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_17 > code"></button><code><span class="nb">iter</span><span class="p">(</span>
    <span class="nf">user_prompt</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="collections.abc.Sequence" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence">Sequence</a></span><span class="p">[</span><span class="n"><span title="pydantic_ai.messages.UserContent">UserContent</span></span><span class="p">],</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">result_type</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type">type</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.agent.RunResultDataT" href="#pydantic_ai.agent.RunResultDataT">RunResultDataT</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">message_history</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list">list</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ModelMessage" href="../messages/#pydantic_ai.messages.ModelMessage">ModelMessage</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">model</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.Model" href="../models/base/#pydantic_ai.models.Model">Model</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.KnownModelName" href="../models/base/#pydantic_ai.models.KnownModelName">KnownModelName</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">deps</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">model_settings</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.settings.ModelSettings" href="../settings/#pydantic_ai.settings.ModelSettings">ModelSettings</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">usage_limits</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.usage.UsageLimits" href="../usage/#pydantic_ai.usage.UsageLimits">UsageLimits</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">usage</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.usage.Usage" href="../usage/#pydantic_ai.usage.Usage">Usage</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">infer_name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">True</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" title="collections.abc.AsyncIterator" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator">AsyncIterator</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.agent.AgentRun" href="#pydantic_ai.agent.AgentRun">AgentRun</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a></span><span class="p">]]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>A contextmanager which can be used to iterate over the agent graph's nodes as they are executed.</p>
<p>This method builds an internal agent graph (using system prompts, tools and result schemas) and then returns an
<code>AgentRun</code> object. The <code>AgentRun</code> can be used to async-iterate over the nodes of the graph as they are
executed. This is the API to use if you want to consume the outputs coming from each LLM model response, or the
stream of events coming from the execution of tools.</p>
<p>The <code>AgentRun</code> also provides methods to access the full message history, new messages, and usage statistics,
and the final result of the run once it has completed.</p>
<p>For more details, see the documentation of <code>AgentRun</code>.</p>
<p>Example:
</p><div class="language-python highlight"><pre id="__code_18"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_18 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>

<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="s1">'openai:gpt-4o'</span><span class="p">)</span>

<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">main</span><span class="p">():</span>
    <span class="n">nodes</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">async</span> <span class="k">with</span> <span class="n">agent</span><span class="o">.</span><span class="n">iter</span><span class="p">(</span><span class="s1">'What is the capital of France?'</span><span class="p">)</span> <span class="k">as</span> <span class="n">agent_run</span><span class="p">:</span>
        <span class="k">async</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">agent_run</span><span class="p">:</span>
            <span class="n">nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span>
<span class="w">    </span><span class="sd">'''</span>
<span class="sd">    [</span>
<span class="sd">        ModelRequestNode(</span>
<span class="sd">            request=ModelRequest(</span>
<span class="sd">                parts=[</span>
<span class="sd">                    UserPromptPart(</span>
<span class="sd">                        content='What is the capital of France?',</span>
<span class="sd">                        timestamp=datetime.datetime(...),</span>
<span class="sd">                        part_kind='user-prompt',</span>
<span class="sd">                    )</span>
<span class="sd">                ],</span>
<span class="sd">                kind='request',</span>
<span class="sd">            )</span>
<span class="sd">        ),</span>
<span class="sd">        CallToolsNode(</span>
<span class="sd">            model_response=ModelResponse(</span>
<span class="sd">                parts=[TextPart(content='Paris', part_kind='text')],</span>
<span class="sd">                model_name='gpt-4o',</span>
<span class="sd">                timestamp=datetime.datetime(...),</span>
<span class="sd">                kind='response',</span>
<span class="sd">            )</span>
<span class="sd">        ),</span>
<span class="sd">        End(data=FinalResult(data='Paris', tool_name=None, tool_call_id=None)),</span>
<span class="sd">    ]</span>
<span class="sd">    '''</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">agent_run</span><span class="o">.</span><span class="n">result</span><span class="o">.</span><span class="n">data</span><span class="p">)</span>
    <span class="c1">#&gt; Paris</span>
</code></pre></div><p></p>


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
                <code>user_prompt</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a> | <a class="autorefs autorefs-external" title="collections.abc.Sequence" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence">Sequence</a>[<span title="pydantic_ai.messages.UserContent">UserContent</span>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>User input to start/continue the conversation.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>result_type</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type">type</a>[<a class="autorefs autorefs-internal" title="pydantic_ai.agent.RunResultDataT" href="#pydantic_ai.agent.RunResultDataT">RunResultDataT</a>] | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Custom result type to use for this run, <code>result_type</code> may only be used if the agent has no
result validators since result validators would expect an argument that matches the agent's result type.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>message_history</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list">list</a>[<a class="autorefs autorefs-internal" title="pydantic_ai.messages.ModelMessage" href="../messages/#pydantic_ai.messages.ModelMessage">ModelMessage</a>] | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>History of the conversation so far.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>model</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_ai.models.Model" href="../models/base/#pydantic_ai.models.Model">Model</a> | <a class="autorefs autorefs-internal" title="pydantic_ai.models.KnownModelName" href="../models/base/#pydantic_ai.models.KnownModelName">KnownModelName</a> | <a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Optional model to use for this run, required if <code>model</code> was not set when creating the agent.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>deps</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Optional dependencies to use for this run.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>model_settings</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_ai.settings.ModelSettings" href="../settings/#pydantic_ai.settings.ModelSettings">ModelSettings</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Optional settings to use for this model's request.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>usage_limits</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_ai.usage.UsageLimits" href="../usage/#pydantic_ai.usage.UsageLimits">UsageLimits</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Optional limits on model request count or token usage.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>usage</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_ai.usage.Usage" href="../usage/#pydantic_ai.usage.Usage">Usage</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Optional usage to start with, useful for resuming a conversation or agents used in tools.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>infer_name</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Whether to try to infer the agent name from the call frame if it's not set.</p>
              </div>
            </td>
            <td>
                  <code>True</code>
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
                  <code><a class="autorefs autorefs-external" title="collections.abc.AsyncIterator" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator">AsyncIterator</a>[<a class="autorefs autorefs-internal" title="pydantic_ai.agent.AgentRun" href="#pydantic_ai.agent.AgentRun">AgentRun</a>[<a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a>, <a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a>]]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The result of the run.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/agent.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">335</span>
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
<span class="normal">364</span>
<span class="normal">365</span>
<span class="normal">366</span>
<span class="normal">367</span>
<span class="normal">368</span>
<span class="normal">369</span>
<span class="normal">370</span>
<span class="normal">371</span>
<span class="normal">372</span>
<span class="normal">373</span>
<span class="normal">374</span>
<span class="normal">375</span>
<span class="normal">376</span>
<span class="normal">377</span>
<span class="normal">378</span>
<span class="normal">379</span>
<span class="normal">380</span>
<span class="normal">381</span>
<span class="normal">382</span>
<span class="normal">383</span>
<span class="normal">384</span>
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
<span class="normal">396</span>
<span class="normal">397</span>
<span class="normal">398</span>
<span class="normal">399</span>
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
<span class="normal">448</span>
<span class="normal">449</span>
<span class="normal">450</span>
<span class="normal">451</span>
<span class="normal">452</span>
<span class="normal">453</span>
<span class="normal">454</span>
<span class="normal">455</span>
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
<span class="normal">495</span></pre></div></td><td class="code"><div><pre id="__code_19"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_19 > code"></button><code tabindex="0"><span class="nd">@asynccontextmanager</span>
<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">iter</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">user_prompt</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">_messages</span><span class="o">.</span><span class="n">UserContent</span><span class="p">],</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">result_type</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n">RunResultDataT</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">message_history</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">_messages</span><span class="o">.</span><span class="n">ModelMessage</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">model</span><span class="p">:</span> <span class="n">models</span><span class="o">.</span><span class="n">Model</span> <span class="o">|</span> <span class="n">models</span><span class="o">.</span><span class="n">KnownModelName</span> <span class="o">|</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">deps</span><span class="p">:</span> <span class="n">AgentDepsT</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">model_settings</span><span class="p">:</span> <span class="n">ModelSettings</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">usage_limits</span><span class="p">:</span> <span class="n">_usage</span><span class="o">.</span><span class="n">UsageLimits</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">usage</span><span class="p">:</span> <span class="n">_usage</span><span class="o">.</span><span class="n">Usage</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">infer_name</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AsyncIterator</span><span class="p">[</span><span class="n">AgentRun</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]:</span>
<span class="w">    </span><span class="sd">"""A contextmanager which can be used to iterate over the agent graph's nodes as they are executed.</span>

<span class="sd">    This method builds an internal agent graph (using system prompts, tools and result schemas) and then returns an</span>
<span class="sd">    `AgentRun` object. The `AgentRun` can be used to async-iterate over the nodes of the graph as they are</span>
<span class="sd">    executed. This is the API to use if you want to consume the outputs coming from each LLM model response, or the</span>
<span class="sd">    stream of events coming from the execution of tools.</span>

<span class="sd">    The `AgentRun` also provides methods to access the full message history, new messages, and usage statistics,</span>
<span class="sd">    and the final result of the run once it has completed.</span>

<span class="sd">    For more details, see the documentation of `AgentRun`.</span>

<span class="sd">    Example:</span>
<span class="sd">    ```python</span>
<span class="sd">    from pydantic_ai import Agent</span>

<span class="sd">    agent = Agent('openai:gpt-4o')</span>

<span class="sd">    async def main():</span>
<span class="sd">        nodes = []</span>
<span class="sd">        async with agent.iter('What is the capital of France?') as agent_run:</span>
<span class="sd">            async for node in agent_run:</span>
<span class="sd">                nodes.append(node)</span>
<span class="sd">        print(nodes)</span>
<span class="sd">        '''</span>
<span class="sd">        [</span>
<span class="sd">            ModelRequestNode(</span>
<span class="sd">                request=ModelRequest(</span>
<span class="sd">                    parts=[</span>
<span class="sd">                        UserPromptPart(</span>
<span class="sd">                            content='What is the capital of France?',</span>
<span class="sd">                            timestamp=datetime.datetime(...),</span>
<span class="sd">                            part_kind='user-prompt',</span>
<span class="sd">                        )</span>
<span class="sd">                    ],</span>
<span class="sd">                    kind='request',</span>
<span class="sd">                )</span>
<span class="sd">            ),</span>
<span class="sd">            CallToolsNode(</span>
<span class="sd">                model_response=ModelResponse(</span>
<span class="sd">                    parts=[TextPart(content='Paris', part_kind='text')],</span>
<span class="sd">                    model_name='gpt-4o',</span>
<span class="sd">                    timestamp=datetime.datetime(...),</span>
<span class="sd">                    kind='response',</span>
<span class="sd">                )</span>
<span class="sd">            ),</span>
<span class="sd">            End(data=FinalResult(data='Paris', tool_name=None, tool_call_id=None)),</span>
<span class="sd">        ]</span>
<span class="sd">        '''</span>
<span class="sd">        print(agent_run.result.data)</span>
<span class="sd">        #&gt; Paris</span>
<span class="sd">    ```</span>

<span class="sd">    Args:</span>
<span class="sd">        user_prompt: User input to start/continue the conversation.</span>
<span class="sd">        result_type: Custom result type to use for this run, `result_type` may only be used if the agent has no</span>
<span class="sd">            result validators since result validators would expect an argument that matches the agent's result type.</span>
<span class="sd">        message_history: History of the conversation so far.</span>
<span class="sd">        model: Optional model to use for this run, required if `model` was not set when creating the agent.</span>
<span class="sd">        deps: Optional dependencies to use for this run.</span>
<span class="sd">        model_settings: Optional settings to use for this model's request.</span>
<span class="sd">        usage_limits: Optional limits on model request count or token usage.</span>
<span class="sd">        usage: Optional usage to start with, useful for resuming a conversation or agents used in tools.</span>
<span class="sd">        infer_name: Whether to try to infer the agent name from the call frame if it's not set.</span>

<span class="sd">    Returns:</span>
<span class="sd">        The result of the run.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="n">infer_name</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_infer_name</span><span class="p">(</span><span class="n">inspect</span><span class="o">.</span><span class="n">currentframe</span><span class="p">())</span>
    <span class="n">model_used</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_model</span><span class="p">(</span><span class="n">model</span><span class="p">)</span>
    <span class="k">del</span> <span class="n">model</span>

    <span class="n">deps</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_deps</span><span class="p">(</span><span class="n">deps</span><span class="p">)</span>
    <span class="n">new_message_index</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">message_history</span><span class="p">)</span> <span class="k">if</span> <span class="n">message_history</span> <span class="k">else</span> <span class="mi">0</span>
    <span class="n">result_schema</span><span class="p">:</span> <span class="n">_result</span><span class="o">.</span><span class="n">ResultSchema</span><span class="p">[</span><span class="n">RunResultDataT</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prepare_result_schema</span><span class="p">(</span><span class="n">result_type</span><span class="p">)</span>

    <span class="c1"># Build the graph</span>
    <span class="n">graph</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_build_graph</span><span class="p">(</span><span class="n">result_type</span><span class="p">)</span>

    <span class="c1"># Build the initial state</span>
    <span class="n">state</span> <span class="o">=</span> <span class="n">_agent_graph</span><span class="o">.</span><span class="n">GraphAgentState</span><span class="p">(</span>
        <span class="n">message_history</span><span class="o">=</span><span class="n">message_history</span><span class="p">[:]</span> <span class="k">if</span> <span class="n">message_history</span> <span class="k">else</span> <span class="p">[],</span>
        <span class="n">usage</span><span class="o">=</span><span class="n">usage</span> <span class="ow">or</span> <span class="n">_usage</span><span class="o">.</span><span class="n">Usage</span><span class="p">(),</span>
        <span class="n">retries</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
        <span class="n">run_step</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="c1"># We consider it a user error if a user tries to restrict the result type while having a result validator that</span>
    <span class="c1"># may change the result type from the restricted type to something else. Therefore, we consider the following</span>
    <span class="c1"># typecast reasonable, even though it is possible to violate it with otherwise-type-checked code.</span>
    <span class="n">result_validators</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="nb">list</span><span class="p">[</span><span class="n">_result</span><span class="o">.</span><span class="n">ResultValidator</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">,</span> <span class="n">RunResultDataT</span><span class="p">]],</span> <span class="bp">self</span><span class="o">.</span><span class="n">_result_validators</span><span class="p">)</span>

    <span class="c1"># TODO: Instead of this, copy the function tools to ensure they don't share current_retry state between agent</span>
    <span class="c1">#  runs. Requires some changes to `Tool` to make them copyable though.</span>
    <span class="k">for</span> <span class="n">v</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_function_tools</span><span class="o">.</span><span class="n">values</span><span class="p">():</span>
        <span class="n">v</span><span class="o">.</span><span class="n">current_retry</span> <span class="o">=</span> <span class="mi">0</span>

    <span class="n">model_settings</span> <span class="o">=</span> <span class="n">merge_model_settings</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">model_settings</span><span class="p">,</span> <span class="n">model_settings</span><span class="p">)</span>
    <span class="n">usage_limits</span> <span class="o">=</span> <span class="n">usage_limits</span> <span class="ow">or</span> <span class="n">_usage</span><span class="o">.</span><span class="n">UsageLimits</span><span class="p">()</span>

    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">model_used</span><span class="p">,</span> <span class="n">InstrumentedModel</span><span class="p">):</span>
        <span class="n">tracer</span> <span class="o">=</span> <span class="n">model_used</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">tracer</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">tracer</span> <span class="o">=</span> <span class="n">NoOpTracer</span><span class="p">()</span>
    <span class="n">agent_name</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="ow">or</span> <span class="s1">'agent'</span>
    <span class="n">run_span</span> <span class="o">=</span> <span class="n">tracer</span><span class="o">.</span><span class="n">start_span</span><span class="p">(</span>
        <span class="s1">'agent run'</span><span class="p">,</span>
        <span class="n">attributes</span><span class="o">=</span><span class="p">{</span>
            <span class="s1">'model_name'</span><span class="p">:</span> <span class="n">model_used</span><span class="o">.</span><span class="n">model_name</span> <span class="k">if</span> <span class="n">model_used</span> <span class="k">else</span> <span class="s1">'no-model'</span><span class="p">,</span>
            <span class="s1">'agent_name'</span><span class="p">:</span> <span class="n">agent_name</span><span class="p">,</span>
            <span class="s1">'logfire.msg'</span><span class="p">:</span> <span class="sa">f</span><span class="s1">'</span><span class="si">{</span><span class="n">agent_name</span><span class="si">}</span><span class="s1"> run'</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">)</span>

    <span class="n">graph_deps</span> <span class="o">=</span> <span class="n">_agent_graph</span><span class="o">.</span><span class="n">GraphAgentDeps</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">,</span> <span class="n">RunResultDataT</span><span class="p">](</span>
        <span class="n">user_deps</span><span class="o">=</span><span class="n">deps</span><span class="p">,</span>
        <span class="n">prompt</span><span class="o">=</span><span class="n">user_prompt</span><span class="p">,</span>
        <span class="n">new_message_index</span><span class="o">=</span><span class="n">new_message_index</span><span class="p">,</span>
        <span class="n">model</span><span class="o">=</span><span class="n">model_used</span><span class="p">,</span>
        <span class="n">model_settings</span><span class="o">=</span><span class="n">model_settings</span><span class="p">,</span>
        <span class="n">usage_limits</span><span class="o">=</span><span class="n">usage_limits</span><span class="p">,</span>
        <span class="n">max_result_retries</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_max_result_retries</span><span class="p">,</span>
        <span class="n">end_strategy</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">end_strategy</span><span class="p">,</span>
        <span class="n">result_schema</span><span class="o">=</span><span class="n">result_schema</span><span class="p">,</span>
        <span class="n">result_tools</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_result_schema</span><span class="o">.</span><span class="n">tool_defs</span><span class="p">()</span> <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_result_schema</span> <span class="k">else</span> <span class="p">[],</span>
        <span class="n">result_validators</span><span class="o">=</span><span class="n">result_validators</span><span class="p">,</span>
        <span class="n">function_tools</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_function_tools</span><span class="p">,</span>
        <span class="n">mcp_servers</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_mcp_servers</span><span class="p">,</span>
        <span class="n">run_span</span><span class="o">=</span><span class="n">run_span</span><span class="p">,</span>
        <span class="n">tracer</span><span class="o">=</span><span class="n">tracer</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">start_node</span> <span class="o">=</span> <span class="n">_agent_graph</span><span class="o">.</span><span class="n">UserPromptNode</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">](</span>
        <span class="n">user_prompt</span><span class="o">=</span><span class="n">user_prompt</span><span class="p">,</span>
        <span class="n">system_prompts</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_system_prompts</span><span class="p">,</span>
        <span class="n">system_prompt_functions</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_system_prompt_functions</span><span class="p">,</span>
        <span class="n">system_prompt_dynamic_functions</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_system_prompt_dynamic_functions</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="k">async</span> <span class="k">with</span> <span class="n">graph</span><span class="o">.</span><span class="n">iter</span><span class="p">(</span>
        <span class="n">start_node</span><span class="p">,</span>
        <span class="n">state</span><span class="o">=</span><span class="n">state</span><span class="p">,</span>
        <span class="n">deps</span><span class="o">=</span><span class="n">graph_deps</span><span class="p">,</span>
        <span class="n">span</span><span class="o">=</span><span class="n">use_span</span><span class="p">(</span><span class="n">run_span</span><span class="p">,</span> <span class="n">end_on_exit</span><span class="o">=</span><span class="kc">True</span><span class="p">),</span>
        <span class="n">infer_name</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="k">as</span> <span class="n">graph_run</span><span class="p">:</span>
        <span class="k">yield</span> <span class="n">AgentRun</span><span class="p">(</span><span class="n">graph_run</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.agent.Agent.run_sync" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">run_sync</span>


</h4>
          <div class="doc-overloads">
<div class="language-python doc-signature highlight"><pre id="__code_20"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_20 > code"></button><code><span class="nf">run_sync</span><span class="p">(</span>
    <span class="n">user_prompt</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="collections.abc.Sequence" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence">Sequence</a></span><span class="p">[</span><span class="n"><span title="pydantic_ai.messages.UserContent">UserContent</span></span><span class="p">],</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">message_history</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list">list</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ModelMessage" href="../messages/#pydantic_ai.messages.ModelMessage">ModelMessage</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">model</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.Model" href="../models/base/#pydantic_ai.models.Model">Model</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.KnownModelName" href="../models/base/#pydantic_ai.models.KnownModelName">KnownModelName</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">deps</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">model_settings</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.settings.ModelSettings" href="../settings/#pydantic_ai.settings.ModelSettings">ModelSettings</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">usage_limits</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.usage.UsageLimits" href="../usage/#pydantic_ai.usage.UsageLimits">UsageLimits</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">usage</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.usage.Usage" href="../usage/#pydantic_ai.usage.Usage">Usage</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">infer_name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">True</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.agent.AgentRunResult" href="#pydantic_ai.agent.AgentRunResult">AgentRunResult</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.result.ResultDataT" href="../result/#pydantic_ai.result.ResultDataT">ResultDataT</a></span><span class="p">]</span>
</code></pre></div><div class="language-python doc-signature highlight"><pre id="__code_21"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_21 > code"></button><code><span class="nf">run_sync</span><span class="p">(</span>
    <span class="n">user_prompt</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="collections.abc.Sequence" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence">Sequence</a></span><span class="p">[</span><span class="n"><span title="pydantic_ai.messages.UserContent">UserContent</span></span><span class="p">],</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">result_type</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type">type</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.agent.RunResultDataT" href="#pydantic_ai.agent.RunResultDataT">RunResultDataT</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">message_history</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list">list</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ModelMessage" href="../messages/#pydantic_ai.messages.ModelMessage">ModelMessage</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">model</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.Model" href="../models/base/#pydantic_ai.models.Model">Model</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.KnownModelName" href="../models/base/#pydantic_ai.models.KnownModelName">KnownModelName</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">deps</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">model_settings</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.settings.ModelSettings" href="../settings/#pydantic_ai.settings.ModelSettings">ModelSettings</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">usage_limits</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.usage.UsageLimits" href="../usage/#pydantic_ai.usage.UsageLimits">UsageLimits</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">usage</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.usage.Usage" href="../usage/#pydantic_ai.usage.Usage">Usage</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">infer_name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">True</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.agent.AgentRunResult" href="#pydantic_ai.agent.AgentRunResult">AgentRunResult</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.agent.RunResultDataT" href="#pydantic_ai.agent.RunResultDataT">RunResultDataT</a></span><span class="p">]</span>
</code></pre></div>          </div>
<div class="language-python doc-signature highlight"><pre id="__code_22"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_22 > code"></button><code><span class="nf">run_sync</span><span class="p">(</span>
    <span class="n">user_prompt</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="collections.abc.Sequence" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence">Sequence</a></span><span class="p">[</span><span class="n"><span title="pydantic_ai.messages.UserContent">UserContent</span></span><span class="p">],</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">result_type</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type">type</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.agent.RunResultDataT" href="#pydantic_ai.agent.RunResultDataT">RunResultDataT</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">message_history</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list">list</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ModelMessage" href="../messages/#pydantic_ai.messages.ModelMessage">ModelMessage</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">model</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.Model" href="../models/base/#pydantic_ai.models.Model">Model</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.KnownModelName" href="../models/base/#pydantic_ai.models.KnownModelName">KnownModelName</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">deps</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">model_settings</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.settings.ModelSettings" href="../settings/#pydantic_ai.settings.ModelSettings">ModelSettings</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">usage_limits</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.usage.UsageLimits" href="../usage/#pydantic_ai.usage.UsageLimits">UsageLimits</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">usage</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.usage.Usage" href="../usage/#pydantic_ai.usage.Usage">Usage</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">infer_name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">True</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.agent.AgentRunResult" href="#pydantic_ai.agent.AgentRunResult">AgentRunResult</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a></span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Synchronously run the agent with a user prompt.</p>
<p>This is a convenience method that wraps <a class="autorefs autorefs-internal" href="#pydantic_ai.agent.Agent.run"><code>self.run</code></a> with <code>loop.run_until_complete(...)</code>.
You therefore can't use this method inside async code or if there's an active event loop.</p>
<p>Example:
</p><div class="language-python highlight"><pre id="__code_23"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_23 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>

<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="s1">'openai:gpt-4o'</span><span class="p">)</span>

<span class="n">result_sync</span> <span class="o">=</span> <span class="n">agent</span><span class="o">.</span><span class="n">run_sync</span><span class="p">(</span><span class="s1">'What is the capital of Italy?'</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">result_sync</span><span class="o">.</span><span class="n">data</span><span class="p">)</span>
<span class="c1">#&gt; Rome</span>
</code></pre></div><p></p>


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
                <code>user_prompt</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a> | <a class="autorefs autorefs-external" title="collections.abc.Sequence" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence">Sequence</a>[<span title="pydantic_ai.messages.UserContent">UserContent</span>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>User input to start/continue the conversation.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>result_type</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type">type</a>[<a class="autorefs autorefs-internal" title="pydantic_ai.agent.RunResultDataT" href="#pydantic_ai.agent.RunResultDataT">RunResultDataT</a>] | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Custom result type to use for this run, <code>result_type</code> may only be used if the agent has no
result validators since result validators would expect an argument that matches the agent's result type.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>message_history</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list">list</a>[<a class="autorefs autorefs-internal" title="pydantic_ai.messages.ModelMessage" href="../messages/#pydantic_ai.messages.ModelMessage">ModelMessage</a>] | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>History of the conversation so far.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>model</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_ai.models.Model" href="../models/base/#pydantic_ai.models.Model">Model</a> | <a class="autorefs autorefs-internal" title="pydantic_ai.models.KnownModelName" href="../models/base/#pydantic_ai.models.KnownModelName">KnownModelName</a> | <a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Optional model to use for this run, required if <code>model</code> was not set when creating the agent.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>deps</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Optional dependencies to use for this run.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>model_settings</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_ai.settings.ModelSettings" href="../settings/#pydantic_ai.settings.ModelSettings">ModelSettings</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Optional settings to use for this model's request.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>usage_limits</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_ai.usage.UsageLimits" href="../usage/#pydantic_ai.usage.UsageLimits">UsageLimits</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Optional limits on model request count or token usage.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>usage</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_ai.usage.Usage" href="../usage/#pydantic_ai.usage.Usage">Usage</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Optional usage to start with, useful for resuming a conversation or agents used in tools.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>infer_name</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Whether to try to infer the agent name from the call frame if it's not set.</p>
              </div>
            </td>
            <td>
                  <code>True</code>
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
                  <code><a class="autorefs autorefs-internal" title="pydantic_ai.agent.AgentRunResult" href="#pydantic_ai.agent.AgentRunResult">AgentRunResult</a>[<a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The result of the run.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/agent.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">526</span>
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
<span class="normal">538</span>
<span class="normal">539</span>
<span class="normal">540</span>
<span class="normal">541</span>
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
<span class="normal">584</span></pre></div></td><td class="code"><div><pre id="__code_24"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_24 > code"></button><code tabindex="0"><span class="k">def</span><span class="w"> </span><span class="nf">run_sync</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">user_prompt</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">_messages</span><span class="o">.</span><span class="n">UserContent</span><span class="p">],</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">result_type</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n">RunResultDataT</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">message_history</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">_messages</span><span class="o">.</span><span class="n">ModelMessage</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">model</span><span class="p">:</span> <span class="n">models</span><span class="o">.</span><span class="n">Model</span> <span class="o">|</span> <span class="n">models</span><span class="o">.</span><span class="n">KnownModelName</span> <span class="o">|</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">deps</span><span class="p">:</span> <span class="n">AgentDepsT</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">model_settings</span><span class="p">:</span> <span class="n">ModelSettings</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">usage_limits</span><span class="p">:</span> <span class="n">_usage</span><span class="o">.</span><span class="n">UsageLimits</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">usage</span><span class="p">:</span> <span class="n">_usage</span><span class="o">.</span><span class="n">Usage</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">infer_name</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AgentRunResult</span><span class="p">[</span><span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Synchronously run the agent with a user prompt.</span>

<span class="sd">    This is a convenience method that wraps [`self.run`][pydantic_ai.Agent.run] with `loop.run_until_complete(...)`.</span>
<span class="sd">    You therefore can't use this method inside async code or if there's an active event loop.</span>

<span class="sd">    Example:</span>
<span class="sd">    ```python</span>
<span class="sd">    from pydantic_ai import Agent</span>

<span class="sd">    agent = Agent('openai:gpt-4o')</span>

<span class="sd">    result_sync = agent.run_sync('What is the capital of Italy?')</span>
<span class="sd">    print(result_sync.data)</span>
<span class="sd">    #&gt; Rome</span>
<span class="sd">    ```</span>

<span class="sd">    Args:</span>
<span class="sd">        user_prompt: User input to start/continue the conversation.</span>
<span class="sd">        result_type: Custom result type to use for this run, `result_type` may only be used if the agent has no</span>
<span class="sd">            result validators since result validators would expect an argument that matches the agent's result type.</span>
<span class="sd">        message_history: History of the conversation so far.</span>
<span class="sd">        model: Optional model to use for this run, required if `model` was not set when creating the agent.</span>
<span class="sd">        deps: Optional dependencies to use for this run.</span>
<span class="sd">        model_settings: Optional settings to use for this model's request.</span>
<span class="sd">        usage_limits: Optional limits on model request count or token usage.</span>
<span class="sd">        usage: Optional usage to start with, useful for resuming a conversation or agents used in tools.</span>
<span class="sd">        infer_name: Whether to try to infer the agent name from the call frame if it's not set.</span>

<span class="sd">    Returns:</span>
<span class="sd">        The result of the run.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="n">infer_name</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_infer_name</span><span class="p">(</span><span class="n">inspect</span><span class="o">.</span><span class="n">currentframe</span><span class="p">())</span>
    <span class="k">return</span> <span class="n">get_event_loop</span><span class="p">()</span><span class="o">.</span><span class="n">run_until_complete</span><span class="p">(</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">run</span><span class="p">(</span>
            <span class="n">user_prompt</span><span class="p">,</span>
            <span class="n">result_type</span><span class="o">=</span><span class="n">result_type</span><span class="p">,</span>
            <span class="n">message_history</span><span class="o">=</span><span class="n">message_history</span><span class="p">,</span>
            <span class="n">model</span><span class="o">=</span><span class="n">model</span><span class="p">,</span>
            <span class="n">deps</span><span class="o">=</span><span class="n">deps</span><span class="p">,</span>
            <span class="n">model_settings</span><span class="o">=</span><span class="n">model_settings</span><span class="p">,</span>
            <span class="n">usage_limits</span><span class="o">=</span><span class="n">usage_limits</span><span class="p">,</span>
            <span class="n">usage</span><span class="o">=</span><span class="n">usage</span><span class="p">,</span>
            <span class="n">infer_name</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
        <span class="p">)</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.agent.Agent.run_stream" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">run_stream</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-async"><code>async</code></small>
  </span>

</h4>
          <div class="doc-overloads">
<div class="language-python doc-signature highlight"><pre id="__code_25"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_25 > code"></button><code><span class="nf">run_stream</span><span class="p">(</span>
    <span class="n">user_prompt</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="collections.abc.Sequence" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence">Sequence</a></span><span class="p">[</span><span class="n"><span title="pydantic_ai.messages.UserContent">UserContent</span></span><span class="p">],</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">result_type</span><span class="p">:</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">message_history</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list">list</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ModelMessage" href="../messages/#pydantic_ai.messages.ModelMessage">ModelMessage</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">model</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.Model" href="../models/base/#pydantic_ai.models.Model">Model</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.KnownModelName" href="../models/base/#pydantic_ai.models.KnownModelName">KnownModelName</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">deps</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">model_settings</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.settings.ModelSettings" href="../settings/#pydantic_ai.settings.ModelSettings">ModelSettings</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">usage_limits</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.usage.UsageLimits" href="../usage/#pydantic_ai.usage.UsageLimits">UsageLimits</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">usage</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.usage.Usage" href="../usage/#pydantic_ai.usage.Usage">Usage</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">infer_name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">True</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" title="contextlib.AbstractAsyncContextManager" href="https://docs.python.org/3/library/contextlib.html#contextlib.AbstractAsyncContextManager">AbstractAsyncContextManager</a></span><span class="p">[</span>
    <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.result.StreamedRunResult" href="../result/#pydantic_ai.result.StreamedRunResult">StreamedRunResult</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.result.ResultDataT" href="../result/#pydantic_ai.result.ResultDataT">ResultDataT</a></span><span class="p">]</span>
<span class="p">]</span>
</code></pre></div><div class="language-python doc-signature highlight"><pre id="__code_26"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_26 > code"></button><code><span class="nf">run_stream</span><span class="p">(</span>
    <span class="n">user_prompt</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="collections.abc.Sequence" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence">Sequence</a></span><span class="p">[</span><span class="n"><span title="pydantic_ai.messages.UserContent">UserContent</span></span><span class="p">],</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">result_type</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type">type</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.agent.RunResultDataT" href="#pydantic_ai.agent.RunResultDataT">RunResultDataT</a></span><span class="p">],</span>
    <span class="n">message_history</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list">list</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ModelMessage" href="../messages/#pydantic_ai.messages.ModelMessage">ModelMessage</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">model</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.Model" href="../models/base/#pydantic_ai.models.Model">Model</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.KnownModelName" href="../models/base/#pydantic_ai.models.KnownModelName">KnownModelName</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">deps</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">model_settings</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.settings.ModelSettings" href="../settings/#pydantic_ai.settings.ModelSettings">ModelSettings</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">usage_limits</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.usage.UsageLimits" href="../usage/#pydantic_ai.usage.UsageLimits">UsageLimits</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">usage</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.usage.Usage" href="../usage/#pydantic_ai.usage.Usage">Usage</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">infer_name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">True</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" title="contextlib.AbstractAsyncContextManager" href="https://docs.python.org/3/library/contextlib.html#contextlib.AbstractAsyncContextManager">AbstractAsyncContextManager</a></span><span class="p">[</span>
    <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.result.StreamedRunResult" href="../result/#pydantic_ai.result.StreamedRunResult">StreamedRunResult</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.agent.RunResultDataT" href="#pydantic_ai.agent.RunResultDataT">RunResultDataT</a></span><span class="p">]</span>
<span class="p">]</span>
</code></pre></div>          </div>
<div class="language-python doc-signature highlight"><pre id="__code_27"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_27 > code"></button><code><span class="nf">run_stream</span><span class="p">(</span>
    <span class="n">user_prompt</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="collections.abc.Sequence" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence">Sequence</a></span><span class="p">[</span><span class="n"><span title="pydantic_ai.messages.UserContent">UserContent</span></span><span class="p">],</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">result_type</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type">type</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.agent.RunResultDataT" href="#pydantic_ai.agent.RunResultDataT">RunResultDataT</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">message_history</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list">list</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ModelMessage" href="../messages/#pydantic_ai.messages.ModelMessage">ModelMessage</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">model</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.Model" href="../models/base/#pydantic_ai.models.Model">Model</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.KnownModelName" href="../models/base/#pydantic_ai.models.KnownModelName">KnownModelName</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">deps</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">model_settings</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.settings.ModelSettings" href="../settings/#pydantic_ai.settings.ModelSettings">ModelSettings</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">usage_limits</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.usage.UsageLimits" href="../usage/#pydantic_ai.usage.UsageLimits">UsageLimits</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">usage</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.usage.Usage" href="../usage/#pydantic_ai.usage.Usage">Usage</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">infer_name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">True</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" title="collections.abc.AsyncIterator" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator">AsyncIterator</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.result.StreamedRunResult" href="../result/#pydantic_ai.result.StreamedRunResult">StreamedRunResult</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a></span><span class="p">]]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Run the agent with a user prompt in async mode, returning a streamed response.</p>
<p>Example:
</p><div class="language-python highlight"><pre id="__code_28"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_28 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>

<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="s1">'openai:gpt-4o'</span><span class="p">)</span>

<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">main</span><span class="p">():</span>
    <span class="k">async</span> <span class="k">with</span> <span class="n">agent</span><span class="o">.</span><span class="n">run_stream</span><span class="p">(</span><span class="s1">'What is the capital of the UK?'</span><span class="p">)</span> <span class="k">as</span> <span class="n">response</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="k">await</span> <span class="n">response</span><span class="o">.</span><span class="n">get_data</span><span class="p">())</span>
        <span class="c1">#&gt; London</span>
</code></pre></div><p></p>


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
                <code>user_prompt</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a> | <a class="autorefs autorefs-external" title="collections.abc.Sequence" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence">Sequence</a>[<span title="pydantic_ai.messages.UserContent">UserContent</span>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>User input to start/continue the conversation.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>result_type</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type">type</a>[<a class="autorefs autorefs-internal" title="pydantic_ai.agent.RunResultDataT" href="#pydantic_ai.agent.RunResultDataT">RunResultDataT</a>] | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Custom result type to use for this run, <code>result_type</code> may only be used if the agent has no
result validators since result validators would expect an argument that matches the agent's result type.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>message_history</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list">list</a>[<a class="autorefs autorefs-internal" title="pydantic_ai.messages.ModelMessage" href="../messages/#pydantic_ai.messages.ModelMessage">ModelMessage</a>] | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>History of the conversation so far.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>model</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_ai.models.Model" href="../models/base/#pydantic_ai.models.Model">Model</a> | <a class="autorefs autorefs-internal" title="pydantic_ai.models.KnownModelName" href="../models/base/#pydantic_ai.models.KnownModelName">KnownModelName</a> | <a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Optional model to use for this run, required if <code>model</code> was not set when creating the agent.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>deps</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Optional dependencies to use for this run.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>model_settings</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_ai.settings.ModelSettings" href="../settings/#pydantic_ai.settings.ModelSettings">ModelSettings</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Optional settings to use for this model's request.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>usage_limits</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_ai.usage.UsageLimits" href="../usage/#pydantic_ai.usage.UsageLimits">UsageLimits</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Optional limits on model request count or token usage.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>usage</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_ai.usage.Usage" href="../usage/#pydantic_ai.usage.Usage">Usage</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Optional usage to start with, useful for resuming a conversation or agents used in tools.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>infer_name</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Whether to try to infer the agent name from the call frame if it's not set.</p>
              </div>
            </td>
            <td>
                  <code>True</code>
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
                  <code><a class="autorefs autorefs-external" title="collections.abc.AsyncIterator" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator">AsyncIterator</a>[<a class="autorefs autorefs-internal" title="pydantic_ai.result.StreamedRunResult" href="../result/#pydantic_ai.result.StreamedRunResult">StreamedRunResult</a>[<a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a>, <a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a>]]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The result of the run.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/agent.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">616</span>
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
<span class="normal">653</span>
<span class="normal">654</span>
<span class="normal">655</span>
<span class="normal">656</span>
<span class="normal">657</span>
<span class="normal">658</span>
<span class="normal">659</span>
<span class="normal">660</span>
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
<span class="normal">675</span>
<span class="normal">676</span>
<span class="normal">677</span>
<span class="normal">678</span>
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
<span class="normal">689</span>
<span class="normal">690</span>
<span class="normal">691</span>
<span class="normal">692</span>
<span class="normal">693</span>
<span class="normal">694</span>
<span class="normal">695</span>
<span class="normal">696</span>
<span class="normal">697</span>
<span class="normal">698</span>
<span class="normal">699</span>
<span class="normal">700</span>
<span class="normal">701</span>
<span class="normal">702</span>
<span class="normal">703</span>
<span class="normal">704</span>
<span class="normal">705</span>
<span class="normal">706</span>
<span class="normal">707</span>
<span class="normal">708</span>
<span class="normal">709</span>
<span class="normal">710</span>
<span class="normal">711</span>
<span class="normal">712</span>
<span class="normal">713</span>
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
<span class="normal">725</span>
<span class="normal">726</span>
<span class="normal">727</span>
<span class="normal">728</span>
<span class="normal">729</span>
<span class="normal">730</span>
<span class="normal">731</span>
<span class="normal">732</span>
<span class="normal">733</span>
<span class="normal">734</span>
<span class="normal">735</span>
<span class="normal">736</span>
<span class="normal">737</span>
<span class="normal">738</span>
<span class="normal">739</span>
<span class="normal">740</span>
<span class="normal">741</span>
<span class="normal">742</span>
<span class="normal">743</span>
<span class="normal">744</span>
<span class="normal">745</span>
<span class="normal">746</span>
<span class="normal">747</span>
<span class="normal">748</span>
<span class="normal">749</span>
<span class="normal">750</span>
<span class="normal">751</span>
<span class="normal">752</span>
<span class="normal">753</span>
<span class="normal">754</span>
<span class="normal">755</span></pre></div></td><td class="code"><div><pre id="__code_29"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_29 > code"></button><code tabindex="0"><span class="nd">@asynccontextmanager</span>
<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">run_stream</span><span class="p">(</span>  <span class="c1"># noqa C901</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">user_prompt</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">_messages</span><span class="o">.</span><span class="n">UserContent</span><span class="p">],</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">result_type</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n">RunResultDataT</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">message_history</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">_messages</span><span class="o">.</span><span class="n">ModelMessage</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">model</span><span class="p">:</span> <span class="n">models</span><span class="o">.</span><span class="n">Model</span> <span class="o">|</span> <span class="n">models</span><span class="o">.</span><span class="n">KnownModelName</span> <span class="o">|</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">deps</span><span class="p">:</span> <span class="n">AgentDepsT</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">model_settings</span><span class="p">:</span> <span class="n">ModelSettings</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">usage_limits</span><span class="p">:</span> <span class="n">_usage</span><span class="o">.</span><span class="n">UsageLimits</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">usage</span><span class="p">:</span> <span class="n">_usage</span><span class="o">.</span><span class="n">Usage</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">infer_name</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AsyncIterator</span><span class="p">[</span><span class="n">result</span><span class="o">.</span><span class="n">StreamedRunResult</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]:</span>
<span class="w">    </span><span class="sd">"""Run the agent with a user prompt in async mode, returning a streamed response.</span>

<span class="sd">    Example:</span>
<span class="sd">    ```python</span>
<span class="sd">    from pydantic_ai import Agent</span>

<span class="sd">    agent = Agent('openai:gpt-4o')</span>

<span class="sd">    async def main():</span>
<span class="sd">        async with agent.run_stream('What is the capital of the UK?') as response:</span>
<span class="sd">            print(await response.get_data())</span>
<span class="sd">            #&gt; London</span>
<span class="sd">    ```</span>

<span class="sd">    Args:</span>
<span class="sd">        user_prompt: User input to start/continue the conversation.</span>
<span class="sd">        result_type: Custom result type to use for this run, `result_type` may only be used if the agent has no</span>
<span class="sd">            result validators since result validators would expect an argument that matches the agent's result type.</span>
<span class="sd">        message_history: History of the conversation so far.</span>
<span class="sd">        model: Optional model to use for this run, required if `model` was not set when creating the agent.</span>
<span class="sd">        deps: Optional dependencies to use for this run.</span>
<span class="sd">        model_settings: Optional settings to use for this model's request.</span>
<span class="sd">        usage_limits: Optional limits on model request count or token usage.</span>
<span class="sd">        usage: Optional usage to start with, useful for resuming a conversation or agents used in tools.</span>
<span class="sd">        infer_name: Whether to try to infer the agent name from the call frame if it's not set.</span>

<span class="sd">    Returns:</span>
<span class="sd">        The result of the run.</span>
<span class="sd">    """</span>
    <span class="c1"># TODO: We need to deprecate this now that we have the `iter` method.</span>
    <span class="c1">#   Before that, though, we should add an event for when we reach the final result of the stream.</span>
    <span class="k">if</span> <span class="n">infer_name</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="c1"># f_back because `asynccontextmanager` adds one frame</span>
        <span class="k">if</span> <span class="n">frame</span> <span class="o">:=</span> <span class="n">inspect</span><span class="o">.</span><span class="n">currentframe</span><span class="p">():</span>  <span class="c1"># pragma: no branch</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_infer_name</span><span class="p">(</span><span class="n">frame</span><span class="o">.</span><span class="n">f_back</span><span class="p">)</span>

    <span class="n">yielded</span> <span class="o">=</span> <span class="kc">False</span>
    <span class="k">async</span> <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">iter</span><span class="p">(</span>
        <span class="n">user_prompt</span><span class="p">,</span>
        <span class="n">result_type</span><span class="o">=</span><span class="n">result_type</span><span class="p">,</span>
        <span class="n">message_history</span><span class="o">=</span><span class="n">message_history</span><span class="p">,</span>
        <span class="n">model</span><span class="o">=</span><span class="n">model</span><span class="p">,</span>
        <span class="n">deps</span><span class="o">=</span><span class="n">deps</span><span class="p">,</span>
        <span class="n">model_settings</span><span class="o">=</span><span class="n">model_settings</span><span class="p">,</span>
        <span class="n">usage_limits</span><span class="o">=</span><span class="n">usage_limits</span><span class="p">,</span>
        <span class="n">usage</span><span class="o">=</span><span class="n">usage</span><span class="p">,</span>
        <span class="n">infer_name</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="k">as</span> <span class="n">agent_run</span><span class="p">:</span>
        <span class="n">first_node</span> <span class="o">=</span> <span class="n">agent_run</span><span class="o">.</span><span class="n">next_node</span>  <span class="c1"># start with the first node</span>
        <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">first_node</span><span class="p">,</span> <span class="n">_agent_graph</span><span class="o">.</span><span class="n">UserPromptNode</span><span class="p">)</span>  <span class="c1"># the first node should be a user prompt node</span>
        <span class="n">node</span> <span class="o">=</span> <span class="n">first_node</span>
        <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">is_model_request_node</span><span class="p">(</span><span class="n">node</span><span class="p">):</span>
                <span class="n">graph_ctx</span> <span class="o">=</span> <span class="n">agent_run</span><span class="o">.</span><span class="n">ctx</span>
                <span class="k">async</span> <span class="k">with</span> <span class="n">node</span><span class="o">.</span><span class="n">_stream</span><span class="p">(</span><span class="n">graph_ctx</span><span class="p">)</span> <span class="k">as</span> <span class="n">streamed_response</span><span class="p">:</span>  <span class="c1"># pyright: ignore[reportPrivateUsage]</span>

                    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">stream_to_final</span><span class="p">(</span>
                        <span class="n">s</span><span class="p">:</span> <span class="n">models</span><span class="o">.</span><span class="n">StreamedResponse</span><span class="p">,</span>
                    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">FinalResult</span><span class="p">[</span><span class="n">models</span><span class="o">.</span><span class="n">StreamedResponse</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span><span class="p">:</span>
                        <span class="n">result_schema</span> <span class="o">=</span> <span class="n">graph_ctx</span><span class="o">.</span><span class="n">deps</span><span class="o">.</span><span class="n">result_schema</span>
                        <span class="k">async</span> <span class="k">for</span> <span class="n">maybe_part_event</span> <span class="ow">in</span> <span class="n">streamed_response</span><span class="p">:</span>
                            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">maybe_part_event</span><span class="p">,</span> <span class="n">_messages</span><span class="o">.</span><span class="n">PartStartEvent</span><span class="p">):</span>
                                <span class="n">new_part</span> <span class="o">=</span> <span class="n">maybe_part_event</span><span class="o">.</span><span class="n">part</span>
                                <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">new_part</span><span class="p">,</span> <span class="n">_messages</span><span class="o">.</span><span class="n">TextPart</span><span class="p">):</span>
                                    <span class="k">if</span> <span class="n">_agent_graph</span><span class="o">.</span><span class="n">allow_text_result</span><span class="p">(</span><span class="n">result_schema</span><span class="p">):</span>
                                        <span class="k">return</span> <span class="n">FinalResult</span><span class="p">(</span><span class="n">s</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
                                <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">new_part</span><span class="p">,</span> <span class="n">_messages</span><span class="o">.</span><span class="n">ToolCallPart</span><span class="p">)</span> <span class="ow">and</span> <span class="n">result_schema</span><span class="p">:</span>
                                    <span class="k">for</span> <span class="n">call</span><span class="p">,</span> <span class="n">_</span> <span class="ow">in</span> <span class="n">result_schema</span><span class="o">.</span><span class="n">find_tool</span><span class="p">([</span><span class="n">new_part</span><span class="p">]):</span>
                                        <span class="k">return</span> <span class="n">FinalResult</span><span class="p">(</span><span class="n">s</span><span class="p">,</span> <span class="n">call</span><span class="o">.</span><span class="n">tool_name</span><span class="p">,</span> <span class="n">call</span><span class="o">.</span><span class="n">tool_call_id</span><span class="p">)</span>
                        <span class="k">return</span> <span class="kc">None</span>

                    <span class="n">final_result_details</span> <span class="o">=</span> <span class="k">await</span> <span class="n">stream_to_final</span><span class="p">(</span><span class="n">streamed_response</span><span class="p">)</span>
                    <span class="k">if</span> <span class="n">final_result_details</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                        <span class="k">if</span> <span class="n">yielded</span><span class="p">:</span>
                            <span class="k">raise</span> <span class="n">exceptions</span><span class="o">.</span><span class="n">AgentRunError</span><span class="p">(</span><span class="s1">'Agent run produced final results'</span><span class="p">)</span>
                        <span class="n">yielded</span> <span class="o">=</span> <span class="kc">True</span>

                        <span class="n">messages</span> <span class="o">=</span> <span class="n">graph_ctx</span><span class="o">.</span><span class="n">state</span><span class="o">.</span><span class="n">message_history</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>

                        <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">on_complete</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">                            </span><span class="sd">"""Called when the stream has completed.</span>

<span class="sd">                            The model response will have been added to messages by now</span>
<span class="sd">                            by `StreamedRunResult._marked_completed`.</span>
<span class="sd">                            """</span>
                            <span class="n">last_message</span> <span class="o">=</span> <span class="n">messages</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>
                            <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">last_message</span><span class="p">,</span> <span class="n">_messages</span><span class="o">.</span><span class="n">ModelResponse</span><span class="p">)</span>
                            <span class="n">tool_calls</span> <span class="o">=</span> <span class="p">[</span>
                                <span class="n">part</span> <span class="k">for</span> <span class="n">part</span> <span class="ow">in</span> <span class="n">last_message</span><span class="o">.</span><span class="n">parts</span> <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">part</span><span class="p">,</span> <span class="n">_messages</span><span class="o">.</span><span class="n">ToolCallPart</span><span class="p">)</span>
                            <span class="p">]</span>

                            <span class="n">parts</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">_messages</span><span class="o">.</span><span class="n">ModelRequestPart</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
                            <span class="k">async</span> <span class="k">for</span> <span class="n">_event</span> <span class="ow">in</span> <span class="n">_agent_graph</span><span class="o">.</span><span class="n">process_function_tools</span><span class="p">(</span>
                                <span class="n">tool_calls</span><span class="p">,</span>
                                <span class="n">final_result_details</span><span class="o">.</span><span class="n">tool_name</span><span class="p">,</span>
                                <span class="n">final_result_details</span><span class="o">.</span><span class="n">tool_call_id</span><span class="p">,</span>
                                <span class="n">graph_ctx</span><span class="p">,</span>
                                <span class="n">parts</span><span class="p">,</span>
                            <span class="p">):</span>
                                <span class="k">pass</span>
                            <span class="c1"># TODO: Should we do something here related to the retry count?</span>
                            <span class="c1">#   Maybe we should move the incrementing of the retry count to where we actually make a request?</span>
                            <span class="c1"># if any(isinstance(part, _messages.RetryPromptPart) for part in parts):</span>
                            <span class="c1">#     ctx.state.increment_retries(ctx.deps.max_result_retries)</span>
                            <span class="k">if</span> <span class="n">parts</span><span class="p">:</span>
                                <span class="n">messages</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">_messages</span><span class="o">.</span><span class="n">ModelRequest</span><span class="p">(</span><span class="n">parts</span><span class="p">))</span>

                        <span class="k">yield</span> <span class="n">StreamedRunResult</span><span class="p">(</span>
                            <span class="n">messages</span><span class="p">,</span>
                            <span class="n">graph_ctx</span><span class="o">.</span><span class="n">deps</span><span class="o">.</span><span class="n">new_message_index</span><span class="p">,</span>
                            <span class="n">graph_ctx</span><span class="o">.</span><span class="n">deps</span><span class="o">.</span><span class="n">usage_limits</span><span class="p">,</span>
                            <span class="n">streamed_response</span><span class="p">,</span>
                            <span class="n">graph_ctx</span><span class="o">.</span><span class="n">deps</span><span class="o">.</span><span class="n">result_schema</span><span class="p">,</span>
                            <span class="n">_agent_graph</span><span class="o">.</span><span class="n">build_run_context</span><span class="p">(</span><span class="n">graph_ctx</span><span class="p">),</span>
                            <span class="n">graph_ctx</span><span class="o">.</span><span class="n">deps</span><span class="o">.</span><span class="n">result_validators</span><span class="p">,</span>
                            <span class="n">final_result_details</span><span class="o">.</span><span class="n">tool_name</span><span class="p">,</span>
                            <span class="n">on_complete</span><span class="p">,</span>
                        <span class="p">)</span>
                        <span class="k">break</span>
            <span class="n">next_node</span> <span class="o">=</span> <span class="k">await</span> <span class="n">agent_run</span><span class="o">.</span><span class="n">next</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">next_node</span><span class="p">,</span> <span class="n">_agent_graph</span><span class="o">.</span><span class="n">AgentNode</span><span class="p">):</span>
                <span class="k">raise</span> <span class="n">exceptions</span><span class="o">.</span><span class="n">AgentRunError</span><span class="p">(</span><span class="s1">'Should have produced a StreamedRunResult before getting here'</span><span class="p">)</span>
            <span class="n">node</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">_agent_graph</span><span class="o">.</span><span class="n">AgentNode</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span> <span class="n">next_node</span><span class="p">)</span>

    <span class="k">if</span> <span class="ow">not</span> <span class="n">yielded</span><span class="p">:</span>
        <span class="k">raise</span> <span class="n">exceptions</span><span class="o">.</span><span class="n">AgentRunError</span><span class="p">(</span><span class="s1">'Agent run finished without producing a final result'</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.agent.Agent.override" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">override</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_30"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_30 > code"></button><code><span class="nf">override</span><span class="p">(</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">deps</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span> <span class="o">|</span> <span class="n"><span title="pydantic_ai._utils.Unset">Unset</span></span> <span class="o">=</span> <span class="n"><span title="pydantic_ai._utils.UNSET">UNSET</span></span><span class="p">,</span>
    <span class="n">model</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.Model" href="../models/base/#pydantic_ai.models.Model">Model</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.KnownModelName" href="../models/base/#pydantic_ai.models.KnownModelName">KnownModelName</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="n"><span title="pydantic_ai._utils.Unset">Unset</span></span> <span class="o">=</span> <span class="n"><span title="pydantic_ai._utils.UNSET">UNSET</span></span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" title="collections.abc.Iterator" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator">Iterator</a></span><span class="p">[</span><span class="kc">None</span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Context manager to temporarily override agent dependencies and model.</p>
<p>This is particularly useful when testing.
You can find an example of this <a href="../../testing/#overriding-model-via-pytest-fixtures">here</a>.</p>


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
                <code>deps</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a> | <span title="pydantic_ai._utils.Unset">Unset</span></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The dependencies to use instead of the dependencies passed to the agent run.</p>
              </div>
            </td>
            <td>
                  <code><span title="pydantic_ai._utils.UNSET">UNSET</span></code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>model</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_ai.models.Model" href="../models/base/#pydantic_ai.models.Model">Model</a> | <a class="autorefs autorefs-internal" title="pydantic_ai.models.KnownModelName" href="../models/base/#pydantic_ai.models.KnownModelName">KnownModelName</a> | <a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a> | <span title="pydantic_ai._utils.Unset">Unset</span></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The model to use instead of the model passed to the agent run.</p>
              </div>
            </td>
            <td>
                  <code><span title="pydantic_ai._utils.UNSET">UNSET</span></code>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/agent.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">757</span>
<span class="normal">758</span>
<span class="normal">759</span>
<span class="normal">760</span>
<span class="normal">761</span>
<span class="normal">762</span>
<span class="normal">763</span>
<span class="normal">764</span>
<span class="normal">765</span>
<span class="normal">766</span>
<span class="normal">767</span>
<span class="normal">768</span>
<span class="normal">769</span>
<span class="normal">770</span>
<span class="normal">771</span>
<span class="normal">772</span>
<span class="normal">773</span>
<span class="normal">774</span>
<span class="normal">775</span>
<span class="normal">776</span>
<span class="normal">777</span>
<span class="normal">778</span>
<span class="normal">779</span>
<span class="normal">780</span>
<span class="normal">781</span>
<span class="normal">782</span>
<span class="normal">783</span>
<span class="normal">784</span>
<span class="normal">785</span>
<span class="normal">786</span>
<span class="normal">787</span>
<span class="normal">788</span>
<span class="normal">789</span>
<span class="normal">790</span>
<span class="normal">791</span></pre></div></td><td class="code"><div><pre id="__code_31"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_31 > code"></button><code><span class="nd">@contextmanager</span>
<span class="k">def</span><span class="w"> </span><span class="nf">override</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">deps</span><span class="p">:</span> <span class="n">AgentDepsT</span> <span class="o">|</span> <span class="n">_utils</span><span class="o">.</span><span class="n">Unset</span> <span class="o">=</span> <span class="n">_utils</span><span class="o">.</span><span class="n">UNSET</span><span class="p">,</span>
    <span class="n">model</span><span class="p">:</span> <span class="n">models</span><span class="o">.</span><span class="n">Model</span> <span class="o">|</span> <span class="n">models</span><span class="o">.</span><span class="n">KnownModelName</span> <span class="o">|</span> <span class="nb">str</span> <span class="o">|</span> <span class="n">_utils</span><span class="o">.</span><span class="n">Unset</span> <span class="o">=</span> <span class="n">_utils</span><span class="o">.</span><span class="n">UNSET</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Iterator</span><span class="p">[</span><span class="kc">None</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Context manager to temporarily override agent dependencies and model.</span>

<span class="sd">    This is particularly useful when testing.</span>
<span class="sd">    You can find an example of this [here](../testing.md#overriding-model-via-pytest-fixtures).</span>

<span class="sd">    Args:</span>
<span class="sd">        deps: The dependencies to use instead of the dependencies passed to the agent run.</span>
<span class="sd">        model: The model to use instead of the model passed to the agent run.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="n">_utils</span><span class="o">.</span><span class="n">is_set</span><span class="p">(</span><span class="n">deps</span><span class="p">):</span>
        <span class="n">override_deps_before</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_override_deps</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_override_deps</span> <span class="o">=</span> <span class="n">_utils</span><span class="o">.</span><span class="n">Some</span><span class="p">(</span><span class="n">deps</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">override_deps_before</span> <span class="o">=</span> <span class="n">_utils</span><span class="o">.</span><span class="n">UNSET</span>

    <span class="k">if</span> <span class="n">_utils</span><span class="o">.</span><span class="n">is_set</span><span class="p">(</span><span class="n">model</span><span class="p">):</span>
        <span class="n">override_model_before</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_override_model</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_override_model</span> <span class="o">=</span> <span class="n">_utils</span><span class="o">.</span><span class="n">Some</span><span class="p">(</span><span class="n">models</span><span class="o">.</span><span class="n">infer_model</span><span class="p">(</span><span class="n">model</span><span class="p">))</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">override_model_before</span> <span class="o">=</span> <span class="n">_utils</span><span class="o">.</span><span class="n">UNSET</span>

    <span class="k">try</span><span class="p">:</span>
        <span class="k">yield</span>
    <span class="k">finally</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">_utils</span><span class="o">.</span><span class="n">is_set</span><span class="p">(</span><span class="n">override_deps_before</span><span class="p">):</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_override_deps</span> <span class="o">=</span> <span class="n">override_deps_before</span>
        <span class="k">if</span> <span class="n">_utils</span><span class="o">.</span><span class="n">is_set</span><span class="p">(</span><span class="n">override_model_before</span><span class="p">):</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_override_model</span> <span class="o">=</span> <span class="n">override_model_before</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.agent.Agent.system_prompt" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">system_prompt</span>


</h4>
          <div class="doc-overloads">
<div class="language-python doc-signature highlight"><pre id="__code_32"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_32 > code"></button><code><span class="nf">system_prompt</span><span class="p">(</span>
    <span class="n">func</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Callable" href="https://docs.python.org/3/library/typing.html#typing.Callable">Callable</a></span><span class="p">[[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.RunContext" href="../tools/#pydantic_ai.tools.RunContext">RunContext</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span><span class="p">]],</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span><span class="p">],</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Callable" href="https://docs.python.org/3/library/typing.html#typing.Callable">Callable</a></span><span class="p">[[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.RunContext" href="../tools/#pydantic_ai.tools.RunContext">RunContext</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span><span class="p">]],</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span><span class="p">]</span>
</code></pre></div><div class="language-python doc-signature highlight"><pre id="__code_33"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_33 > code"></button><code><span class="nf">system_prompt</span><span class="p">(</span>
    <span class="n">func</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Callable" href="https://docs.python.org/3/library/typing.html#typing.Callable">Callable</a></span><span class="p">[</span>
        <span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.RunContext" href="../tools/#pydantic_ai.tools.RunContext">RunContext</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span><span class="p">]],</span> <span class="n"><a class="autorefs autorefs-external" title="collections.abc.Awaitable" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Awaitable">Awaitable</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span><span class="p">]</span>
    <span class="p">],</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Callable" href="https://docs.python.org/3/library/typing.html#typing.Callable">Callable</a></span><span class="p">[[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.RunContext" href="../tools/#pydantic_ai.tools.RunContext">RunContext</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span><span class="p">]],</span> <span class="n"><a class="autorefs autorefs-external" title="collections.abc.Awaitable" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Awaitable">Awaitable</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span><span class="p">]]</span>
</code></pre></div><div class="language-python doc-signature highlight"><pre id="__code_34"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_34 > code"></button><code><span class="nf">system_prompt</span><span class="p">(</span><span class="n">func</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Callable" href="https://docs.python.org/3/library/typing.html#typing.Callable">Callable</a></span><span class="p">[[],</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Callable" href="https://docs.python.org/3/library/typing.html#typing.Callable">Callable</a></span><span class="p">[[],</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span><span class="p">]</span>
</code></pre></div><div class="language-python doc-signature highlight"><pre id="__code_35"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_35 > code"></button><code><span class="nf">system_prompt</span><span class="p">(</span>
    <span class="n">func</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Callable" href="https://docs.python.org/3/library/typing.html#typing.Callable">Callable</a></span><span class="p">[[],</span> <span class="n"><a class="autorefs autorefs-external" title="collections.abc.Awaitable" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Awaitable">Awaitable</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span><span class="p">]],</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Callable" href="https://docs.python.org/3/library/typing.html#typing.Callable">Callable</a></span><span class="p">[[],</span> <span class="n"><a class="autorefs autorefs-external" title="collections.abc.Awaitable" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Awaitable">Awaitable</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span><span class="p">]]</span>
</code></pre></div><div class="language-python doc-signature highlight"><pre id="__code_36"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_36 > code"></button><code><span class="nf">system_prompt</span><span class="p">(</span><span class="o">*</span><span class="p">,</span> <span class="n">dynamic</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Callable" href="https://docs.python.org/3/library/typing.html#typing.Callable">Callable</a></span><span class="p">[</span>
    <span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai._system_prompt.SystemPromptFunc" href="../tools/#pydantic_ai.tools.SystemPromptFunc">SystemPromptFunc</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span><span class="p">]],</span>
    <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai._system_prompt.SystemPromptFunc" href="../tools/#pydantic_ai.tools.SystemPromptFunc">SystemPromptFunc</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span><span class="p">],</span>
<span class="p">]</span>
</code></pre></div>          </div>
<div class="language-python doc-signature highlight"><pre id="__code_37"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_37 > code"></button><code><span class="nf">system_prompt</span><span class="p">(</span>
    <span class="n">func</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai._system_prompt.SystemPromptFunc" href="../tools/#pydantic_ai.tools.SystemPromptFunc">SystemPromptFunc</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">/</span><span class="p">,</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">dynamic</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="p">(</span>
    <span class="n"><a class="autorefs autorefs-external" title="typing.Callable" href="https://docs.python.org/3/library/typing.html#typing.Callable">Callable</a></span><span class="p">[</span>
        <span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai._system_prompt.SystemPromptFunc" href="../tools/#pydantic_ai.tools.SystemPromptFunc">SystemPromptFunc</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span><span class="p">]],</span>
        <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai._system_prompt.SystemPromptFunc" href="../tools/#pydantic_ai.tools.SystemPromptFunc">SystemPromptFunc</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span><span class="p">],</span>
    <span class="p">]</span>
    <span class="o">|</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai._system_prompt.SystemPromptFunc" href="../tools/#pydantic_ai.tools.SystemPromptFunc">SystemPromptFunc</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span><span class="p">]</span>
<span class="p">)</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Decorator to register a system prompt function.</p>
<p>Optionally takes <a class="autorefs autorefs-internal" href="../tools/#pydantic_ai.tools.RunContext"><code>RunContext</code></a> as its only argument.
Can decorate a sync or async functions.</p>
<p>The decorator can be used either bare (<code>agent.system_prompt</code>) or as a function call
(<code>agent.system_prompt(...)</code>), see the examples below.</p>
<p>Overloads for every possible signature of <code>system_prompt</code> are included so the decorator doesn't obscure
the type of the function, see <code>tests/typed_agent.py</code> for tests.</p>


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
                <code>func</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_ai._system_prompt.SystemPromptFunc" href="../tools/#pydantic_ai.tools.SystemPromptFunc">SystemPromptFunc</a>[<a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a>] | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The function to decorate</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>dynamic</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>If True, the system prompt will be reevaluated even when <code>messages_history</code> is provided,
see <a class="autorefs autorefs-internal" href="../messages/#pydantic_ai.messages.SystemPromptPart.dynamic_ref"><code>SystemPromptPart.dynamic_ref</code></a></p>
              </div>
            </td>
            <td>
                  <code>False</code>
            </td>
          </tr>
      </tbody>
    </table></div></div>
        <p>Example:
</p><div class="language-python highlight"><pre id="__code_38"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_38 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span><span class="p">,</span> <span class="n">RunContext</span>

<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="s1">'test'</span><span class="p">,</span> <span class="n">deps_type</span><span class="o">=</span><span class="nb">str</span><span class="p">)</span>

<span class="nd">@agent</span><span class="o">.</span><span class="n">system_prompt</span>
<span class="k">def</span><span class="w"> </span><span class="nf">simple_system_prompt</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
    <span class="k">return</span> <span class="s1">'foobar'</span>

<span class="nd">@agent</span><span class="o">.</span><span class="n">system_prompt</span><span class="p">(</span><span class="n">dynamic</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">async_system_prompt</span><span class="p">(</span><span class="n">ctx</span><span class="p">:</span> <span class="n">RunContext</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
    <span class="k">return</span> <span class="sa">f</span><span class="s1">'</span><span class="si">{</span><span class="n">ctx</span><span class="o">.</span><span class="n">deps</span><span class="si">}</span><span class="s1"> is the best'</span>
</code></pre></div><p></p>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/agent.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">814</span>
<span class="normal">815</span>
<span class="normal">816</span>
<span class="normal">817</span>
<span class="normal">818</span>
<span class="normal">819</span>
<span class="normal">820</span>
<span class="normal">821</span>
<span class="normal">822</span>
<span class="normal">823</span>
<span class="normal">824</span>
<span class="normal">825</span>
<span class="normal">826</span>
<span class="normal">827</span>
<span class="normal">828</span>
<span class="normal">829</span>
<span class="normal">830</span>
<span class="normal">831</span>
<span class="normal">832</span>
<span class="normal">833</span>
<span class="normal">834</span>
<span class="normal">835</span>
<span class="normal">836</span>
<span class="normal">837</span>
<span class="normal">838</span>
<span class="normal">839</span>
<span class="normal">840</span>
<span class="normal">841</span>
<span class="normal">842</span>
<span class="normal">843</span>
<span class="normal">844</span>
<span class="normal">845</span>
<span class="normal">846</span>
<span class="normal">847</span>
<span class="normal">848</span>
<span class="normal">849</span>
<span class="normal">850</span>
<span class="normal">851</span>
<span class="normal">852</span>
<span class="normal">853</span>
<span class="normal">854</span>
<span class="normal">855</span>
<span class="normal">856</span>
<span class="normal">857</span>
<span class="normal">858</span>
<span class="normal">859</span>
<span class="normal">860</span>
<span class="normal">861</span>
<span class="normal">862</span>
<span class="normal">863</span>
<span class="normal">864</span>
<span class="normal">865</span>
<span class="normal">866</span>
<span class="normal">867</span>
<span class="normal">868</span>
<span class="normal">869</span>
<span class="normal">870</span></pre></div></td><td class="code"><div><pre id="__code_39"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_39 > code"></button><code tabindex="0"><span class="k">def</span><span class="w"> </span><span class="nf">system_prompt</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">func</span><span class="p">:</span> <span class="n">_system_prompt</span><span class="o">.</span><span class="n">SystemPromptFunc</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">/</span><span class="p">,</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">dynamic</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="p">(</span>
    <span class="n">Callable</span><span class="p">[[</span><span class="n">_system_prompt</span><span class="o">.</span><span class="n">SystemPromptFunc</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">]],</span> <span class="n">_system_prompt</span><span class="o">.</span><span class="n">SystemPromptFunc</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">]]</span>
    <span class="o">|</span> <span class="n">_system_prompt</span><span class="o">.</span><span class="n">SystemPromptFunc</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">]</span>
<span class="p">):</span>
<span class="w">    </span><span class="sd">"""Decorator to register a system prompt function.</span>

<span class="sd">    Optionally takes [`RunContext`][pydantic_ai.tools.RunContext] as its only argument.</span>
<span class="sd">    Can decorate a sync or async functions.</span>

<span class="sd">    The decorator can be used either bare (`agent.system_prompt`) or as a function call</span>
<span class="sd">    (`agent.system_prompt(...)`), see the examples below.</span>

<span class="sd">    Overloads for every possible signature of `system_prompt` are included so the decorator doesn't obscure</span>
<span class="sd">    the type of the function, see `tests/typed_agent.py` for tests.</span>

<span class="sd">    Args:</span>
<span class="sd">        func: The function to decorate</span>
<span class="sd">        dynamic: If True, the system prompt will be reevaluated even when `messages_history` is provided,</span>
<span class="sd">            see [`SystemPromptPart.dynamic_ref`][pydantic_ai.messages.SystemPromptPart.dynamic_ref]</span>

<span class="sd">    Example:</span>
<span class="sd">    ```python</span>
<span class="sd">    from pydantic_ai import Agent, RunContext</span>

<span class="sd">    agent = Agent('test', deps_type=str)</span>

<span class="sd">    @agent.system_prompt</span>
<span class="sd">    def simple_system_prompt() -&gt; str:</span>
<span class="sd">        return 'foobar'</span>

<span class="sd">    @agent.system_prompt(dynamic=True)</span>
<span class="sd">    async def async_system_prompt(ctx: RunContext[str]) -&gt; str:</span>
<span class="sd">        return f'{ctx.deps} is the best'</span>
<span class="sd">    ```</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="n">func</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>

        <span class="k">def</span><span class="w"> </span><span class="nf">decorator</span><span class="p">(</span>
            <span class="n">func_</span><span class="p">:</span> <span class="n">_system_prompt</span><span class="o">.</span><span class="n">SystemPromptFunc</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">],</span>
        <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">_system_prompt</span><span class="o">.</span><span class="n">SystemPromptFunc</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">]:</span>
            <span class="n">runner</span> <span class="o">=</span> <span class="n">_system_prompt</span><span class="o">.</span><span class="n">SystemPromptRunner</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">](</span><span class="n">func_</span><span class="p">,</span> <span class="n">dynamic</span><span class="o">=</span><span class="n">dynamic</span><span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_system_prompt_functions</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">runner</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">dynamic</span><span class="p">:</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_system_prompt_dynamic_functions</span><span class="p">[</span><span class="n">func_</span><span class="o">.</span><span class="vm">__qualname__</span><span class="p">]</span> <span class="o">=</span> <span class="n">runner</span>
            <span class="k">return</span> <span class="n">func_</span>

        <span class="k">return</span> <span class="n">decorator</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">assert</span> <span class="ow">not</span> <span class="n">dynamic</span><span class="p">,</span> <span class="s2">"dynamic can't be True in this case"</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_system_prompt_functions</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">_system_prompt</span><span class="o">.</span><span class="n">SystemPromptRunner</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">](</span><span class="n">func</span><span class="p">,</span> <span class="n">dynamic</span><span class="o">=</span><span class="n">dynamic</span><span class="p">))</span>
        <span class="k">return</span> <span class="n">func</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.agent.Agent.result_validator" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">result_validator</span>


</h4>
          <div class="doc-overloads">
<div class="language-python doc-signature highlight"><pre id="__code_40"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_40 > code"></button><code><span class="nf">result_validator</span><span class="p">(</span>
    <span class="n">func</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Callable" href="https://docs.python.org/3/library/typing.html#typing.Callable">Callable</a></span><span class="p">[</span>
        <span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.RunContext" href="../tools/#pydantic_ai.tools.RunContext">RunContext</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span><span class="p">],</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.result.ResultDataT" href="../result/#pydantic_ai.result.ResultDataT">ResultDataT</a></span><span class="p">],</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.result.ResultDataT" href="../result/#pydantic_ai.result.ResultDataT">ResultDataT</a></span>
    <span class="p">],</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Callable" href="https://docs.python.org/3/library/typing.html#typing.Callable">Callable</a></span><span class="p">[</span>
    <span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.RunContext" href="../tools/#pydantic_ai.tools.RunContext">RunContext</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span><span class="p">],</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.result.ResultDataT" href="../result/#pydantic_ai.result.ResultDataT">ResultDataT</a></span><span class="p">],</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.result.ResultDataT" href="../result/#pydantic_ai.result.ResultDataT">ResultDataT</a></span>
<span class="p">]</span>
</code></pre></div><div class="language-python doc-signature highlight"><pre id="__code_41"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_41 > code"></button><code><span class="nf">result_validator</span><span class="p">(</span>
    <span class="n">func</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Callable" href="https://docs.python.org/3/library/typing.html#typing.Callable">Callable</a></span><span class="p">[</span>
        <span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.RunContext" href="../tools/#pydantic_ai.tools.RunContext">RunContext</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span><span class="p">],</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.result.ResultDataT" href="../result/#pydantic_ai.result.ResultDataT">ResultDataT</a></span><span class="p">],</span>
        <span class="n"><a class="autorefs autorefs-external" title="collections.abc.Awaitable" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Awaitable">Awaitable</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.result.ResultDataT" href="../result/#pydantic_ai.result.ResultDataT">ResultDataT</a></span><span class="p">],</span>
    <span class="p">],</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Callable" href="https://docs.python.org/3/library/typing.html#typing.Callable">Callable</a></span><span class="p">[</span>
    <span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.RunContext" href="../tools/#pydantic_ai.tools.RunContext">RunContext</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span><span class="p">],</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.result.ResultDataT" href="../result/#pydantic_ai.result.ResultDataT">ResultDataT</a></span><span class="p">],</span>
    <span class="n"><a class="autorefs autorefs-external" title="collections.abc.Awaitable" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Awaitable">Awaitable</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.result.ResultDataT" href="../result/#pydantic_ai.result.ResultDataT">ResultDataT</a></span><span class="p">],</span>
<span class="p">]</span>
</code></pre></div><div class="language-python doc-signature highlight"><pre id="__code_42"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_42 > code"></button><code><span class="nf">result_validator</span><span class="p">(</span>
    <span class="n">func</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Callable" href="https://docs.python.org/3/library/typing.html#typing.Callable">Callable</a></span><span class="p">[[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.result.ResultDataT" href="../result/#pydantic_ai.result.ResultDataT">ResultDataT</a></span><span class="p">],</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.result.ResultDataT" href="../result/#pydantic_ai.result.ResultDataT">ResultDataT</a></span><span class="p">],</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Callable" href="https://docs.python.org/3/library/typing.html#typing.Callable">Callable</a></span><span class="p">[[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.result.ResultDataT" href="../result/#pydantic_ai.result.ResultDataT">ResultDataT</a></span><span class="p">],</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.result.ResultDataT" href="../result/#pydantic_ai.result.ResultDataT">ResultDataT</a></span><span class="p">]</span>
</code></pre></div><div class="language-python doc-signature highlight"><pre id="__code_43"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_43 > code"></button><code><span class="nf">result_validator</span><span class="p">(</span>
    <span class="n">func</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Callable" href="https://docs.python.org/3/library/typing.html#typing.Callable">Callable</a></span><span class="p">[[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.result.ResultDataT" href="../result/#pydantic_ai.result.ResultDataT">ResultDataT</a></span><span class="p">],</span> <span class="n"><a class="autorefs autorefs-external" title="collections.abc.Awaitable" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Awaitable">Awaitable</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.result.ResultDataT" href="../result/#pydantic_ai.result.ResultDataT">ResultDataT</a></span><span class="p">]],</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Callable" href="https://docs.python.org/3/library/typing.html#typing.Callable">Callable</a></span><span class="p">[[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.result.ResultDataT" href="../result/#pydantic_ai.result.ResultDataT">ResultDataT</a></span><span class="p">],</span> <span class="n"><a class="autorefs autorefs-external" title="collections.abc.Awaitable" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Awaitable">Awaitable</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.result.ResultDataT" href="../result/#pydantic_ai.result.ResultDataT">ResultDataT</a></span><span class="p">]]</span>
</code></pre></div>          </div>
<div class="language-python doc-signature highlight"><pre id="__code_44"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_44 > code"></button><code><span class="nf">result_validator</span><span class="p">(</span>
    <span class="n">func</span><span class="p">:</span> <span class="n"><span title="pydantic_ai._result.ResultValidatorFunc">ResultValidatorFunc</span></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.result.ResultDataT" href="../result/#pydantic_ai.result.ResultDataT">ResultDataT</a></span><span class="p">],</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><span title="pydantic_ai._result.ResultValidatorFunc">ResultValidatorFunc</span></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.result.ResultDataT" href="../result/#pydantic_ai.result.ResultDataT">ResultDataT</a></span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Decorator to register a result validator function.</p>
<p>Optionally takes <a class="autorefs autorefs-internal" href="../tools/#pydantic_ai.tools.RunContext"><code>RunContext</code></a> as its first argument.
Can decorate a sync or async functions.</p>
<p>Overloads for every possible signature of <code>result_validator</code> are included so the decorator doesn't obscure
the type of the function, see <code>tests/typed_agent.py</code> for tests.</p>
<p>Example:
</p><div class="language-python highlight"><pre id="__code_45"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_45 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span><span class="p">,</span> <span class="n">ModelRetry</span><span class="p">,</span> <span class="n">RunContext</span>

<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="s1">'test'</span><span class="p">,</span> <span class="n">deps_type</span><span class="o">=</span><span class="nb">str</span><span class="p">)</span>

<span class="nd">@agent</span><span class="o">.</span><span class="n">result_validator</span>
<span class="k">def</span><span class="w"> </span><span class="nf">result_validator_simple</span><span class="p">(</span><span class="n">data</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
    <span class="k">if</span> <span class="s1">'wrong'</span> <span class="ow">in</span> <span class="n">data</span><span class="p">:</span>
        <span class="k">raise</span> <span class="n">ModelRetry</span><span class="p">(</span><span class="s1">'wrong response'</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">data</span>

<span class="nd">@agent</span><span class="o">.</span><span class="n">result_validator</span>
<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">result_validator_deps</span><span class="p">(</span><span class="n">ctx</span><span class="p">:</span> <span class="n">RunContext</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">data</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
    <span class="k">if</span> <span class="n">ctx</span><span class="o">.</span><span class="n">deps</span> <span class="ow">in</span> <span class="n">data</span><span class="p">:</span>
        <span class="k">raise</span> <span class="n">ModelRetry</span><span class="p">(</span><span class="s1">'wrong response'</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">data</span>

<span class="n">result</span> <span class="o">=</span> <span class="n">agent</span><span class="o">.</span><span class="n">run_sync</span><span class="p">(</span><span class="s1">'foobar'</span><span class="p">,</span> <span class="n">deps</span><span class="o">=</span><span class="s1">'spam'</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">result</span><span class="o">.</span><span class="n">data</span><span class="p">)</span>
<span class="c1">#&gt; success (no tool calls)</span>
</code></pre></div><p></p>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/agent.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">892</span>
<span class="normal">893</span>
<span class="normal">894</span>
<span class="normal">895</span>
<span class="normal">896</span>
<span class="normal">897</span>
<span class="normal">898</span>
<span class="normal">899</span>
<span class="normal">900</span>
<span class="normal">901</span>
<span class="normal">902</span>
<span class="normal">903</span>
<span class="normal">904</span>
<span class="normal">905</span>
<span class="normal">906</span>
<span class="normal">907</span>
<span class="normal">908</span>
<span class="normal">909</span>
<span class="normal">910</span>
<span class="normal">911</span>
<span class="normal">912</span>
<span class="normal">913</span>
<span class="normal">914</span>
<span class="normal">915</span>
<span class="normal">916</span>
<span class="normal">917</span>
<span class="normal">918</span>
<span class="normal">919</span>
<span class="normal">920</span>
<span class="normal">921</span>
<span class="normal">922</span>
<span class="normal">923</span>
<span class="normal">924</span>
<span class="normal">925</span>
<span class="normal">926</span>
<span class="normal">927</span></pre></div></td><td class="code"><div><pre id="__code_46"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_46 > code"></button><code tabindex="0"><span class="k">def</span><span class="w"> </span><span class="nf">result_validator</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">func</span><span class="p">:</span> <span class="n">_result</span><span class="o">.</span><span class="n">ResultValidatorFunc</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">,</span> <span class="n">ResultDataT</span><span class="p">],</span> <span class="o">/</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">_result</span><span class="o">.</span><span class="n">ResultValidatorFunc</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">,</span> <span class="n">ResultDataT</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Decorator to register a result validator function.</span>

<span class="sd">    Optionally takes [`RunContext`][pydantic_ai.tools.RunContext] as its first argument.</span>
<span class="sd">    Can decorate a sync or async functions.</span>

<span class="sd">    Overloads for every possible signature of `result_validator` are included so the decorator doesn't obscure</span>
<span class="sd">    the type of the function, see `tests/typed_agent.py` for tests.</span>

<span class="sd">    Example:</span>
<span class="sd">    ```python</span>
<span class="sd">    from pydantic_ai import Agent, ModelRetry, RunContext</span>

<span class="sd">    agent = Agent('test', deps_type=str)</span>

<span class="sd">    @agent.result_validator</span>
<span class="sd">    def result_validator_simple(data: str) -&gt; str:</span>
<span class="sd">        if 'wrong' in data:</span>
<span class="sd">            raise ModelRetry('wrong response')</span>
<span class="sd">        return data</span>

<span class="sd">    @agent.result_validator</span>
<span class="sd">    async def result_validator_deps(ctx: RunContext[str], data: str) -&gt; str:</span>
<span class="sd">        if ctx.deps in data:</span>
<span class="sd">            raise ModelRetry('wrong response')</span>
<span class="sd">        return data</span>

<span class="sd">    result = agent.run_sync('foobar', deps='spam')</span>
<span class="sd">    print(result.data)</span>
<span class="sd">    #&gt; success (no tool calls)</span>
<span class="sd">    ```</span>
<span class="sd">    """</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_result_validators</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">_result</span><span class="o">.</span><span class="n">ResultValidator</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">,</span> <span class="n">Any</span><span class="p">](</span><span class="n">func</span><span class="p">))</span>
    <span class="k">return</span> <span class="n">func</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.agent.Agent.tool" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">tool</span>


</h4>
          <div class="doc-overloads">
<div class="language-python doc-signature highlight"><pre id="__code_47"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_47 > code"></button><code><span class="nf">tool</span><span class="p">(</span>
    <span class="n">func</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.ToolFuncContext" href="../tools/#pydantic_ai.tools.ToolFuncContext">ToolFuncContext</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.ToolParams" href="../tools/#pydantic_ai.tools.ToolParams">ToolParams</a></span><span class="p">],</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.ToolFuncContext" href="../tools/#pydantic_ai.tools.ToolFuncContext">ToolFuncContext</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.ToolParams" href="../tools/#pydantic_ai.tools.ToolParams">ToolParams</a></span><span class="p">]</span>
</code></pre></div><div class="language-python doc-signature highlight"><pre id="__code_48"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_48 > code"></button><code><span class="nf">tool</span><span class="p">(</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">retries</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#int">int</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">prepare</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.ToolPrepareFunc" href="../tools/#pydantic_ai.tools.ToolPrepareFunc">ToolPrepareFunc</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">docstring_format</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.DocstringFormat" href="../tools/#pydantic_ai.tools.DocstringFormat">DocstringFormat</a></span> <span class="o">=</span> <span class="s2">"auto"</span><span class="p">,</span>
    <span class="n">require_parameter_descriptions</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">schema_generator</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type">type</a></span><span class="p">[</span>
        <span class="n"><a class="autorefs autorefs-external" title="pydantic.json_schema.GenerateJsonSchema" href="https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema">GenerateJsonSchema</a></span>
    <span class="p">]</span> <span class="o">=</span> <span class="n"><span title="pydantic_ai.tools.GenerateToolJsonSchema">GenerateToolJsonSchema</span></span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Callable" href="https://docs.python.org/3/library/typing.html#typing.Callable">Callable</a></span><span class="p">[</span>
    <span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.ToolFuncContext" href="../tools/#pydantic_ai.tools.ToolFuncContext">ToolFuncContext</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.ToolParams" href="../tools/#pydantic_ai.tools.ToolParams">ToolParams</a></span><span class="p">]],</span>
    <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.ToolFuncContext" href="../tools/#pydantic_ai.tools.ToolFuncContext">ToolFuncContext</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.ToolParams" href="../tools/#pydantic_ai.tools.ToolParams">ToolParams</a></span><span class="p">],</span>
<span class="p">]</span>
</code></pre></div>          </div>
<div class="language-python doc-signature highlight"><pre id="__code_49"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_49 > code"></button><code><span class="nf">tool</span><span class="p">(</span>
    <span class="n">func</span><span class="p">:</span> <span class="p">(</span>
        <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.ToolFuncContext" href="../tools/#pydantic_ai.tools.ToolFuncContext">ToolFuncContext</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.ToolParams" href="../tools/#pydantic_ai.tools.ToolParams">ToolParams</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">/</span><span class="p">,</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">retries</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#int">int</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">prepare</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.ToolPrepareFunc" href="../tools/#pydantic_ai.tools.ToolPrepareFunc">ToolPrepareFunc</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">docstring_format</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.DocstringFormat" href="../tools/#pydantic_ai.tools.DocstringFormat">DocstringFormat</a></span> <span class="o">=</span> <span class="s2">"auto"</span><span class="p">,</span>
    <span class="n">require_parameter_descriptions</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">schema_generator</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type">type</a></span><span class="p">[</span>
        <span class="n"><a class="autorefs autorefs-external" title="pydantic.json_schema.GenerateJsonSchema" href="https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema">GenerateJsonSchema</a></span>
    <span class="p">]</span> <span class="o">=</span> <span class="n"><span title="pydantic_ai.tools.GenerateToolJsonSchema">GenerateToolJsonSchema</span></span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Decorator to register a tool function which takes <a class="autorefs autorefs-internal" href="../tools/#pydantic_ai.tools.RunContext"><code>RunContext</code></a> as its first argument.</p>
<p>Can decorate a sync or async functions.</p>
<p>The docstring is inspected to extract both the tool description and description of each parameter,
<a href="../../tools/#function-tools-and-schema">learn more</a>.</p>
<p>We can't add overloads for every possible signature of tool, since the return type is a recursive union
so the signature of functions decorated with <code>@agent.tool</code> is obscured.</p>
<p>Example:
</p><div class="language-python highlight"><pre id="__code_50"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_50 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span><span class="p">,</span> <span class="n">RunContext</span>

<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="s1">'test'</span><span class="p">,</span> <span class="n">deps_type</span><span class="o">=</span><span class="nb">int</span><span class="p">)</span>

<span class="nd">@agent</span><span class="o">.</span><span class="n">tool</span>
<span class="k">def</span><span class="w"> </span><span class="nf">foobar</span><span class="p">(</span><span class="n">ctx</span><span class="p">:</span> <span class="n">RunContext</span><span class="p">[</span><span class="nb">int</span><span class="p">],</span> <span class="n">x</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">int</span><span class="p">:</span>
    <span class="k">return</span> <span class="n">ctx</span><span class="o">.</span><span class="n">deps</span> <span class="o">+</span> <span class="n">x</span>

<span class="nd">@agent</span><span class="o">.</span><span class="n">tool</span><span class="p">(</span><span class="n">retries</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">spam</span><span class="p">(</span><span class="n">ctx</span><span class="p">:</span> <span class="n">RunContext</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">y</span><span class="p">:</span> <span class="nb">float</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">float</span><span class="p">:</span>
    <span class="k">return</span> <span class="n">ctx</span><span class="o">.</span><span class="n">deps</span> <span class="o">+</span> <span class="n">y</span>

<span class="n">result</span> <span class="o">=</span> <span class="n">agent</span><span class="o">.</span><span class="n">run_sync</span><span class="p">(</span><span class="s1">'foobar'</span><span class="p">,</span> <span class="n">deps</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">result</span><span class="o">.</span><span class="n">data</span><span class="p">)</span>
<span class="c1">#&gt; {"foobar":1,"spam":1.0}</span>
</code></pre></div><p></p>


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
                <code>func</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_ai.tools.ToolFuncContext" href="../tools/#pydantic_ai.tools.ToolFuncContext">ToolFuncContext</a>[<a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a>, <a class="autorefs autorefs-internal" title="pydantic_ai.tools.ToolParams" href="../tools/#pydantic_ai.tools.ToolParams">ToolParams</a>] | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The tool function to register.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>name</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The name of the tool, defaults to the function name.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>retries</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#int">int</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The number of retries to allow for this tool, defaults to the agent's default retries,
which defaults to 1.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>prepare</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_ai.tools.ToolPrepareFunc" href="../tools/#pydantic_ai.tools.ToolPrepareFunc">ToolPrepareFunc</a>[<a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a>] | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>custom method to prepare the tool definition for each step, return <code>None</code> to omit this
tool from a given step. This is useful if you want to customise a tool at call time,
or omit it completely from a step. See <a class="autorefs autorefs-internal" href="../tools/#pydantic_ai.tools.ToolPrepareFunc"><code>ToolPrepareFunc</code></a>.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>docstring_format</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_ai.tools.DocstringFormat" href="../tools/#pydantic_ai.tools.DocstringFormat">DocstringFormat</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The format of the docstring, see <a class="autorefs autorefs-internal" href="../tools/#pydantic_ai.tools.DocstringFormat"><code>DocstringFormat</code></a>.
Defaults to <code>'auto'</code>, such that the format is inferred from the structure of the docstring.</p>
              </div>
            </td>
            <td>
                  <code>'auto'</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>require_parameter_descriptions</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>If True, raise an error if a parameter description is missing. Defaults to False.</p>
              </div>
            </td>
            <td>
                  <code>False</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>schema_generator</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type">type</a>[<a class="autorefs autorefs-external" title="pydantic.json_schema.GenerateJsonSchema" href="https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema">GenerateJsonSchema</a>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The JSON schema generator class to use for this tool. Defaults to <code>GenerateToolJsonSchema</code>.</p>
              </div>
            </td>
            <td>
                  <code><span title="pydantic_ai.tools.GenerateToolJsonSchema">GenerateToolJsonSchema</span></code>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/agent.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 945</span>
<span class="normal"> 946</span>
<span class="normal"> 947</span>
<span class="normal"> 948</span>
<span class="normal"> 949</span>
<span class="normal"> 950</span>
<span class="normal"> 951</span>
<span class="normal"> 952</span>
<span class="normal"> 953</span>
<span class="normal"> 954</span>
<span class="normal"> 955</span>
<span class="normal"> 956</span>
<span class="normal"> 957</span>
<span class="normal"> 958</span>
<span class="normal"> 959</span>
<span class="normal"> 960</span>
<span class="normal"> 961</span>
<span class="normal"> 962</span>
<span class="normal"> 963</span>
<span class="normal"> 964</span>
<span class="normal"> 965</span>
<span class="normal"> 966</span>
<span class="normal"> 967</span>
<span class="normal"> 968</span>
<span class="normal"> 969</span>
<span class="normal"> 970</span>
<span class="normal"> 971</span>
<span class="normal"> 972</span>
<span class="normal"> 973</span>
<span class="normal"> 974</span>
<span class="normal"> 975</span>
<span class="normal"> 976</span>
<span class="normal"> 977</span>
<span class="normal"> 978</span>
<span class="normal"> 979</span>
<span class="normal"> 980</span>
<span class="normal"> 981</span>
<span class="normal"> 982</span>
<span class="normal"> 983</span>
<span class="normal"> 984</span>
<span class="normal"> 985</span>
<span class="normal"> 986</span>
<span class="normal"> 987</span>
<span class="normal"> 988</span>
<span class="normal"> 989</span>
<span class="normal"> 990</span>
<span class="normal"> 991</span>
<span class="normal"> 992</span>
<span class="normal"> 993</span>
<span class="normal"> 994</span>
<span class="normal"> 995</span>
<span class="normal"> 996</span>
<span class="normal"> 997</span>
<span class="normal"> 998</span>
<span class="normal"> 999</span>
<span class="normal">1000</span>
<span class="normal">1001</span>
<span class="normal">1002</span>
<span class="normal">1003</span>
<span class="normal">1004</span>
<span class="normal">1005</span>
<span class="normal">1006</span>
<span class="normal">1007</span>
<span class="normal">1008</span>
<span class="normal">1009</span>
<span class="normal">1010</span>
<span class="normal">1011</span>
<span class="normal">1012</span>
<span class="normal">1013</span>
<span class="normal">1014</span>
<span class="normal">1015</span>
<span class="normal">1016</span>
<span class="normal">1017</span>
<span class="normal">1018</span>
<span class="normal">1019</span>
<span class="normal">1020</span>
<span class="normal">1021</span>
<span class="normal">1022</span>
<span class="normal">1023</span></pre></div></td><td class="code"><div><pre id="__code_51"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_51 > code"></button><code tabindex="0"><span class="k">def</span><span class="w"> </span><span class="nf">tool</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">func</span><span class="p">:</span> <span class="n">ToolFuncContext</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">,</span> <span class="n">ToolParams</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">/</span><span class="p">,</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">retries</span><span class="p">:</span> <span class="nb">int</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">prepare</span><span class="p">:</span> <span class="n">ToolPrepareFunc</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">docstring_format</span><span class="p">:</span> <span class="n">DocstringFormat</span> <span class="o">=</span> <span class="s1">'auto'</span><span class="p">,</span>
    <span class="n">require_parameter_descriptions</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">schema_generator</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n">GenerateJsonSchema</span><span class="p">]</span> <span class="o">=</span> <span class="n">GenerateToolJsonSchema</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Decorator to register a tool function which takes [`RunContext`][pydantic_ai.tools.RunContext] as its first argument.</span>

<span class="sd">    Can decorate a sync or async functions.</span>

<span class="sd">    The docstring is inspected to extract both the tool description and description of each parameter,</span>
<span class="sd">    [learn more](../tools.md#function-tools-and-schema).</span>

<span class="sd">    We can't add overloads for every possible signature of tool, since the return type is a recursive union</span>
<span class="sd">    so the signature of functions decorated with `@agent.tool` is obscured.</span>

<span class="sd">    Example:</span>
<span class="sd">    ```python</span>
<span class="sd">    from pydantic_ai import Agent, RunContext</span>

<span class="sd">    agent = Agent('test', deps_type=int)</span>

<span class="sd">    @agent.tool</span>
<span class="sd">    def foobar(ctx: RunContext[int], x: int) -&gt; int:</span>
<span class="sd">        return ctx.deps + x</span>

<span class="sd">    @agent.tool(retries=2)</span>
<span class="sd">    async def spam(ctx: RunContext[str], y: float) -&gt; float:</span>
<span class="sd">        return ctx.deps + y</span>

<span class="sd">    result = agent.run_sync('foobar', deps=1)</span>
<span class="sd">    print(result.data)</span>
<span class="sd">    #&gt; {"foobar":1,"spam":1.0}</span>
<span class="sd">    ```</span>

<span class="sd">    Args:</span>
<span class="sd">        func: The tool function to register.</span>
<span class="sd">        name: The name of the tool, defaults to the function name.</span>
<span class="sd">        retries: The number of retries to allow for this tool, defaults to the agent's default retries,</span>
<span class="sd">            which defaults to 1.</span>
<span class="sd">        prepare: custom method to prepare the tool definition for each step, return `None` to omit this</span>
<span class="sd">            tool from a given step. This is useful if you want to customise a tool at call time,</span>
<span class="sd">            or omit it completely from a step. See [`ToolPrepareFunc`][pydantic_ai.tools.ToolPrepareFunc].</span>
<span class="sd">        docstring_format: The format of the docstring, see [`DocstringFormat`][pydantic_ai.tools.DocstringFormat].</span>
<span class="sd">            Defaults to `'auto'`, such that the format is inferred from the structure of the docstring.</span>
<span class="sd">        require_parameter_descriptions: If True, raise an error if a parameter description is missing. Defaults to False.</span>
<span class="sd">        schema_generator: The JSON schema generator class to use for this tool. Defaults to `GenerateToolJsonSchema`.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="n">func</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>

        <span class="k">def</span><span class="w"> </span><span class="nf">tool_decorator</span><span class="p">(</span>
            <span class="n">func_</span><span class="p">:</span> <span class="n">ToolFuncContext</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">,</span> <span class="n">ToolParams</span><span class="p">],</span>
        <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ToolFuncContext</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">,</span> <span class="n">ToolParams</span><span class="p">]:</span>
            <span class="c1"># noinspection PyTypeChecker</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_register_function</span><span class="p">(</span>
                <span class="n">func_</span><span class="p">,</span>
                <span class="kc">True</span><span class="p">,</span>
                <span class="n">name</span><span class="p">,</span>
                <span class="n">retries</span><span class="p">,</span>
                <span class="n">prepare</span><span class="p">,</span>
                <span class="n">docstring_format</span><span class="p">,</span>
                <span class="n">require_parameter_descriptions</span><span class="p">,</span>
                <span class="n">schema_generator</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="k">return</span> <span class="n">func_</span>

        <span class="k">return</span> <span class="n">tool_decorator</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="c1"># noinspection PyTypeChecker</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_register_function</span><span class="p">(</span>
            <span class="n">func</span><span class="p">,</span> <span class="kc">True</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span> <span class="n">retries</span><span class="p">,</span> <span class="n">prepare</span><span class="p">,</span> <span class="n">docstring_format</span><span class="p">,</span> <span class="n">require_parameter_descriptions</span><span class="p">,</span> <span class="n">schema_generator</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="n">func</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.agent.Agent.tool_plain" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">tool_plain</span>


</h4>
          <div class="doc-overloads">
<div class="language-python doc-signature highlight"><pre id="__code_52"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_52 > code"></button><code><span class="nf">tool_plain</span><span class="p">(</span>
    <span class="n">func</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.ToolFuncPlain" href="../tools/#pydantic_ai.tools.ToolFuncPlain">ToolFuncPlain</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.ToolParams" href="../tools/#pydantic_ai.tools.ToolParams">ToolParams</a></span><span class="p">],</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.ToolFuncPlain" href="../tools/#pydantic_ai.tools.ToolFuncPlain">ToolFuncPlain</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.ToolParams" href="../tools/#pydantic_ai.tools.ToolParams">ToolParams</a></span><span class="p">]</span>
</code></pre></div><div class="language-python doc-signature highlight"><pre id="__code_53"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_53 > code"></button><code><span class="nf">tool_plain</span><span class="p">(</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">retries</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#int">int</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">prepare</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.ToolPrepareFunc" href="../tools/#pydantic_ai.tools.ToolPrepareFunc">ToolPrepareFunc</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">docstring_format</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.DocstringFormat" href="../tools/#pydantic_ai.tools.DocstringFormat">DocstringFormat</a></span> <span class="o">=</span> <span class="s2">"auto"</span><span class="p">,</span>
    <span class="n">require_parameter_descriptions</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">schema_generator</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type">type</a></span><span class="p">[</span>
        <span class="n"><a class="autorefs autorefs-external" title="pydantic.json_schema.GenerateJsonSchema" href="https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema">GenerateJsonSchema</a></span>
    <span class="p">]</span> <span class="o">=</span> <span class="n"><span title="pydantic_ai.tools.GenerateToolJsonSchema">GenerateToolJsonSchema</span></span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Callable" href="https://docs.python.org/3/library/typing.html#typing.Callable">Callable</a></span><span class="p">[</span>
    <span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.ToolFuncPlain" href="../tools/#pydantic_ai.tools.ToolFuncPlain">ToolFuncPlain</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.ToolParams" href="../tools/#pydantic_ai.tools.ToolParams">ToolParams</a></span><span class="p">]],</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.ToolFuncPlain" href="../tools/#pydantic_ai.tools.ToolFuncPlain">ToolFuncPlain</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.ToolParams" href="../tools/#pydantic_ai.tools.ToolParams">ToolParams</a></span><span class="p">]</span>
<span class="p">]</span>
</code></pre></div>          </div>
<div class="language-python doc-signature highlight"><pre id="__code_54"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_54 > code"></button><code><span class="nf">tool_plain</span><span class="p">(</span>
    <span class="n">func</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.ToolFuncPlain" href="../tools/#pydantic_ai.tools.ToolFuncPlain">ToolFuncPlain</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.ToolParams" href="../tools/#pydantic_ai.tools.ToolParams">ToolParams</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">/</span><span class="p">,</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">retries</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#int">int</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">prepare</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.ToolPrepareFunc" href="../tools/#pydantic_ai.tools.ToolPrepareFunc">ToolPrepareFunc</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">docstring_format</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.DocstringFormat" href="../tools/#pydantic_ai.tools.DocstringFormat">DocstringFormat</a></span> <span class="o">=</span> <span class="s2">"auto"</span><span class="p">,</span>
    <span class="n">require_parameter_descriptions</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">schema_generator</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type">type</a></span><span class="p">[</span>
        <span class="n"><a class="autorefs autorefs-external" title="pydantic.json_schema.GenerateJsonSchema" href="https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema">GenerateJsonSchema</a></span>
    <span class="p">]</span> <span class="o">=</span> <span class="n"><span title="pydantic_ai.tools.GenerateToolJsonSchema">GenerateToolJsonSchema</span></span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Decorator to register a tool function which DOES NOT take <code>RunContext</code> as an argument.</p>
<p>Can decorate a sync or async functions.</p>
<p>The docstring is inspected to extract both the tool description and description of each parameter,
<a href="../../tools/#function-tools-and-schema">learn more</a>.</p>
<p>We can't add overloads for every possible signature of tool, since the return type is a recursive union
so the signature of functions decorated with <code>@agent.tool</code> is obscured.</p>
<p>Example:
</p><div class="language-python highlight"><pre id="__code_55"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_55 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span><span class="p">,</span> <span class="n">RunContext</span>

<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="s1">'test'</span><span class="p">)</span>

<span class="nd">@agent</span><span class="o">.</span><span class="n">tool</span>
<span class="k">def</span><span class="w"> </span><span class="nf">foobar</span><span class="p">(</span><span class="n">ctx</span><span class="p">:</span> <span class="n">RunContext</span><span class="p">[</span><span class="nb">int</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="nb">int</span><span class="p">:</span>
    <span class="k">return</span> <span class="mi">123</span>

<span class="nd">@agent</span><span class="o">.</span><span class="n">tool</span><span class="p">(</span><span class="n">retries</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">spam</span><span class="p">(</span><span class="n">ctx</span><span class="p">:</span> <span class="n">RunContext</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="nb">float</span><span class="p">:</span>
    <span class="k">return</span> <span class="mf">3.14</span>

<span class="n">result</span> <span class="o">=</span> <span class="n">agent</span><span class="o">.</span><span class="n">run_sync</span><span class="p">(</span><span class="s1">'foobar'</span><span class="p">,</span> <span class="n">deps</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">result</span><span class="o">.</span><span class="n">data</span><span class="p">)</span>
<span class="c1">#&gt; {"foobar":123,"spam":3.14}</span>
</code></pre></div><p></p>


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
                <code>func</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_ai.tools.ToolFuncPlain" href="../tools/#pydantic_ai.tools.ToolFuncPlain">ToolFuncPlain</a>[<a class="autorefs autorefs-internal" title="pydantic_ai.tools.ToolParams" href="../tools/#pydantic_ai.tools.ToolParams">ToolParams</a>] | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The tool function to register.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>name</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The name of the tool, defaults to the function name.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>retries</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#int">int</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The number of retries to allow for this tool, defaults to the agent's default retries,
which defaults to 1.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>prepare</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_ai.tools.ToolPrepareFunc" href="../tools/#pydantic_ai.tools.ToolPrepareFunc">ToolPrepareFunc</a>[<a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a>] | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>custom method to prepare the tool definition for each step, return <code>None</code> to omit this
tool from a given step. This is useful if you want to customise a tool at call time,
or omit it completely from a step. See <a class="autorefs autorefs-internal" href="../tools/#pydantic_ai.tools.ToolPrepareFunc"><code>ToolPrepareFunc</code></a>.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>docstring_format</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_ai.tools.DocstringFormat" href="../tools/#pydantic_ai.tools.DocstringFormat">DocstringFormat</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The format of the docstring, see <a class="autorefs autorefs-internal" href="../tools/#pydantic_ai.tools.DocstringFormat"><code>DocstringFormat</code></a>.
Defaults to <code>'auto'</code>, such that the format is inferred from the structure of the docstring.</p>
              </div>
            </td>
            <td>
                  <code>'auto'</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>require_parameter_descriptions</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>If True, raise an error if a parameter description is missing. Defaults to False.</p>
              </div>
            </td>
            <td>
                  <code>False</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>schema_generator</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type">type</a>[<a class="autorefs autorefs-external" title="pydantic.json_schema.GenerateJsonSchema" href="https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema">GenerateJsonSchema</a>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The JSON schema generator class to use for this tool. Defaults to <code>GenerateToolJsonSchema</code>.</p>
              </div>
            </td>
            <td>
                  <code><span title="pydantic_ai.tools.GenerateToolJsonSchema">GenerateToolJsonSchema</span></code>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/agent.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">1041</span>
<span class="normal">1042</span>
<span class="normal">1043</span>
<span class="normal">1044</span>
<span class="normal">1045</span>
<span class="normal">1046</span>
<span class="normal">1047</span>
<span class="normal">1048</span>
<span class="normal">1049</span>
<span class="normal">1050</span>
<span class="normal">1051</span>
<span class="normal">1052</span>
<span class="normal">1053</span>
<span class="normal">1054</span>
<span class="normal">1055</span>
<span class="normal">1056</span>
<span class="normal">1057</span>
<span class="normal">1058</span>
<span class="normal">1059</span>
<span class="normal">1060</span>
<span class="normal">1061</span>
<span class="normal">1062</span>
<span class="normal">1063</span>
<span class="normal">1064</span>
<span class="normal">1065</span>
<span class="normal">1066</span>
<span class="normal">1067</span>
<span class="normal">1068</span>
<span class="normal">1069</span>
<span class="normal">1070</span>
<span class="normal">1071</span>
<span class="normal">1072</span>
<span class="normal">1073</span>
<span class="normal">1074</span>
<span class="normal">1075</span>
<span class="normal">1076</span>
<span class="normal">1077</span>
<span class="normal">1078</span>
<span class="normal">1079</span>
<span class="normal">1080</span>
<span class="normal">1081</span>
<span class="normal">1082</span>
<span class="normal">1083</span>
<span class="normal">1084</span>
<span class="normal">1085</span>
<span class="normal">1086</span>
<span class="normal">1087</span>
<span class="normal">1088</span>
<span class="normal">1089</span>
<span class="normal">1090</span>
<span class="normal">1091</span>
<span class="normal">1092</span>
<span class="normal">1093</span>
<span class="normal">1094</span>
<span class="normal">1095</span>
<span class="normal">1096</span>
<span class="normal">1097</span>
<span class="normal">1098</span>
<span class="normal">1099</span>
<span class="normal">1100</span>
<span class="normal">1101</span>
<span class="normal">1102</span>
<span class="normal">1103</span>
<span class="normal">1104</span>
<span class="normal">1105</span>
<span class="normal">1106</span>
<span class="normal">1107</span>
<span class="normal">1108</span>
<span class="normal">1109</span>
<span class="normal">1110</span>
<span class="normal">1111</span>
<span class="normal">1112</span>
<span class="normal">1113</span>
<span class="normal">1114</span>
<span class="normal">1115</span>
<span class="normal">1116</span></pre></div></td><td class="code"><div><pre id="__code_56"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_56 > code"></button><code tabindex="0"><span class="k">def</span><span class="w"> </span><span class="nf">tool_plain</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">func</span><span class="p">:</span> <span class="n">ToolFuncPlain</span><span class="p">[</span><span class="n">ToolParams</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">/</span><span class="p">,</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">retries</span><span class="p">:</span> <span class="nb">int</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">prepare</span><span class="p">:</span> <span class="n">ToolPrepareFunc</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">docstring_format</span><span class="p">:</span> <span class="n">DocstringFormat</span> <span class="o">=</span> <span class="s1">'auto'</span><span class="p">,</span>
    <span class="n">require_parameter_descriptions</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">schema_generator</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n">GenerateJsonSchema</span><span class="p">]</span> <span class="o">=</span> <span class="n">GenerateToolJsonSchema</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Decorator to register a tool function which DOES NOT take `RunContext` as an argument.</span>

<span class="sd">    Can decorate a sync or async functions.</span>

<span class="sd">    The docstring is inspected to extract both the tool description and description of each parameter,</span>
<span class="sd">    [learn more](../tools.md#function-tools-and-schema).</span>

<span class="sd">    We can't add overloads for every possible signature of tool, since the return type is a recursive union</span>
<span class="sd">    so the signature of functions decorated with `@agent.tool` is obscured.</span>

<span class="sd">    Example:</span>
<span class="sd">    ```python</span>
<span class="sd">    from pydantic_ai import Agent, RunContext</span>

<span class="sd">    agent = Agent('test')</span>

<span class="sd">    @agent.tool</span>
<span class="sd">    def foobar(ctx: RunContext[int]) -&gt; int:</span>
<span class="sd">        return 123</span>

<span class="sd">    @agent.tool(retries=2)</span>
<span class="sd">    async def spam(ctx: RunContext[str]) -&gt; float:</span>
<span class="sd">        return 3.14</span>

<span class="sd">    result = agent.run_sync('foobar', deps=1)</span>
<span class="sd">    print(result.data)</span>
<span class="sd">    #&gt; {"foobar":123,"spam":3.14}</span>
<span class="sd">    ```</span>

<span class="sd">    Args:</span>
<span class="sd">        func: The tool function to register.</span>
<span class="sd">        name: The name of the tool, defaults to the function name.</span>
<span class="sd">        retries: The number of retries to allow for this tool, defaults to the agent's default retries,</span>
<span class="sd">            which defaults to 1.</span>
<span class="sd">        prepare: custom method to prepare the tool definition for each step, return `None` to omit this</span>
<span class="sd">            tool from a given step. This is useful if you want to customise a tool at call time,</span>
<span class="sd">            or omit it completely from a step. See [`ToolPrepareFunc`][pydantic_ai.tools.ToolPrepareFunc].</span>
<span class="sd">        docstring_format: The format of the docstring, see [`DocstringFormat`][pydantic_ai.tools.DocstringFormat].</span>
<span class="sd">            Defaults to `'auto'`, such that the format is inferred from the structure of the docstring.</span>
<span class="sd">        require_parameter_descriptions: If True, raise an error if a parameter description is missing. Defaults to False.</span>
<span class="sd">        schema_generator: The JSON schema generator class to use for this tool. Defaults to `GenerateToolJsonSchema`.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="n">func</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>

        <span class="k">def</span><span class="w"> </span><span class="nf">tool_decorator</span><span class="p">(</span><span class="n">func_</span><span class="p">:</span> <span class="n">ToolFuncPlain</span><span class="p">[</span><span class="n">ToolParams</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">ToolFuncPlain</span><span class="p">[</span><span class="n">ToolParams</span><span class="p">]:</span>
            <span class="c1"># noinspection PyTypeChecker</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_register_function</span><span class="p">(</span>
                <span class="n">func_</span><span class="p">,</span>
                <span class="kc">False</span><span class="p">,</span>
                <span class="n">name</span><span class="p">,</span>
                <span class="n">retries</span><span class="p">,</span>
                <span class="n">prepare</span><span class="p">,</span>
                <span class="n">docstring_format</span><span class="p">,</span>
                <span class="n">require_parameter_descriptions</span><span class="p">,</span>
                <span class="n">schema_generator</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="k">return</span> <span class="n">func_</span>

        <span class="k">return</span> <span class="n">tool_decorator</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_register_function</span><span class="p">(</span>
            <span class="n">func</span><span class="p">,</span> <span class="kc">False</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span> <span class="n">retries</span><span class="p">,</span> <span class="n">prepare</span><span class="p">,</span> <span class="n">docstring_format</span><span class="p">,</span> <span class="n">require_parameter_descriptions</span><span class="p">,</span> <span class="n">schema_generator</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="n">func</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>


























<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.agent.Agent.is_model_request_node" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">is_model_request_node</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-staticmethod"><code>staticmethod</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_57"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_57 > code"></button><code><span class="nf">is_model_request_node</span><span class="p">(</span>
    <span class="n">node</span><span class="p">:</span> <span class="n"><span title="pydantic_ai._agent_graph.AgentNode">AgentNode</span></span><span class="p">[</span><span class="n"><span title="pydantic_ai.agent.T">T</span></span><span class="p">,</span> <span class="n"><span title="pydantic_ai.agent.S">S</span></span><span class="p">]</span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.End" href="../pydantic_graph/nodes/#pydantic_graph.nodes.End">End</a></span><span class="p">[</span><span class="n"><span title="pydantic_ai.result.FinalResult">FinalResult</span></span><span class="p">[</span><span class="n"><span title="pydantic_ai.agent.S">S</span></span><span class="p">]],</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" title="typing_extensions.TypeGuard" href="https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypeGuard">TypeGuard</a></span><span class="p">[</span><span class="n"><span title="pydantic_ai._agent_graph.ModelRequestNode">ModelRequestNode</span></span><span class="p">[</span><span class="n"><span title="pydantic_ai.agent.T">T</span></span><span class="p">,</span> <span class="n"><span title="pydantic_ai.agent.S">S</span></span><span class="p">]]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Check if the node is a <code>ModelRequestNode</code>, narrowing the type if it is.</p>
<p>This method preserves the generic parameters while narrowing the type, unlike a direct call to <code>isinstance</code>.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/agent.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">1250</span>
<span class="normal">1251</span>
<span class="normal">1252</span>
<span class="normal">1253</span>
<span class="normal">1254</span>
<span class="normal">1255</span>
<span class="normal">1256</span>
<span class="normal">1257</span>
<span class="normal">1258</span></pre></div></td><td class="code"><div><pre id="__code_58"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_58 > code"></button><code tabindex="0"><span class="nd">@staticmethod</span>
<span class="k">def</span><span class="w"> </span><span class="nf">is_model_request_node</span><span class="p">(</span>
    <span class="n">node</span><span class="p">:</span> <span class="n">_agent_graph</span><span class="o">.</span><span class="n">AgentNode</span><span class="p">[</span><span class="n">T</span><span class="p">,</span> <span class="n">S</span><span class="p">]</span> <span class="o">|</span> <span class="n">End</span><span class="p">[</span><span class="n">result</span><span class="o">.</span><span class="n">FinalResult</span><span class="p">[</span><span class="n">S</span><span class="p">]],</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TypeGuard</span><span class="p">[</span><span class="n">_agent_graph</span><span class="o">.</span><span class="n">ModelRequestNode</span><span class="p">[</span><span class="n">T</span><span class="p">,</span> <span class="n">S</span><span class="p">]]:</span>
<span class="w">    </span><span class="sd">"""Check if the node is a `ModelRequestNode`, narrowing the type if it is.</span>

<span class="sd">    This method preserves the generic parameters while narrowing the type, unlike a direct call to `isinstance`.</span>
<span class="sd">    """</span>
    <span class="k">return</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">node</span><span class="p">,</span> <span class="n">_agent_graph</span><span class="o">.</span><span class="n">ModelRequestNode</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.agent.Agent.is_call_tools_node" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">is_call_tools_node</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-staticmethod"><code>staticmethod</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_59"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_59 > code"></button><code><span class="nf">is_call_tools_node</span><span class="p">(</span>
    <span class="n">node</span><span class="p">:</span> <span class="n"><span title="pydantic_ai._agent_graph.AgentNode">AgentNode</span></span><span class="p">[</span><span class="n"><span title="pydantic_ai.agent.T">T</span></span><span class="p">,</span> <span class="n"><span title="pydantic_ai.agent.S">S</span></span><span class="p">]</span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.End" href="../pydantic_graph/nodes/#pydantic_graph.nodes.End">End</a></span><span class="p">[</span><span class="n"><span title="pydantic_ai.result.FinalResult">FinalResult</span></span><span class="p">[</span><span class="n"><span title="pydantic_ai.agent.S">S</span></span><span class="p">]],</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" title="typing_extensions.TypeGuard" href="https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypeGuard">TypeGuard</a></span><span class="p">[</span><span class="n"><span title="pydantic_ai._agent_graph.CallToolsNode">CallToolsNode</span></span><span class="p">[</span><span class="n"><span title="pydantic_ai.agent.T">T</span></span><span class="p">,</span> <span class="n"><span title="pydantic_ai.agent.S">S</span></span><span class="p">]]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Check if the node is a <code>CallToolsNode</code>, narrowing the type if it is.</p>
<p>This method preserves the generic parameters while narrowing the type, unlike a direct call to <code>isinstance</code>.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/agent.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">1260</span>
<span class="normal">1261</span>
<span class="normal">1262</span>
<span class="normal">1263</span>
<span class="normal">1264</span>
<span class="normal">1265</span>
<span class="normal">1266</span>
<span class="normal">1267</span>
<span class="normal">1268</span></pre></div></td><td class="code"><div><pre id="__code_60"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_60 > code"></button><code tabindex="0"><span class="nd">@staticmethod</span>
<span class="k">def</span><span class="w"> </span><span class="nf">is_call_tools_node</span><span class="p">(</span>
    <span class="n">node</span><span class="p">:</span> <span class="n">_agent_graph</span><span class="o">.</span><span class="n">AgentNode</span><span class="p">[</span><span class="n">T</span><span class="p">,</span> <span class="n">S</span><span class="p">]</span> <span class="o">|</span> <span class="n">End</span><span class="p">[</span><span class="n">result</span><span class="o">.</span><span class="n">FinalResult</span><span class="p">[</span><span class="n">S</span><span class="p">]],</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TypeGuard</span><span class="p">[</span><span class="n">_agent_graph</span><span class="o">.</span><span class="n">CallToolsNode</span><span class="p">[</span><span class="n">T</span><span class="p">,</span> <span class="n">S</span><span class="p">]]:</span>
<span class="w">    </span><span class="sd">"""Check if the node is a `CallToolsNode`, narrowing the type if it is.</span>

<span class="sd">    This method preserves the generic parameters while narrowing the type, unlike a direct call to `isinstance`.</span>
<span class="sd">    """</span>
    <span class="k">return</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">node</span><span class="p">,</span> <span class="n">_agent_graph</span><span class="o">.</span><span class="n">CallToolsNode</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.agent.Agent.is_user_prompt_node" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">is_user_prompt_node</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-staticmethod"><code>staticmethod</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_61"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_61 > code"></button><code><span class="nf">is_user_prompt_node</span><span class="p">(</span>
    <span class="n">node</span><span class="p">:</span> <span class="n"><span title="pydantic_ai._agent_graph.AgentNode">AgentNode</span></span><span class="p">[</span><span class="n"><span title="pydantic_ai.agent.T">T</span></span><span class="p">,</span> <span class="n"><span title="pydantic_ai.agent.S">S</span></span><span class="p">]</span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.End" href="../pydantic_graph/nodes/#pydantic_graph.nodes.End">End</a></span><span class="p">[</span><span class="n"><span title="pydantic_ai.result.FinalResult">FinalResult</span></span><span class="p">[</span><span class="n"><span title="pydantic_ai.agent.S">S</span></span><span class="p">]],</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" title="typing_extensions.TypeGuard" href="https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypeGuard">TypeGuard</a></span><span class="p">[</span><span class="n"><span title="pydantic_ai._agent_graph.UserPromptNode">UserPromptNode</span></span><span class="p">[</span><span class="n"><span title="pydantic_ai.agent.T">T</span></span><span class="p">,</span> <span class="n"><span title="pydantic_ai.agent.S">S</span></span><span class="p">]]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Check if the node is a <code>UserPromptNode</code>, narrowing the type if it is.</p>
<p>This method preserves the generic parameters while narrowing the type, unlike a direct call to <code>isinstance</code>.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/agent.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">1270</span>
<span class="normal">1271</span>
<span class="normal">1272</span>
<span class="normal">1273</span>
<span class="normal">1274</span>
<span class="normal">1275</span>
<span class="normal">1276</span>
<span class="normal">1277</span>
<span class="normal">1278</span></pre></div></td><td class="code"><div><pre id="__code_62"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_62 > code"></button><code tabindex="0"><span class="nd">@staticmethod</span>
<span class="k">def</span><span class="w"> </span><span class="nf">is_user_prompt_node</span><span class="p">(</span>
    <span class="n">node</span><span class="p">:</span> <span class="n">_agent_graph</span><span class="o">.</span><span class="n">AgentNode</span><span class="p">[</span><span class="n">T</span><span class="p">,</span> <span class="n">S</span><span class="p">]</span> <span class="o">|</span> <span class="n">End</span><span class="p">[</span><span class="n">result</span><span class="o">.</span><span class="n">FinalResult</span><span class="p">[</span><span class="n">S</span><span class="p">]],</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TypeGuard</span><span class="p">[</span><span class="n">_agent_graph</span><span class="o">.</span><span class="n">UserPromptNode</span><span class="p">[</span><span class="n">T</span><span class="p">,</span> <span class="n">S</span><span class="p">]]:</span>
<span class="w">    </span><span class="sd">"""Check if the node is a `UserPromptNode`, narrowing the type if it is.</span>

<span class="sd">    This method preserves the generic parameters while narrowing the type, unlike a direct call to `isinstance`.</span>
<span class="sd">    """</span>
    <span class="k">return</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">node</span><span class="p">,</span> <span class="n">_agent_graph</span><span class="o">.</span><span class="n">UserPromptNode</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.agent.Agent.is_end_node" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">is_end_node</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-staticmethod"><code>staticmethod</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_63"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_63 > code"></button><code><span class="nf">is_end_node</span><span class="p">(</span>
    <span class="n">node</span><span class="p">:</span> <span class="n"><span title="pydantic_ai._agent_graph.AgentNode">AgentNode</span></span><span class="p">[</span><span class="n"><span title="pydantic_ai.agent.T">T</span></span><span class="p">,</span> <span class="n"><span title="pydantic_ai.agent.S">S</span></span><span class="p">]</span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.End" href="../pydantic_graph/nodes/#pydantic_graph.nodes.End">End</a></span><span class="p">[</span><span class="n"><span title="pydantic_ai.result.FinalResult">FinalResult</span></span><span class="p">[</span><span class="n"><span title="pydantic_ai.agent.S">S</span></span><span class="p">]],</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" title="typing_extensions.TypeGuard" href="https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypeGuard">TypeGuard</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.End" href="../pydantic_graph/nodes/#pydantic_graph.nodes.End">End</a></span><span class="p">[</span><span class="n"><span title="pydantic_ai.result.FinalResult">FinalResult</span></span><span class="p">[</span><span class="n"><span title="pydantic_ai.agent.S">S</span></span><span class="p">]]]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Check if the node is a <code>End</code>, narrowing the type if it is.</p>
<p>This method preserves the generic parameters while narrowing the type, unlike a direct call to <code>isinstance</code>.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/agent.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">1280</span>
<span class="normal">1281</span>
<span class="normal">1282</span>
<span class="normal">1283</span>
<span class="normal">1284</span>
<span class="normal">1285</span>
<span class="normal">1286</span>
<span class="normal">1287</span>
<span class="normal">1288</span></pre></div></td><td class="code"><div><pre id="__code_64"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_64 > code"></button><code tabindex="0"><span class="nd">@staticmethod</span>
<span class="k">def</span><span class="w"> </span><span class="nf">is_end_node</span><span class="p">(</span>
    <span class="n">node</span><span class="p">:</span> <span class="n">_agent_graph</span><span class="o">.</span><span class="n">AgentNode</span><span class="p">[</span><span class="n">T</span><span class="p">,</span> <span class="n">S</span><span class="p">]</span> <span class="o">|</span> <span class="n">End</span><span class="p">[</span><span class="n">result</span><span class="o">.</span><span class="n">FinalResult</span><span class="p">[</span><span class="n">S</span><span class="p">]],</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TypeGuard</span><span class="p">[</span><span class="n">End</span><span class="p">[</span><span class="n">result</span><span class="o">.</span><span class="n">FinalResult</span><span class="p">[</span><span class="n">S</span><span class="p">]]]:</span>
<span class="w">    </span><span class="sd">"""Check if the node is a `End`, narrowing the type if it is.</span>

<span class="sd">    This method preserves the generic parameters while narrowing the type, unlike a direct call to `isinstance`.</span>
<span class="sd">    """</span>
    <span class="k">return</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">node</span><span class="p">,</span> <span class="n">End</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.agent.Agent.run_mcp_servers" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">run_mcp_servers</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-async"><code>async</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_65"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_65 > code"></button><code><span class="nf">run_mcp_servers</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" title="collections.abc.AsyncIterator" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator">AsyncIterator</a></span><span class="p">[</span><span class="kc">None</span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Run <a class="autorefs autorefs-internal" href="../mcp/#pydantic_ai.mcp.MCPServerStdio"><code>MCPServerStdio</code>s</a> so they can be used by the agent.</p>
<p>Returns: a context manager to start and shutdown the servers.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/agent.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">1290</span>
<span class="normal">1291</span>
<span class="normal">1292</span>
<span class="normal">1293</span>
<span class="normal">1294</span>
<span class="normal">1295</span>
<span class="normal">1296</span>
<span class="normal">1297</span>
<span class="normal">1298</span>
<span class="normal">1299</span>
<span class="normal">1300</span>
<span class="normal">1301</span>
<span class="normal">1302</span></pre></div></td><td class="code"><div><pre id="__code_66"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_66 > code"></button><code><span class="nd">@asynccontextmanager</span>
<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">run_mcp_servers</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AsyncIterator</span><span class="p">[</span><span class="kc">None</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Run [`MCPServerStdio`s][pydantic_ai.mcp.MCPServerStdio] so they can be used by the agent.</span>

<span class="sd">    Returns: a context manager to start and shutdown the servers.</span>
<span class="sd">    """</span>
    <span class="n">exit_stack</span> <span class="o">=</span> <span class="n">AsyncExitStack</span><span class="p">()</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="k">for</span> <span class="n">mcp_server</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_mcp_servers</span><span class="p">:</span>
            <span class="k">await</span> <span class="n">exit_stack</span><span class="o">.</span><span class="n">enter_async_context</span><span class="p">(</span><span class="n">mcp_server</span><span class="p">)</span>
        <span class="k">yield</span>
    <span class="k">finally</span><span class="p">:</span>
        <span class="k">await</span> <span class="n">exit_stack</span><span class="o">.</span><span class="n">aclose</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>




  </div>

    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_ai.agent.AgentRun" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">AgentRun</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">
            <p class="doc doc-class-bases">
              Bases: <code><a class="autorefs autorefs-external" title="typing.Generic" href="https://docs.python.org/3/library/typing.html#typing.Generic">Generic</a>[<a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a>, <a class="autorefs autorefs-internal" title="pydantic_ai.result.ResultDataT" href="../result/#pydantic_ai.result.ResultDataT">ResultDataT</a>]</code></p>


        <p>A stateful, async-iterable run of an <a class="autorefs autorefs-internal" href="#pydantic_ai.agent.Agent"><code>Agent</code></a>.</p>
<p>You generally obtain an <code>AgentRun</code> instance by calling <code>async with my_agent.iter(...) as agent_run:</code>.</p>
<p>Once you have an instance, you can use it to iterate through the run's nodes as they execute. When an
<a class="autorefs autorefs-internal" href="../pydantic_graph/nodes/#pydantic_graph.nodes.End"><code>End</code></a> is reached, the run finishes and <a class="autorefs autorefs-internal" href="#pydantic_ai.agent.AgentRun.result"><code>result</code></a>
becomes available.</p>
<p>Example:
</p><div class="language-python highlight"><pre id="__code_67"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_67 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>

<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="s1">'openai:gpt-4o'</span><span class="p">)</span>

<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">main</span><span class="p">():</span>
    <span class="n">nodes</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="c1"># Iterate through the run, recording each node along the way:</span>
    <span class="k">async</span> <span class="k">with</span> <span class="n">agent</span><span class="o">.</span><span class="n">iter</span><span class="p">(</span><span class="s1">'What is the capital of France?'</span><span class="p">)</span> <span class="k">as</span> <span class="n">agent_run</span><span class="p">:</span>
        <span class="k">async</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">agent_run</span><span class="p">:</span>
            <span class="n">nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span>
<span class="w">    </span><span class="sd">'''</span>
<span class="sd">    [</span>
<span class="sd">        ModelRequestNode(</span>
<span class="sd">            request=ModelRequest(</span>
<span class="sd">                parts=[</span>
<span class="sd">                    UserPromptPart(</span>
<span class="sd">                        content='What is the capital of France?',</span>
<span class="sd">                        timestamp=datetime.datetime(...),</span>
<span class="sd">                        part_kind='user-prompt',</span>
<span class="sd">                    )</span>
<span class="sd">                ],</span>
<span class="sd">                kind='request',</span>
<span class="sd">            )</span>
<span class="sd">        ),</span>
<span class="sd">        CallToolsNode(</span>
<span class="sd">            model_response=ModelResponse(</span>
<span class="sd">                parts=[TextPart(content='Paris', part_kind='text')],</span>
<span class="sd">                model_name='gpt-4o',</span>
<span class="sd">                timestamp=datetime.datetime(...),</span>
<span class="sd">                kind='response',</span>
<span class="sd">            )</span>
<span class="sd">        ),</span>
<span class="sd">        End(data=FinalResult(data='Paris', tool_name=None, tool_call_id=None)),</span>
<span class="sd">    ]</span>
<span class="sd">    '''</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">agent_run</span><span class="o">.</span><span class="n">result</span><span class="o">.</span><span class="n">data</span><span class="p">)</span>
    <span class="c1">#&gt; Paris</span>
</code></pre></div><p></p>
<p>You can also manually drive the iteration using the <a class="autorefs autorefs-internal" href="#pydantic_ai.agent.AgentRun.next"><code>next</code></a> method for
more granular control.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/agent.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">1305</span>
<span class="normal">1306</span>
<span class="normal">1307</span>
<span class="normal">1308</span>
<span class="normal">1309</span>
<span class="normal">1310</span>
<span class="normal">1311</span>
<span class="normal">1312</span>
<span class="normal">1313</span>
<span class="normal">1314</span>
<span class="normal">1315</span>
<span class="normal">1316</span>
<span class="normal">1317</span>
<span class="normal">1318</span>
<span class="normal">1319</span>
<span class="normal">1320</span>
<span class="normal">1321</span>
<span class="normal">1322</span>
<span class="normal">1323</span>
<span class="normal">1324</span>
<span class="normal">1325</span>
<span class="normal">1326</span>
<span class="normal">1327</span>
<span class="normal">1328</span>
<span class="normal">1329</span>
<span class="normal">1330</span>
<span class="normal">1331</span>
<span class="normal">1332</span>
<span class="normal">1333</span>
<span class="normal">1334</span>
<span class="normal">1335</span>
<span class="normal">1336</span>
<span class="normal">1337</span>
<span class="normal">1338</span>
<span class="normal">1339</span>
<span class="normal">1340</span>
<span class="normal">1341</span>
<span class="normal">1342</span>
<span class="normal">1343</span>
<span class="normal">1344</span>
<span class="normal">1345</span>
<span class="normal">1346</span>
<span class="normal">1347</span>
<span class="normal">1348</span>
<span class="normal">1349</span>
<span class="normal">1350</span>
<span class="normal">1351</span>
<span class="normal">1352</span>
<span class="normal">1353</span>
<span class="normal">1354</span>
<span class="normal">1355</span>
<span class="normal">1356</span>
<span class="normal">1357</span>
<span class="normal">1358</span>
<span class="normal">1359</span>
<span class="normal">1360</span>
<span class="normal">1361</span>
<span class="normal">1362</span>
<span class="normal">1363</span>
<span class="normal">1364</span>
<span class="normal">1365</span>
<span class="normal">1366</span>
<span class="normal">1367</span>
<span class="normal">1368</span>
<span class="normal">1369</span>
<span class="normal">1370</span>
<span class="normal">1371</span>
<span class="normal">1372</span>
<span class="normal">1373</span>
<span class="normal">1374</span>
<span class="normal">1375</span>
<span class="normal">1376</span>
<span class="normal">1377</span>
<span class="normal">1378</span>
<span class="normal">1379</span>
<span class="normal">1380</span>
<span class="normal">1381</span>
<span class="normal">1382</span>
<span class="normal">1383</span>
<span class="normal">1384</span>
<span class="normal">1385</span>
<span class="normal">1386</span>
<span class="normal">1387</span>
<span class="normal">1388</span>
<span class="normal">1389</span>
<span class="normal">1390</span>
<span class="normal">1391</span>
<span class="normal">1392</span>
<span class="normal">1393</span>
<span class="normal">1394</span>
<span class="normal">1395</span>
<span class="normal">1396</span>
<span class="normal">1397</span>
<span class="normal">1398</span>
<span class="normal">1399</span>
<span class="normal">1400</span>
<span class="normal">1401</span>
<span class="normal">1402</span>
<span class="normal">1403</span>
<span class="normal">1404</span>
<span class="normal">1405</span>
<span class="normal">1406</span>
<span class="normal">1407</span>
<span class="normal">1408</span>
<span class="normal">1409</span>
<span class="normal">1410</span>
<span class="normal">1411</span>
<span class="normal">1412</span>
<span class="normal">1413</span>
<span class="normal">1414</span>
<span class="normal">1415</span>
<span class="normal">1416</span>
<span class="normal">1417</span>
<span class="normal">1418</span>
<span class="normal">1419</span>
<span class="normal">1420</span>
<span class="normal">1421</span>
<span class="normal">1422</span>
<span class="normal">1423</span>
<span class="normal">1424</span>
<span class="normal">1425</span>
<span class="normal">1426</span>
<span class="normal">1427</span>
<span class="normal">1428</span>
<span class="normal">1429</span>
<span class="normal">1430</span>
<span class="normal">1431</span>
<span class="normal">1432</span>
<span class="normal">1433</span>
<span class="normal">1434</span>
<span class="normal">1435</span>
<span class="normal">1436</span>
<span class="normal">1437</span>
<span class="normal">1438</span>
<span class="normal">1439</span>
<span class="normal">1440</span>
<span class="normal">1441</span>
<span class="normal">1442</span>
<span class="normal">1443</span>
<span class="normal">1444</span>
<span class="normal">1445</span>
<span class="normal">1446</span>
<span class="normal">1447</span>
<span class="normal">1448</span>
<span class="normal">1449</span>
<span class="normal">1450</span>
<span class="normal">1451</span>
<span class="normal">1452</span>
<span class="normal">1453</span>
<span class="normal">1454</span>
<span class="normal">1455</span>
<span class="normal">1456</span>
<span class="normal">1457</span>
<span class="normal">1458</span>
<span class="normal">1459</span>
<span class="normal">1460</span>
<span class="normal">1461</span>
<span class="normal">1462</span>
<span class="normal">1463</span>
<span class="normal">1464</span>
<span class="normal">1465</span>
<span class="normal">1466</span>
<span class="normal">1467</span>
<span class="normal">1468</span>
<span class="normal">1469</span>
<span class="normal">1470</span>
<span class="normal">1471</span>
<span class="normal">1472</span>
<span class="normal">1473</span>
<span class="normal">1474</span>
<span class="normal">1475</span>
<span class="normal">1476</span>
<span class="normal">1477</span>
<span class="normal">1478</span>
<span class="normal">1479</span>
<span class="normal">1480</span>
<span class="normal">1481</span>
<span class="normal">1482</span>
<span class="normal">1483</span>
<span class="normal">1484</span>
<span class="normal">1485</span>
<span class="normal">1486</span>
<span class="normal">1487</span>
<span class="normal">1488</span>
<span class="normal">1489</span>
<span class="normal">1490</span>
<span class="normal">1491</span>
<span class="normal">1492</span>
<span class="normal">1493</span>
<span class="normal">1494</span>
<span class="normal">1495</span>
<span class="normal">1496</span>
<span class="normal">1497</span>
<span class="normal">1498</span>
<span class="normal">1499</span>
<span class="normal">1500</span>
<span class="normal">1501</span>
<span class="normal">1502</span>
<span class="normal">1503</span></pre></div></td><td class="code"><div><pre id="__code_68"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_68 > code"></button><code tabindex="0"><span class="nd">@dataclasses</span><span class="o">.</span><span class="n">dataclass</span><span class="p">(</span><span class="nb">repr</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
<span class="k">class</span><span class="w"> </span><span class="nc">AgentRun</span><span class="p">(</span><span class="n">Generic</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">,</span> <span class="n">ResultDataT</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""A stateful, async-iterable run of an [`Agent`][pydantic_ai.agent.Agent].</span>

<span class="sd">    You generally obtain an `AgentRun` instance by calling `async with my_agent.iter(...) as agent_run:`.</span>

<span class="sd">    Once you have an instance, you can use it to iterate through the run's nodes as they execute. When an</span>
<span class="sd">    [`End`][pydantic_graph.nodes.End] is reached, the run finishes and [`result`][pydantic_ai.agent.AgentRun.result]</span>
<span class="sd">    becomes available.</span>

<span class="sd">    Example:</span>
<span class="sd">    ```python</span>
<span class="sd">    from pydantic_ai import Agent</span>

<span class="sd">    agent = Agent('openai:gpt-4o')</span>

<span class="sd">    async def main():</span>
<span class="sd">        nodes = []</span>
<span class="sd">        # Iterate through the run, recording each node along the way:</span>
<span class="sd">        async with agent.iter('What is the capital of France?') as agent_run:</span>
<span class="sd">            async for node in agent_run:</span>
<span class="sd">                nodes.append(node)</span>
<span class="sd">        print(nodes)</span>
<span class="sd">        '''</span>
<span class="sd">        [</span>
<span class="sd">            ModelRequestNode(</span>
<span class="sd">                request=ModelRequest(</span>
<span class="sd">                    parts=[</span>
<span class="sd">                        UserPromptPart(</span>
<span class="sd">                            content='What is the capital of France?',</span>
<span class="sd">                            timestamp=datetime.datetime(...),</span>
<span class="sd">                            part_kind='user-prompt',</span>
<span class="sd">                        )</span>
<span class="sd">                    ],</span>
<span class="sd">                    kind='request',</span>
<span class="sd">                )</span>
<span class="sd">            ),</span>
<span class="sd">            CallToolsNode(</span>
<span class="sd">                model_response=ModelResponse(</span>
<span class="sd">                    parts=[TextPart(content='Paris', part_kind='text')],</span>
<span class="sd">                    model_name='gpt-4o',</span>
<span class="sd">                    timestamp=datetime.datetime(...),</span>
<span class="sd">                    kind='response',</span>
<span class="sd">                )</span>
<span class="sd">            ),</span>
<span class="sd">            End(data=FinalResult(data='Paris', tool_name=None, tool_call_id=None)),</span>
<span class="sd">        ]</span>
<span class="sd">        '''</span>
<span class="sd">        print(agent_run.result.data)</span>
<span class="sd">        #&gt; Paris</span>
<span class="sd">    ```</span>

<span class="sd">    You can also manually drive the iteration using the [`next`][pydantic_ai.agent.AgentRun.next] method for</span>
<span class="sd">    more granular control.</span>
<span class="sd">    """</span>

    <span class="n">_graph_run</span><span class="p">:</span> <span class="n">GraphRun</span><span class="p">[</span>
        <span class="n">_agent_graph</span><span class="o">.</span><span class="n">GraphAgentState</span><span class="p">,</span> <span class="n">_agent_graph</span><span class="o">.</span><span class="n">GraphAgentDeps</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span> <span class="n">FinalResult</span><span class="p">[</span><span class="n">ResultDataT</span><span class="p">]</span>
    <span class="p">]</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">ctx</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">GraphRunContext</span><span class="p">[</span><span class="n">_agent_graph</span><span class="o">.</span><span class="n">GraphAgentState</span><span class="p">,</span> <span class="n">_agent_graph</span><span class="o">.</span><span class="n">GraphAgentDeps</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""The current context of the agent run."""</span>
        <span class="k">return</span> <span class="n">GraphRunContext</span><span class="p">[</span><span class="n">_agent_graph</span><span class="o">.</span><span class="n">GraphAgentState</span><span class="p">,</span> <span class="n">_agent_graph</span><span class="o">.</span><span class="n">GraphAgentDeps</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">,</span> <span class="n">Any</span><span class="p">]](</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_graph_run</span><span class="o">.</span><span class="n">state</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_graph_run</span><span class="o">.</span><span class="n">deps</span>
        <span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">next_node</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">_agent_graph</span><span class="o">.</span><span class="n">AgentNode</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">,</span> <span class="n">ResultDataT</span><span class="p">]</span> <span class="o">|</span> <span class="n">End</span><span class="p">[</span><span class="n">FinalResult</span><span class="p">[</span><span class="n">ResultDataT</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""The next node that will be run in the agent graph.</span>

<span class="sd">        This is the next node that will be used during async iteration, or if a node is not passed to `self.next(...)`.</span>
<span class="sd">        """</span>
        <span class="n">next_node</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_graph_run</span><span class="o">.</span><span class="n">next_node</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">next_node</span><span class="p">,</span> <span class="n">End</span><span class="p">):</span>
            <span class="k">return</span> <span class="n">next_node</span>
        <span class="k">if</span> <span class="n">_agent_graph</span><span class="o">.</span><span class="n">is_agent_node</span><span class="p">(</span><span class="n">next_node</span><span class="p">):</span>
            <span class="k">return</span> <span class="n">next_node</span>
        <span class="k">raise</span> <span class="n">exceptions</span><span class="o">.</span><span class="n">AgentRunError</span><span class="p">(</span><span class="sa">f</span><span class="s1">'Unexpected node type: </span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="n">next_node</span><span class="p">)</span><span class="si">}</span><span class="s1">'</span><span class="p">)</span>  <span class="c1"># pragma: no cover</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">result</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AgentRunResult</span><span class="p">[</span><span class="n">ResultDataT</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""The final result of the run if it has ended, otherwise `None`.</span>

<span class="sd">        Once the run returns an [`End`][pydantic_graph.nodes.End] node, `result` is populated</span>
<span class="sd">        with an [`AgentRunResult`][pydantic_ai.agent.AgentRunResult].</span>
<span class="sd">        """</span>
        <span class="n">graph_run_result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_graph_run</span><span class="o">.</span><span class="n">result</span>
        <span class="k">if</span> <span class="n">graph_run_result</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">return</span> <span class="kc">None</span>
        <span class="k">return</span> <span class="n">AgentRunResult</span><span class="p">(</span>
            <span class="n">graph_run_result</span><span class="o">.</span><span class="n">output</span><span class="o">.</span><span class="n">data</span><span class="p">,</span>
            <span class="n">graph_run_result</span><span class="o">.</span><span class="n">output</span><span class="o">.</span><span class="n">tool_name</span><span class="p">,</span>
            <span class="n">graph_run_result</span><span class="o">.</span><span class="n">state</span><span class="p">,</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_graph_run</span><span class="o">.</span><span class="n">deps</span><span class="o">.</span><span class="n">new_message_index</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="fm">__aiter__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AsyncIterator</span><span class="p">[</span><span class="n">_agent_graph</span><span class="o">.</span><span class="n">AgentNode</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">,</span> <span class="n">ResultDataT</span><span class="p">]</span> <span class="o">|</span> <span class="n">End</span><span class="p">[</span><span class="n">FinalResult</span><span class="p">[</span><span class="n">ResultDataT</span><span class="p">]]]:</span>
<span class="w">        </span><span class="sd">"""Provide async-iteration over the nodes in the agent run."""</span>
        <span class="k">return</span> <span class="bp">self</span>

    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="fm">__anext__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">_agent_graph</span><span class="o">.</span><span class="n">AgentNode</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">,</span> <span class="n">ResultDataT</span><span class="p">]</span> <span class="o">|</span> <span class="n">End</span><span class="p">[</span><span class="n">FinalResult</span><span class="p">[</span><span class="n">ResultDataT</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""Advance to the next node automatically based on the last returned node."""</span>
        <span class="n">next_node</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_graph_run</span><span class="o">.</span><span class="fm">__anext__</span><span class="p">()</span>
        <span class="k">if</span> <span class="n">_agent_graph</span><span class="o">.</span><span class="n">is_agent_node</span><span class="p">(</span><span class="n">next_node</span><span class="p">):</span>
            <span class="k">return</span> <span class="n">next_node</span>
        <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">next_node</span><span class="p">,</span> <span class="n">End</span><span class="p">),</span> <span class="sa">f</span><span class="s1">'Unexpected node type: </span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="n">next_node</span><span class="p">)</span><span class="si">}</span><span class="s1">'</span>
        <span class="k">return</span> <span class="n">next_node</span>

    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">next</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">node</span><span class="p">:</span> <span class="n">_agent_graph</span><span class="o">.</span><span class="n">AgentNode</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">,</span> <span class="n">ResultDataT</span><span class="p">],</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">_agent_graph</span><span class="o">.</span><span class="n">AgentNode</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">,</span> <span class="n">ResultDataT</span><span class="p">]</span> <span class="o">|</span> <span class="n">End</span><span class="p">[</span><span class="n">FinalResult</span><span class="p">[</span><span class="n">ResultDataT</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""Manually drive the agent run by passing in the node you want to run next.</span>

<span class="sd">        This lets you inspect or mutate the node before continuing execution, or skip certain nodes</span>
<span class="sd">        under dynamic conditions. The agent run should be stopped when you return an [`End`][pydantic_graph.nodes.End]</span>
<span class="sd">        node.</span>

<span class="sd">        Example:</span>
<span class="sd">        ```python</span>
<span class="sd">        from pydantic_ai import Agent</span>
<span class="sd">        from pydantic_graph import End</span>

<span class="sd">        agent = Agent('openai:gpt-4o')</span>

<span class="sd">        async def main():</span>
<span class="sd">            async with agent.iter('What is the capital of France?') as agent_run:</span>
<span class="sd">                next_node = agent_run.next_node  # start with the first node</span>
<span class="sd">                nodes = [next_node]</span>
<span class="sd">                while not isinstance(next_node, End):</span>
<span class="sd">                    next_node = await agent_run.next(next_node)</span>
<span class="sd">                    nodes.append(next_node)</span>
<span class="sd">                # Once `next_node` is an End, we've finished:</span>
<span class="sd">                print(nodes)</span>
<span class="sd">                '''</span>
<span class="sd">                [</span>
<span class="sd">                    UserPromptNode(</span>
<span class="sd">                        user_prompt='What is the capital of France?',</span>
<span class="sd">                        system_prompts=(),</span>
<span class="sd">                        system_prompt_functions=[],</span>
<span class="sd">                        system_prompt_dynamic_functions={},</span>
<span class="sd">                    ),</span>
<span class="sd">                    ModelRequestNode(</span>
<span class="sd">                        request=ModelRequest(</span>
<span class="sd">                            parts=[</span>
<span class="sd">                                UserPromptPart(</span>
<span class="sd">                                    content='What is the capital of France?',</span>
<span class="sd">                                    timestamp=datetime.datetime(...),</span>
<span class="sd">                                    part_kind='user-prompt',</span>
<span class="sd">                                )</span>
<span class="sd">                            ],</span>
<span class="sd">                            kind='request',</span>
<span class="sd">                        )</span>
<span class="sd">                    ),</span>
<span class="sd">                    CallToolsNode(</span>
<span class="sd">                        model_response=ModelResponse(</span>
<span class="sd">                            parts=[TextPart(content='Paris', part_kind='text')],</span>
<span class="sd">                            model_name='gpt-4o',</span>
<span class="sd">                            timestamp=datetime.datetime(...),</span>
<span class="sd">                            kind='response',</span>
<span class="sd">                        )</span>
<span class="sd">                    ),</span>
<span class="sd">                    End(data=FinalResult(data='Paris', tool_name=None, tool_call_id=None)),</span>
<span class="sd">                ]</span>
<span class="sd">                '''</span>
<span class="sd">                print('Final result:', agent_run.result.data)</span>
<span class="sd">                #&gt; Final result: Paris</span>
<span class="sd">        ```</span>

<span class="sd">        Args:</span>
<span class="sd">            node: The node to run next in the graph.</span>

<span class="sd">        Returns:</span>
<span class="sd">            The next node returned by the graph logic, or an [`End`][pydantic_graph.nodes.End] node if</span>
<span class="sd">            the run has completed.</span>
<span class="sd">        """</span>
        <span class="c1"># Note: It might be nice to expose a synchronous interface for iteration, but we shouldn't do it</span>
        <span class="c1"># on this class, or else IDEs won't warn you if you accidentally use `for` instead of `async for` to iterate.</span>
        <span class="n">next_node</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_graph_run</span><span class="o">.</span><span class="n">next</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">_agent_graph</span><span class="o">.</span><span class="n">is_agent_node</span><span class="p">(</span><span class="n">next_node</span><span class="p">):</span>
            <span class="k">return</span> <span class="n">next_node</span>
        <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">next_node</span><span class="p">,</span> <span class="n">End</span><span class="p">),</span> <span class="sa">f</span><span class="s1">'Unexpected node type: </span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="n">next_node</span><span class="p">)</span><span class="si">}</span><span class="s1">'</span>
        <span class="k">return</span> <span class="n">next_node</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">usage</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">_usage</span><span class="o">.</span><span class="n">Usage</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get usage statistics for the run so far, including token usage, model requests, and so on."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_graph_run</span><span class="o">.</span><span class="n">state</span><span class="o">.</span><span class="n">usage</span>

    <span class="k">def</span><span class="w"> </span><span class="fm">__repr__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_graph_run</span><span class="o">.</span><span class="n">result</span>
        <span class="n">result_repr</span> <span class="o">=</span> <span class="s1">'&lt;run not finished&gt;'</span> <span class="k">if</span> <span class="n">result</span> <span class="ow">is</span> <span class="kc">None</span> <span class="k">else</span> <span class="nb">repr</span><span class="p">(</span><span class="n">result</span><span class="o">.</span><span class="n">output</span><span class="p">)</span>
        <span class="k">return</span> <span class="sa">f</span><span class="s1">'&lt;</span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="vm">__name__</span><span class="si">}</span><span class="s1"> result=</span><span class="si">{</span><span class="n">result_repr</span><span class="si">}</span><span class="s1"> usage=</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">usage</span><span class="p">()</span><span class="si">}</span><span class="s1">&gt;'</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.agent.AgentRun.ctx" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">ctx</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-property"><code>property</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_69"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_69 > code"></button><code><span class="n">ctx</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.GraphRunContext" href="../pydantic_graph/nodes/#pydantic_graph.nodes.GraphRunContext">GraphRunContext</a></span><span class="p">[</span>
    <span class="n"><span title="pydantic_ai._agent_graph.GraphAgentState">GraphAgentState</span></span><span class="p">,</span> <span class="n"><span title="pydantic_ai._agent_graph.GraphAgentDeps">GraphAgentDeps</span></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a></span><span class="p">]</span>
<span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The current context of the agent run.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.agent.AgentRun.next_node" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">next_node</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-property"><code>property</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_70"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_70 > code"></button><code><span class="n">next_node</span><span class="p">:</span> <span class="p">(</span>
    <span class="n"><span title="pydantic_ai._agent_graph.AgentNode">AgentNode</span></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.result.ResultDataT" href="../result/#pydantic_ai.result.ResultDataT">ResultDataT</a></span><span class="p">]</span>
    <span class="o">|</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.End" href="../pydantic_graph/nodes/#pydantic_graph.nodes.End">End</a></span><span class="p">[</span><span class="n"><span title="pydantic_ai.result.FinalResult">FinalResult</span></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.result.ResultDataT" href="../result/#pydantic_ai.result.ResultDataT">ResultDataT</a></span><span class="p">]]</span>
<span class="p">)</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The next node that will be run in the agent graph.</p>
<p>This is the next node that will be used during async iteration, or if a node is not passed to <code>self.next(...)</code>.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.agent.AgentRun.result" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">result</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-property"><code>property</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_71"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_71 > code"></button><code><span class="n">result</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.agent.AgentRunResult" href="#pydantic_ai.agent.AgentRunResult">AgentRunResult</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.result.ResultDataT" href="../result/#pydantic_ai.result.ResultDataT">ResultDataT</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The final result of the run if it has ended, otherwise <code>None</code>.</p>
<p>Once the run returns an <a class="autorefs autorefs-internal" href="../pydantic_graph/nodes/#pydantic_graph.nodes.End"><code>End</code></a> node, <code>result</code> is populated
with an <a class="autorefs autorefs-internal" href="#pydantic_ai.agent.AgentRunResult"><code>AgentRunResult</code></a>.</p>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.agent.AgentRun.__aiter__" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">__aiter__</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_72"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_72 > code"></button><code><span class="fm">__aiter__</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="p">(</span>
    <span class="nf"><a class="autorefs autorefs-external" title="collections.abc.AsyncIterator" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator">AsyncIterator</a></span><span class="p">[</span>
        <span class="n"><span title="pydantic_ai._agent_graph.AgentNode">AgentNode</span></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.result.ResultDataT" href="../result/#pydantic_ai.result.ResultDataT">ResultDataT</a></span><span class="p">]</span>
        <span class="o">|</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.End" href="../pydantic_graph/nodes/#pydantic_graph.nodes.End">End</a></span><span class="p">[</span><span class="n"><span title="pydantic_ai.result.FinalResult">FinalResult</span></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.result.ResultDataT" href="../result/#pydantic_ai.result.ResultDataT">ResultDataT</a></span><span class="p">]]</span>
    <span class="p">]</span>
<span class="p">)</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Provide async-iteration over the nodes in the agent run.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/agent.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">1404</span>
<span class="normal">1405</span>
<span class="normal">1406</span>
<span class="normal">1407</span>
<span class="normal">1408</span></pre></div></td><td class="code"><div><pre id="__code_73"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_73 > code"></button><code><span class="k">def</span><span class="w"> </span><span class="fm">__aiter__</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AsyncIterator</span><span class="p">[</span><span class="n">_agent_graph</span><span class="o">.</span><span class="n">AgentNode</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">,</span> <span class="n">ResultDataT</span><span class="p">]</span> <span class="o">|</span> <span class="n">End</span><span class="p">[</span><span class="n">FinalResult</span><span class="p">[</span><span class="n">ResultDataT</span><span class="p">]]]:</span>
<span class="w">    </span><span class="sd">"""Provide async-iteration over the nodes in the agent run."""</span>
    <span class="k">return</span> <span class="bp">self</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.agent.AgentRun.__anext__" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">__anext__</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-async"><code>async</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_74"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_74 > code"></button><code><span class="fm">__anext__</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="p">(</span>
    <span class="nf"><span title="pydantic_ai._agent_graph.AgentNode">AgentNode</span></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.result.ResultDataT" href="../result/#pydantic_ai.result.ResultDataT">ResultDataT</a></span><span class="p">]</span>
    <span class="o">|</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.End" href="../pydantic_graph/nodes/#pydantic_graph.nodes.End">End</a></span><span class="p">[</span><span class="n"><span title="pydantic_ai.result.FinalResult">FinalResult</span></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.result.ResultDataT" href="../result/#pydantic_ai.result.ResultDataT">ResultDataT</a></span><span class="p">]]</span>
<span class="p">)</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Advance to the next node automatically based on the last returned node.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/agent.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">1410</span>
<span class="normal">1411</span>
<span class="normal">1412</span>
<span class="normal">1413</span>
<span class="normal">1414</span>
<span class="normal">1415</span>
<span class="normal">1416</span>
<span class="normal">1417</span>
<span class="normal">1418</span></pre></div></td><td class="code"><div><pre id="__code_75"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_75 > code"></button><code><span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="fm">__anext__</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">_agent_graph</span><span class="o">.</span><span class="n">AgentNode</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">,</span> <span class="n">ResultDataT</span><span class="p">]</span> <span class="o">|</span> <span class="n">End</span><span class="p">[</span><span class="n">FinalResult</span><span class="p">[</span><span class="n">ResultDataT</span><span class="p">]]:</span>
<span class="w">    </span><span class="sd">"""Advance to the next node automatically based on the last returned node."""</span>
    <span class="n">next_node</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_graph_run</span><span class="o">.</span><span class="fm">__anext__</span><span class="p">()</span>
    <span class="k">if</span> <span class="n">_agent_graph</span><span class="o">.</span><span class="n">is_agent_node</span><span class="p">(</span><span class="n">next_node</span><span class="p">):</span>
        <span class="k">return</span> <span class="n">next_node</span>
    <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">next_node</span><span class="p">,</span> <span class="n">End</span><span class="p">),</span> <span class="sa">f</span><span class="s1">'Unexpected node type: </span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="n">next_node</span><span class="p">)</span><span class="si">}</span><span class="s1">'</span>
    <span class="k">return</span> <span class="n">next_node</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.agent.AgentRun.next" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">next</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-async"><code>async</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_76"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_76 > code"></button><code><span class="nb">next</span><span class="p">(</span>
    <span class="nf">node</span><span class="p">:</span> <span class="n"><span title="pydantic_ai._agent_graph.AgentNode">AgentNode</span></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.result.ResultDataT" href="../result/#pydantic_ai.result.ResultDataT">ResultDataT</a></span><span class="p">],</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="p">(</span>
    <span class="n"><span title="pydantic_ai._agent_graph.AgentNode">AgentNode</span></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.result.ResultDataT" href="../result/#pydantic_ai.result.ResultDataT">ResultDataT</a></span><span class="p">]</span>
    <span class="o">|</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.End" href="../pydantic_graph/nodes/#pydantic_graph.nodes.End">End</a></span><span class="p">[</span><span class="n"><span title="pydantic_ai.result.FinalResult">FinalResult</span></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.result.ResultDataT" href="../result/#pydantic_ai.result.ResultDataT">ResultDataT</a></span><span class="p">]]</span>
<span class="p">)</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Manually drive the agent run by passing in the node you want to run next.</p>
<p>This lets you inspect or mutate the node before continuing execution, or skip certain nodes
under dynamic conditions. The agent run should be stopped when you return an <a class="autorefs autorefs-internal" href="../pydantic_graph/nodes/#pydantic_graph.nodes.End"><code>End</code></a>
node.</p>
<p>Example:
</p><div class="language-python highlight"><pre id="__code_77"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_77 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_graph</span><span class="w"> </span><span class="kn">import</span> <span class="n">End</span>

<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="s1">'openai:gpt-4o'</span><span class="p">)</span>

<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">main</span><span class="p">():</span>
    <span class="k">async</span> <span class="k">with</span> <span class="n">agent</span><span class="o">.</span><span class="n">iter</span><span class="p">(</span><span class="s1">'What is the capital of France?'</span><span class="p">)</span> <span class="k">as</span> <span class="n">agent_run</span><span class="p">:</span>
        <span class="n">next_node</span> <span class="o">=</span> <span class="n">agent_run</span><span class="o">.</span><span class="n">next_node</span>  <span class="c1"># start with the first node</span>
        <span class="n">nodes</span> <span class="o">=</span> <span class="p">[</span><span class="n">next_node</span><span class="p">]</span>
        <span class="k">while</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">next_node</span><span class="p">,</span> <span class="n">End</span><span class="p">):</span>
            <span class="n">next_node</span> <span class="o">=</span> <span class="k">await</span> <span class="n">agent_run</span><span class="o">.</span><span class="n">next</span><span class="p">(</span><span class="n">next_node</span><span class="p">)</span>
            <span class="n">nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">next_node</span><span class="p">)</span>
        <span class="c1"># Once `next_node` is an End, we've finished:</span>
        <span class="nb">print</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span>
<span class="w">        </span><span class="sd">'''</span>
<span class="sd">        [</span>
<span class="sd">            UserPromptNode(</span>
<span class="sd">                user_prompt='What is the capital of France?',</span>
<span class="sd">                system_prompts=(),</span>
<span class="sd">                system_prompt_functions=[],</span>
<span class="sd">                system_prompt_dynamic_functions={},</span>
<span class="sd">            ),</span>
<span class="sd">            ModelRequestNode(</span>
<span class="sd">                request=ModelRequest(</span>
<span class="sd">                    parts=[</span>
<span class="sd">                        UserPromptPart(</span>
<span class="sd">                            content='What is the capital of France?',</span>
<span class="sd">                            timestamp=datetime.datetime(...),</span>
<span class="sd">                            part_kind='user-prompt',</span>
<span class="sd">                        )</span>
<span class="sd">                    ],</span>
<span class="sd">                    kind='request',</span>
<span class="sd">                )</span>
<span class="sd">            ),</span>
<span class="sd">            CallToolsNode(</span>
<span class="sd">                model_response=ModelResponse(</span>
<span class="sd">                    parts=[TextPart(content='Paris', part_kind='text')],</span>
<span class="sd">                    model_name='gpt-4o',</span>
<span class="sd">                    timestamp=datetime.datetime(...),</span>
<span class="sd">                    kind='response',</span>
<span class="sd">                )</span>
<span class="sd">            ),</span>
<span class="sd">            End(data=FinalResult(data='Paris', tool_name=None, tool_call_id=None)),</span>
<span class="sd">        ]</span>
<span class="sd">        '''</span>
        <span class="nb">print</span><span class="p">(</span><span class="s1">'Final result:'</span><span class="p">,</span> <span class="n">agent_run</span><span class="o">.</span><span class="n">result</span><span class="o">.</span><span class="n">data</span><span class="p">)</span>
        <span class="c1">#&gt; Final result: Paris</span>
</code></pre></div><p></p>


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
                <code>node</code>
            </td>
            <td>
                  <code><span title="pydantic_ai._agent_graph.AgentNode">AgentNode</span>[<a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a>, <a class="autorefs autorefs-internal" title="pydantic_ai.result.ResultDataT" href="../result/#pydantic_ai.result.ResultDataT">ResultDataT</a>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The node to run next in the graph.</p>
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
                  <code><span title="pydantic_ai._agent_graph.AgentNode">AgentNode</span>[<a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a>, <a class="autorefs autorefs-internal" title="pydantic_ai.result.ResultDataT" href="../result/#pydantic_ai.result.ResultDataT">ResultDataT</a>] | <a class="autorefs autorefs-internal" title="pydantic_graph.End" href="../pydantic_graph/nodes/#pydantic_graph.nodes.End">End</a>[<span title="pydantic_ai.result.FinalResult">FinalResult</span>[<a class="autorefs autorefs-internal" title="pydantic_ai.result.ResultDataT" href="../result/#pydantic_ai.result.ResultDataT">ResultDataT</a>]]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The next node returned by the graph logic, or an <a class="autorefs autorefs-internal" href="../pydantic_graph/nodes/#pydantic_graph.nodes.End"><code>End</code></a> node if</p>
              </div>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                  <code><span title="pydantic_ai._agent_graph.AgentNode">AgentNode</span>[<a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a>, <a class="autorefs autorefs-internal" title="pydantic_ai.result.ResultDataT" href="../result/#pydantic_ai.result.ResultDataT">ResultDataT</a>] | <a class="autorefs autorefs-internal" title="pydantic_graph.End" href="../pydantic_graph/nodes/#pydantic_graph.nodes.End">End</a>[<span title="pydantic_ai.result.FinalResult">FinalResult</span>[<a class="autorefs autorefs-internal" title="pydantic_ai.result.ResultDataT" href="../result/#pydantic_ai.result.ResultDataT">ResultDataT</a>]]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>the run has completed.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/agent.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">1420</span>
<span class="normal">1421</span>
<span class="normal">1422</span>
<span class="normal">1423</span>
<span class="normal">1424</span>
<span class="normal">1425</span>
<span class="normal">1426</span>
<span class="normal">1427</span>
<span class="normal">1428</span>
<span class="normal">1429</span>
<span class="normal">1430</span>
<span class="normal">1431</span>
<span class="normal">1432</span>
<span class="normal">1433</span>
<span class="normal">1434</span>
<span class="normal">1435</span>
<span class="normal">1436</span>
<span class="normal">1437</span>
<span class="normal">1438</span>
<span class="normal">1439</span>
<span class="normal">1440</span>
<span class="normal">1441</span>
<span class="normal">1442</span>
<span class="normal">1443</span>
<span class="normal">1444</span>
<span class="normal">1445</span>
<span class="normal">1446</span>
<span class="normal">1447</span>
<span class="normal">1448</span>
<span class="normal">1449</span>
<span class="normal">1450</span>
<span class="normal">1451</span>
<span class="normal">1452</span>
<span class="normal">1453</span>
<span class="normal">1454</span>
<span class="normal">1455</span>
<span class="normal">1456</span>
<span class="normal">1457</span>
<span class="normal">1458</span>
<span class="normal">1459</span>
<span class="normal">1460</span>
<span class="normal">1461</span>
<span class="normal">1462</span>
<span class="normal">1463</span>
<span class="normal">1464</span>
<span class="normal">1465</span>
<span class="normal">1466</span>
<span class="normal">1467</span>
<span class="normal">1468</span>
<span class="normal">1469</span>
<span class="normal">1470</span>
<span class="normal">1471</span>
<span class="normal">1472</span>
<span class="normal">1473</span>
<span class="normal">1474</span>
<span class="normal">1475</span>
<span class="normal">1476</span>
<span class="normal">1477</span>
<span class="normal">1478</span>
<span class="normal">1479</span>
<span class="normal">1480</span>
<span class="normal">1481</span>
<span class="normal">1482</span>
<span class="normal">1483</span>
<span class="normal">1484</span>
<span class="normal">1485</span>
<span class="normal">1486</span>
<span class="normal">1487</span>
<span class="normal">1488</span>
<span class="normal">1489</span>
<span class="normal">1490</span>
<span class="normal">1491</span>
<span class="normal">1492</span>
<span class="normal">1493</span>
<span class="normal">1494</span></pre></div></td><td class="code"><div><pre id="__code_78"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_78 > code"></button><code tabindex="0"><span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">next</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">node</span><span class="p">:</span> <span class="n">_agent_graph</span><span class="o">.</span><span class="n">AgentNode</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">,</span> <span class="n">ResultDataT</span><span class="p">],</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">_agent_graph</span><span class="o">.</span><span class="n">AgentNode</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">,</span> <span class="n">ResultDataT</span><span class="p">]</span> <span class="o">|</span> <span class="n">End</span><span class="p">[</span><span class="n">FinalResult</span><span class="p">[</span><span class="n">ResultDataT</span><span class="p">]]:</span>
<span class="w">    </span><span class="sd">"""Manually drive the agent run by passing in the node you want to run next.</span>

<span class="sd">    This lets you inspect or mutate the node before continuing execution, or skip certain nodes</span>
<span class="sd">    under dynamic conditions. The agent run should be stopped when you return an [`End`][pydantic_graph.nodes.End]</span>
<span class="sd">    node.</span>

<span class="sd">    Example:</span>
<span class="sd">    ```python</span>
<span class="sd">    from pydantic_ai import Agent</span>
<span class="sd">    from pydantic_graph import End</span>

<span class="sd">    agent = Agent('openai:gpt-4o')</span>

<span class="sd">    async def main():</span>
<span class="sd">        async with agent.iter('What is the capital of France?') as agent_run:</span>
<span class="sd">            next_node = agent_run.next_node  # start with the first node</span>
<span class="sd">            nodes = [next_node]</span>
<span class="sd">            while not isinstance(next_node, End):</span>
<span class="sd">                next_node = await agent_run.next(next_node)</span>
<span class="sd">                nodes.append(next_node)</span>
<span class="sd">            # Once `next_node` is an End, we've finished:</span>
<span class="sd">            print(nodes)</span>
<span class="sd">            '''</span>
<span class="sd">            [</span>
<span class="sd">                UserPromptNode(</span>
<span class="sd">                    user_prompt='What is the capital of France?',</span>
<span class="sd">                    system_prompts=(),</span>
<span class="sd">                    system_prompt_functions=[],</span>
<span class="sd">                    system_prompt_dynamic_functions={},</span>
<span class="sd">                ),</span>
<span class="sd">                ModelRequestNode(</span>
<span class="sd">                    request=ModelRequest(</span>
<span class="sd">                        parts=[</span>
<span class="sd">                            UserPromptPart(</span>
<span class="sd">                                content='What is the capital of France?',</span>
<span class="sd">                                timestamp=datetime.datetime(...),</span>
<span class="sd">                                part_kind='user-prompt',</span>
<span class="sd">                            )</span>
<span class="sd">                        ],</span>
<span class="sd">                        kind='request',</span>
<span class="sd">                    )</span>
<span class="sd">                ),</span>
<span class="sd">                CallToolsNode(</span>
<span class="sd">                    model_response=ModelResponse(</span>
<span class="sd">                        parts=[TextPart(content='Paris', part_kind='text')],</span>
<span class="sd">                        model_name='gpt-4o',</span>
<span class="sd">                        timestamp=datetime.datetime(...),</span>
<span class="sd">                        kind='response',</span>
<span class="sd">                    )</span>
<span class="sd">                ),</span>
<span class="sd">                End(data=FinalResult(data='Paris', tool_name=None, tool_call_id=None)),</span>
<span class="sd">            ]</span>
<span class="sd">            '''</span>
<span class="sd">            print('Final result:', agent_run.result.data)</span>
<span class="sd">            #&gt; Final result: Paris</span>
<span class="sd">    ```</span>

<span class="sd">    Args:</span>
<span class="sd">        node: The node to run next in the graph.</span>

<span class="sd">    Returns:</span>
<span class="sd">        The next node returned by the graph logic, or an [`End`][pydantic_graph.nodes.End] node if</span>
<span class="sd">        the run has completed.</span>
<span class="sd">    """</span>
    <span class="c1"># Note: It might be nice to expose a synchronous interface for iteration, but we shouldn't do it</span>
    <span class="c1"># on this class, or else IDEs won't warn you if you accidentally use `for` instead of `async for` to iterate.</span>
    <span class="n">next_node</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_graph_run</span><span class="o">.</span><span class="n">next</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">_agent_graph</span><span class="o">.</span><span class="n">is_agent_node</span><span class="p">(</span><span class="n">next_node</span><span class="p">):</span>
        <span class="k">return</span> <span class="n">next_node</span>
    <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">next_node</span><span class="p">,</span> <span class="n">End</span><span class="p">),</span> <span class="sa">f</span><span class="s1">'Unexpected node type: </span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="n">next_node</span><span class="p">)</span><span class="si">}</span><span class="s1">'</span>
    <span class="k">return</span> <span class="n">next_node</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.agent.AgentRun.usage" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">usage</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_79"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_79 > code"></button><code><span class="nf">usage</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.usage.Usage" href="../usage/#pydantic_ai.usage.Usage">Usage</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Get usage statistics for the run so far, including token usage, model requests, and so on.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/agent.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">1496</span>
<span class="normal">1497</span>
<span class="normal">1498</span></pre></div></td><td class="code"><div><pre id="__code_80"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_80 > code"></button><code><span class="k">def</span><span class="w"> </span><span class="nf">usage</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">_usage</span><span class="o">.</span><span class="n">Usage</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Get usage statistics for the run so far, including token usage, model requests, and so on."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_graph_run</span><span class="o">.</span><span class="n">state</span><span class="o">.</span><span class="n">usage</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>




  </div>

    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_ai.agent.AgentRunResult" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">AgentRunResult</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">
            <p class="doc doc-class-bases">
              Bases: <code><a class="autorefs autorefs-external" title="typing.Generic" href="https://docs.python.org/3/library/typing.html#typing.Generic">Generic</a>[<a class="autorefs autorefs-internal" title="pydantic_ai.result.ResultDataT" href="../result/#pydantic_ai.result.ResultDataT">ResultDataT</a>]</code></p>


        <p>The final result of an agent run.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/agent.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">1506</span>
<span class="normal">1507</span>
<span class="normal">1508</span>
<span class="normal">1509</span>
<span class="normal">1510</span>
<span class="normal">1511</span>
<span class="normal">1512</span>
<span class="normal">1513</span>
<span class="normal">1514</span>
<span class="normal">1515</span>
<span class="normal">1516</span>
<span class="normal">1517</span>
<span class="normal">1518</span>
<span class="normal">1519</span>
<span class="normal">1520</span>
<span class="normal">1521</span>
<span class="normal">1522</span>
<span class="normal">1523</span>
<span class="normal">1524</span>
<span class="normal">1525</span>
<span class="normal">1526</span>
<span class="normal">1527</span>
<span class="normal">1528</span>
<span class="normal">1529</span>
<span class="normal">1530</span>
<span class="normal">1531</span>
<span class="normal">1532</span>
<span class="normal">1533</span>
<span class="normal">1534</span>
<span class="normal">1535</span>
<span class="normal">1536</span>
<span class="normal">1537</span>
<span class="normal">1538</span>
<span class="normal">1539</span>
<span class="normal">1540</span>
<span class="normal">1541</span>
<span class="normal">1542</span>
<span class="normal">1543</span>
<span class="normal">1544</span>
<span class="normal">1545</span>
<span class="normal">1546</span>
<span class="normal">1547</span>
<span class="normal">1548</span>
<span class="normal">1549</span>
<span class="normal">1550</span>
<span class="normal">1551</span>
<span class="normal">1552</span>
<span class="normal">1553</span>
<span class="normal">1554</span>
<span class="normal">1555</span>
<span class="normal">1556</span>
<span class="normal">1557</span>
<span class="normal">1558</span>
<span class="normal">1559</span>
<span class="normal">1560</span>
<span class="normal">1561</span>
<span class="normal">1562</span>
<span class="normal">1563</span>
<span class="normal">1564</span>
<span class="normal">1565</span>
<span class="normal">1566</span>
<span class="normal">1567</span>
<span class="normal">1568</span>
<span class="normal">1569</span>
<span class="normal">1570</span>
<span class="normal">1571</span>
<span class="normal">1572</span>
<span class="normal">1573</span>
<span class="normal">1574</span>
<span class="normal">1575</span>
<span class="normal">1576</span>
<span class="normal">1577</span>
<span class="normal">1578</span>
<span class="normal">1579</span>
<span class="normal">1580</span>
<span class="normal">1581</span>
<span class="normal">1582</span>
<span class="normal">1583</span>
<span class="normal">1584</span>
<span class="normal">1585</span>
<span class="normal">1586</span>
<span class="normal">1587</span>
<span class="normal">1588</span>
<span class="normal">1589</span>
<span class="normal">1590</span>
<span class="normal">1591</span>
<span class="normal">1592</span>
<span class="normal">1593</span>
<span class="normal">1594</span>
<span class="normal">1595</span>
<span class="normal">1596</span>
<span class="normal">1597</span>
<span class="normal">1598</span></pre></div></td><td class="code"><div><pre id="__code_81"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_81 > code"></button><code tabindex="0"><span class="nd">@dataclasses</span><span class="o">.</span><span class="n">dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">AgentRunResult</span><span class="p">(</span><span class="n">Generic</span><span class="p">[</span><span class="n">ResultDataT</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""The final result of an agent run."""</span>

    <span class="n">data</span><span class="p">:</span> <span class="n">ResultDataT</span>  <span class="c1"># TODO: rename this to output. I'm putting this off for now mostly to reduce the size of the diff</span>

    <span class="n">_result_tool_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="n">dataclasses</span><span class="o">.</span><span class="n">field</span><span class="p">(</span><span class="nb">repr</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
    <span class="n">_state</span><span class="p">:</span> <span class="n">_agent_graph</span><span class="o">.</span><span class="n">GraphAgentState</span> <span class="o">=</span> <span class="n">dataclasses</span><span class="o">.</span><span class="n">field</span><span class="p">(</span><span class="nb">repr</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
    <span class="n">_new_message_index</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">dataclasses</span><span class="o">.</span><span class="n">field</span><span class="p">(</span><span class="nb">repr</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">_set_result_tool_return</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">return_content</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">list</span><span class="p">[</span><span class="n">_messages</span><span class="o">.</span><span class="n">ModelMessage</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Set return content for the result tool.</span>

<span class="sd">        Useful if you want to continue the conversation and want to set the response to the result tool call.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_result_tool_name</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s1">'Cannot set result tool return content when the return type is `str`.'</span><span class="p">)</span>
        <span class="n">messages</span> <span class="o">=</span> <span class="n">deepcopy</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_state</span><span class="o">.</span><span class="n">message_history</span><span class="p">)</span>
        <span class="n">last_message</span> <span class="o">=</span> <span class="n">messages</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>
        <span class="k">for</span> <span class="n">part</span> <span class="ow">in</span> <span class="n">last_message</span><span class="o">.</span><span class="n">parts</span><span class="p">:</span>
            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">part</span><span class="p">,</span> <span class="n">_messages</span><span class="o">.</span><span class="n">ToolReturnPart</span><span class="p">)</span> <span class="ow">and</span> <span class="n">part</span><span class="o">.</span><span class="n">tool_name</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">_result_tool_name</span><span class="p">:</span>
                <span class="n">part</span><span class="o">.</span><span class="n">content</span> <span class="o">=</span> <span class="n">return_content</span>
                <span class="k">return</span> <span class="n">messages</span>
        <span class="k">raise</span> <span class="ne">LookupError</span><span class="p">(</span><span class="sa">f</span><span class="s1">'No tool call found with tool name </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_result_tool_name</span><span class="si">!r}</span><span class="s1">.'</span><span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">all_messages</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">result_tool_return_content</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">list</span><span class="p">[</span><span class="n">_messages</span><span class="o">.</span><span class="n">ModelMessage</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Return the history of _messages.</span>

<span class="sd">        Args:</span>
<span class="sd">            result_tool_return_content: The return content of the tool call to set in the last message.</span>
<span class="sd">                This provides a convenient way to modify the content of the result tool call if you want to continue</span>
<span class="sd">                the conversation and want to set the response to the result tool call. If `None`, the last message will</span>
<span class="sd">                not be modified.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List of messages.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">result_tool_return_content</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_set_result_tool_return</span><span class="p">(</span><span class="n">result_tool_return_content</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_state</span><span class="o">.</span><span class="n">message_history</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">all_messages_json</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">result_tool_return_content</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bytes</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Return all messages from [`all_messages`][pydantic_ai.agent.AgentRunResult.all_messages] as JSON bytes.</span>

<span class="sd">        Args:</span>
<span class="sd">            result_tool_return_content: The return content of the tool call to set in the last message.</span>
<span class="sd">                This provides a convenient way to modify the content of the result tool call if you want to continue</span>
<span class="sd">                the conversation and want to set the response to the result tool call. If `None`, the last message will</span>
<span class="sd">                not be modified.</span>

<span class="sd">        Returns:</span>
<span class="sd">            JSON bytes representing the messages.</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="n">_messages</span><span class="o">.</span><span class="n">ModelMessagesTypeAdapter</span><span class="o">.</span><span class="n">dump_json</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">all_messages</span><span class="p">(</span><span class="n">result_tool_return_content</span><span class="o">=</span><span class="n">result_tool_return_content</span><span class="p">)</span>
        <span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">new_messages</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">result_tool_return_content</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">list</span><span class="p">[</span><span class="n">_messages</span><span class="o">.</span><span class="n">ModelMessage</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Return new messages associated with this run.</span>

<span class="sd">        Messages from older runs are excluded.</span>

<span class="sd">        Args:</span>
<span class="sd">            result_tool_return_content: The return content of the tool call to set in the last message.</span>
<span class="sd">                This provides a convenient way to modify the content of the result tool call if you want to continue</span>
<span class="sd">                the conversation and want to set the response to the result tool call. If `None`, the last message will</span>
<span class="sd">                not be modified.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List of new messages.</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">all_messages</span><span class="p">(</span><span class="n">result_tool_return_content</span><span class="o">=</span><span class="n">result_tool_return_content</span><span class="p">)[</span><span class="bp">self</span><span class="o">.</span><span class="n">_new_message_index</span> <span class="p">:]</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">new_messages_json</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">result_tool_return_content</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bytes</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Return new messages from [`new_messages`][pydantic_ai.agent.AgentRunResult.new_messages] as JSON bytes.</span>

<span class="sd">        Args:</span>
<span class="sd">            result_tool_return_content: The return content of the tool call to set in the last message.</span>
<span class="sd">                This provides a convenient way to modify the content of the result tool call if you want to continue</span>
<span class="sd">                the conversation and want to set the response to the result tool call. If `None`, the last message will</span>
<span class="sd">                not be modified.</span>

<span class="sd">        Returns:</span>
<span class="sd">            JSON bytes representing the new messages.</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="n">_messages</span><span class="o">.</span><span class="n">ModelMessagesTypeAdapter</span><span class="o">.</span><span class="n">dump_json</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">new_messages</span><span class="p">(</span><span class="n">result_tool_return_content</span><span class="o">=</span><span class="n">result_tool_return_content</span><span class="p">)</span>
        <span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">usage</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">_usage</span><span class="o">.</span><span class="n">Usage</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Return the usage of the whole run."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_state</span><span class="o">.</span><span class="n">usage</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">











<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.agent.AgentRunResult.all_messages" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">all_messages</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_82"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_82 > code"></button><code><span class="nf">all_messages</span><span class="p">(</span>
    <span class="o">*</span><span class="p">,</span> <span class="n">result_tool_return_content</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list">list</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ModelMessage" href="../messages/#pydantic_ai.messages.ModelMessage">ModelMessage</a></span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Return the history of _messages.</p>


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
                <code>result_tool_return_content</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The return content of the tool call to set in the last message.
This provides a convenient way to modify the content of the result tool call if you want to continue
the conversation and want to set the response to the result tool call. If <code>None</code>, the last message will
not be modified.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
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
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list">list</a>[<a class="autorefs autorefs-internal" title="pydantic_ai.messages.ModelMessage" href="../messages/#pydantic_ai.messages.ModelMessage">ModelMessage</a>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>List of messages.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/agent.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">1531</span>
<span class="normal">1532</span>
<span class="normal">1533</span>
<span class="normal">1534</span>
<span class="normal">1535</span>
<span class="normal">1536</span>
<span class="normal">1537</span>
<span class="normal">1538</span>
<span class="normal">1539</span>
<span class="normal">1540</span>
<span class="normal">1541</span>
<span class="normal">1542</span>
<span class="normal">1543</span>
<span class="normal">1544</span>
<span class="normal">1545</span>
<span class="normal">1546</span></pre></div></td><td class="code"><div><pre id="__code_83"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_83 > code"></button><code tabindex="0"><span class="k">def</span><span class="w"> </span><span class="nf">all_messages</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">result_tool_return_content</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">list</span><span class="p">[</span><span class="n">_messages</span><span class="o">.</span><span class="n">ModelMessage</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Return the history of _messages.</span>

<span class="sd">    Args:</span>
<span class="sd">        result_tool_return_content: The return content of the tool call to set in the last message.</span>
<span class="sd">            This provides a convenient way to modify the content of the result tool call if you want to continue</span>
<span class="sd">            the conversation and want to set the response to the result tool call. If `None`, the last message will</span>
<span class="sd">            not be modified.</span>

<span class="sd">    Returns:</span>
<span class="sd">        List of messages.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="n">result_tool_return_content</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_set_result_tool_return</span><span class="p">(</span><span class="n">result_tool_return_content</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_state</span><span class="o">.</span><span class="n">message_history</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.agent.AgentRunResult.all_messages_json" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">all_messages_json</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_84"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_84 > code"></button><code><span class="nf">all_messages_json</span><span class="p">(</span>
    <span class="o">*</span><span class="p">,</span> <span class="n">result_tool_return_content</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#bytes">bytes</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Return all messages from <a class="autorefs autorefs-internal" href="#pydantic_ai.agent.AgentRunResult.all_messages"><code>all_messages</code></a> as JSON bytes.</p>


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
                <code>result_tool_return_content</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The return content of the tool call to set in the last message.
This provides a convenient way to modify the content of the result tool call if you want to continue
the conversation and want to set the response to the result tool call. If <code>None</code>, the last message will
not be modified.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
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
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#bytes">bytes</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>JSON bytes representing the messages.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/agent.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">1548</span>
<span class="normal">1549</span>
<span class="normal">1550</span>
<span class="normal">1551</span>
<span class="normal">1552</span>
<span class="normal">1553</span>
<span class="normal">1554</span>
<span class="normal">1555</span>
<span class="normal">1556</span>
<span class="normal">1557</span>
<span class="normal">1558</span>
<span class="normal">1559</span>
<span class="normal">1560</span>
<span class="normal">1561</span>
<span class="normal">1562</span></pre></div></td><td class="code"><div><pre id="__code_85"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_85 > code"></button><code tabindex="0"><span class="k">def</span><span class="w"> </span><span class="nf">all_messages_json</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">result_tool_return_content</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bytes</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Return all messages from [`all_messages`][pydantic_ai.agent.AgentRunResult.all_messages] as JSON bytes.</span>

<span class="sd">    Args:</span>
<span class="sd">        result_tool_return_content: The return content of the tool call to set in the last message.</span>
<span class="sd">            This provides a convenient way to modify the content of the result tool call if you want to continue</span>
<span class="sd">            the conversation and want to set the response to the result tool call. If `None`, the last message will</span>
<span class="sd">            not be modified.</span>

<span class="sd">    Returns:</span>
<span class="sd">        JSON bytes representing the messages.</span>
<span class="sd">    """</span>
    <span class="k">return</span> <span class="n">_messages</span><span class="o">.</span><span class="n">ModelMessagesTypeAdapter</span><span class="o">.</span><span class="n">dump_json</span><span class="p">(</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">all_messages</span><span class="p">(</span><span class="n">result_tool_return_content</span><span class="o">=</span><span class="n">result_tool_return_content</span><span class="p">)</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.agent.AgentRunResult.new_messages" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">new_messages</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_86"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_86 > code"></button><code><span class="nf">new_messages</span><span class="p">(</span>
    <span class="o">*</span><span class="p">,</span> <span class="n">result_tool_return_content</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list">list</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ModelMessage" href="../messages/#pydantic_ai.messages.ModelMessage">ModelMessage</a></span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Return new messages associated with this run.</p>
<p>Messages from older runs are excluded.</p>


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
                <code>result_tool_return_content</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The return content of the tool call to set in the last message.
This provides a convenient way to modify the content of the result tool call if you want to continue
the conversation and want to set the response to the result tool call. If <code>None</code>, the last message will
not be modified.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
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
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list">list</a>[<a class="autorefs autorefs-internal" title="pydantic_ai.messages.ModelMessage" href="../messages/#pydantic_ai.messages.ModelMessage">ModelMessage</a>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>List of new messages.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/agent.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">1564</span>
<span class="normal">1565</span>
<span class="normal">1566</span>
<span class="normal">1567</span>
<span class="normal">1568</span>
<span class="normal">1569</span>
<span class="normal">1570</span>
<span class="normal">1571</span>
<span class="normal">1572</span>
<span class="normal">1573</span>
<span class="normal">1574</span>
<span class="normal">1575</span>
<span class="normal">1576</span>
<span class="normal">1577</span>
<span class="normal">1578</span></pre></div></td><td class="code"><div><pre id="__code_87"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_87 > code"></button><code tabindex="0"><span class="k">def</span><span class="w"> </span><span class="nf">new_messages</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">result_tool_return_content</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">list</span><span class="p">[</span><span class="n">_messages</span><span class="o">.</span><span class="n">ModelMessage</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Return new messages associated with this run.</span>

<span class="sd">    Messages from older runs are excluded.</span>

<span class="sd">    Args:</span>
<span class="sd">        result_tool_return_content: The return content of the tool call to set in the last message.</span>
<span class="sd">            This provides a convenient way to modify the content of the result tool call if you want to continue</span>
<span class="sd">            the conversation and want to set the response to the result tool call. If `None`, the last message will</span>
<span class="sd">            not be modified.</span>

<span class="sd">    Returns:</span>
<span class="sd">        List of new messages.</span>
<span class="sd">    """</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">all_messages</span><span class="p">(</span><span class="n">result_tool_return_content</span><span class="o">=</span><span class="n">result_tool_return_content</span><span class="p">)[</span><span class="bp">self</span><span class="o">.</span><span class="n">_new_message_index</span> <span class="p">:]</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.agent.AgentRunResult.new_messages_json" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">new_messages_json</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_88"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_88 > code"></button><code><span class="nf">new_messages_json</span><span class="p">(</span>
    <span class="o">*</span><span class="p">,</span> <span class="n">result_tool_return_content</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#bytes">bytes</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Return new messages from <a class="autorefs autorefs-internal" href="#pydantic_ai.agent.AgentRunResult.new_messages"><code>new_messages</code></a> as JSON bytes.</p>


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
                <code>result_tool_return_content</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The return content of the tool call to set in the last message.
This provides a convenient way to modify the content of the result tool call if you want to continue
the conversation and want to set the response to the result tool call. If <code>None</code>, the last message will
not be modified.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
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
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#bytes">bytes</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>JSON bytes representing the new messages.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/agent.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">1580</span>
<span class="normal">1581</span>
<span class="normal">1582</span>
<span class="normal">1583</span>
<span class="normal">1584</span>
<span class="normal">1585</span>
<span class="normal">1586</span>
<span class="normal">1587</span>
<span class="normal">1588</span>
<span class="normal">1589</span>
<span class="normal">1590</span>
<span class="normal">1591</span>
<span class="normal">1592</span>
<span class="normal">1593</span>
<span class="normal">1594</span></pre></div></td><td class="code"><div><pre id="__code_89"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_89 > code"></button><code tabindex="0"><span class="k">def</span><span class="w"> </span><span class="nf">new_messages_json</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">result_tool_return_content</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bytes</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Return new messages from [`new_messages`][pydantic_ai.agent.AgentRunResult.new_messages] as JSON bytes.</span>

<span class="sd">    Args:</span>
<span class="sd">        result_tool_return_content: The return content of the tool call to set in the last message.</span>
<span class="sd">            This provides a convenient way to modify the content of the result tool call if you want to continue</span>
<span class="sd">            the conversation and want to set the response to the result tool call. If `None`, the last message will</span>
<span class="sd">            not be modified.</span>

<span class="sd">    Returns:</span>
<span class="sd">        JSON bytes representing the new messages.</span>
<span class="sd">    """</span>
    <span class="k">return</span> <span class="n">_messages</span><span class="o">.</span><span class="n">ModelMessagesTypeAdapter</span><span class="o">.</span><span class="n">dump_json</span><span class="p">(</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">new_messages</span><span class="p">(</span><span class="n">result_tool_return_content</span><span class="o">=</span><span class="n">result_tool_return_content</span><span class="p">)</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.agent.AgentRunResult.usage" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">usage</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_90"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_90 > code"></button><code><span class="nf">usage</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.usage.Usage" href="../usage/#pydantic_ai.usage.Usage">Usage</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Return the usage of the whole run.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/agent.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">1596</span>
<span class="normal">1597</span>
<span class="normal">1598</span></pre></div></td><td class="code"><div><pre id="__code_91"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_91 > code"></button><code><span class="k">def</span><span class="w"> </span><span class="nf">usage</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">_usage</span><span class="o">.</span><span class="n">Usage</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Return the usage of the whole run."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_state</span><span class="o">.</span><span class="n">usage</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>




  </div>

    </div>

</div>






<div class="doc doc-object doc-attribute">



<h3 id="pydantic_ai.agent.EndStrategy" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">EndStrategy</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span>

</h3>
<div class="language-python doc-signature highlight"><pre id="__code_92"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_92 > code"></button><code><span class="n">EndStrategy</span> <span class="o">=</span> <span class="n"><span title="pydantic_ai._agent_graph.EndStrategy">EndStrategy</span></span>
</code></pre></div>

    <div class="doc doc-contents ">
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h3 id="pydantic_ai.agent.RunResultDataT" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">RunResultDataT</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span>

</h3>
<div class="language-python doc-signature highlight"><pre id="__code_93"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_93 > code"></button><code><span class="n">RunResultDataT</span> <span class="o">=</span> <span class="n"><span title="typing_extensions.TypeVar">TypeVar</span></span><span class="p">(</span><span class="s1">'RunResultDataT'</span><span class="p">)</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Type variable for the result data of a run where <code>result_type</code> was customized on the run call.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h3 id="pydantic_ai.agent.capture_run_messages" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">capture_run_messages</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span>

</h3>
<div class="language-python doc-signature highlight"><pre id="__code_94"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_94 > code"></button><code><span class="n">capture_run_messages</span> <span class="o">=</span> <span class="n"><span title="pydantic_ai._agent_graph.capture_run_messages">capture_run_messages</span></span>
</code></pre></div>

    <div class="doc doc-contents ">
    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_ai.agent.InstrumentationSettings" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">InstrumentationSettings</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">


        <p>Options for instrumenting models and agents with OpenTelemetry.</p>
<p>Used in:</p>
<ul>
<li><code>Agent(instrument=...)</code></li>
<li><a class="autorefs autorefs-internal" href="#pydantic_ai.agent.Agent.instrument_all"><code>Agent.instrument_all()</code></a></li>
<li><a class="autorefs autorefs-internal" href="../models/instrumented/#pydantic_ai.models.instrumented.InstrumentedModel"><code>InstrumentedModel</code></a></li>
</ul>
<p>See the <a href="https://ai.pydantic.dev/logfire/">Debugging and Monitoring guide</a> for more info.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/models/instrumented.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">52</span>
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
<span class="normal">95</span></pre></div></td><td class="code"><div><pre id="__code_95"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_95 > code"></button><code tabindex="0"><span class="nd">@dataclass</span><span class="p">(</span><span class="n">init</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
<span class="k">class</span><span class="w"> </span><span class="nc">InstrumentationSettings</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Options for instrumenting models and agents with OpenTelemetry.</span>

<span class="sd">    Used in:</span>

<span class="sd">    - `Agent(instrument=...)`</span>
<span class="sd">    - [`Agent.instrument_all()`][pydantic_ai.agent.Agent.instrument_all]</span>
<span class="sd">    - [`InstrumentedModel`][pydantic_ai.models.instrumented.InstrumentedModel]</span>

<span class="sd">    See the [Debugging and Monitoring guide](https://ai.pydantic.dev/logfire/) for more info.</span>
<span class="sd">    """</span>

    <span class="n">tracer</span><span class="p">:</span> <span class="n">Tracer</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span><span class="nb">repr</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
    <span class="n">event_logger</span><span class="p">:</span> <span class="n">EventLogger</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span><span class="nb">repr</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
    <span class="n">event_mode</span><span class="p">:</span> <span class="n">Literal</span><span class="p">[</span><span class="s1">'attributes'</span><span class="p">,</span> <span class="s1">'logs'</span><span class="p">]</span> <span class="o">=</span> <span class="s1">'attributes'</span>

    <span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="o">*</span><span class="p">,</span>
        <span class="n">event_mode</span><span class="p">:</span> <span class="n">Literal</span><span class="p">[</span><span class="s1">'attributes'</span><span class="p">,</span> <span class="s1">'logs'</span><span class="p">]</span> <span class="o">=</span> <span class="s1">'attributes'</span><span class="p">,</span>
        <span class="n">tracer_provider</span><span class="p">:</span> <span class="n">TracerProvider</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">event_logger_provider</span><span class="p">:</span> <span class="n">EventLoggerProvider</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">):</span>
<span class="w">        </span><span class="sd">"""Create instrumentation options.</span>

<span class="sd">        Args:</span>
<span class="sd">            event_mode: The mode for emitting events. If `'attributes'`, events are attached to the span as attributes.</span>
<span class="sd">                If `'logs'`, events are emitted as OpenTelemetry log-based events.</span>
<span class="sd">            tracer_provider: The OpenTelemetry tracer provider to use.</span>
<span class="sd">                If not provided, the global tracer provider is used.</span>
<span class="sd">                Calling `logfire.configure()` sets the global tracer provider, so most users don't need this.</span>
<span class="sd">            event_logger_provider: The OpenTelemetry event logger provider to use.</span>
<span class="sd">                If not provided, the global event logger provider is used.</span>
<span class="sd">                Calling `logfire.configure()` sets the global event logger provider, so most users don't need this.</span>
<span class="sd">                This is only used if `event_mode='logs'`.</span>
<span class="sd">        """</span>
        <span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">__version__</span>

        <span class="n">tracer_provider</span> <span class="o">=</span> <span class="n">tracer_provider</span> <span class="ow">or</span> <span class="n">get_tracer_provider</span><span class="p">()</span>
        <span class="n">event_logger_provider</span> <span class="o">=</span> <span class="n">event_logger_provider</span> <span class="ow">or</span> <span class="n">get_event_logger_provider</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">tracer</span> <span class="o">=</span> <span class="n">tracer_provider</span><span class="o">.</span><span class="n">get_tracer</span><span class="p">(</span><span class="s1">'pydantic-ai'</span><span class="p">,</span> <span class="n">__version__</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">event_logger</span> <span class="o">=</span> <span class="n">event_logger_provider</span><span class="o">.</span><span class="n">get_event_logger</span><span class="p">(</span><span class="s1">'pydantic-ai'</span><span class="p">,</span> <span class="n">__version__</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">event_mode</span> <span class="o">=</span> <span class="n">event_mode</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.agent.InstrumentationSettings.__init__" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">__init__</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_96"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_96 > code"></button><code><span class="fm">__init__</span><span class="p">(</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="nf">event_mode</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Literal" href="https://docs.python.org/3/library/typing.html#typing.Literal">Literal</a></span><span class="p">[</span>
        <span class="s2">"attributes"</span><span class="p">,</span> <span class="s2">"logs"</span>
    <span class="p">]</span> <span class="o">=</span> <span class="s2">"attributes"</span><span class="p">,</span>
    <span class="n">tracer_provider</span><span class="p">:</span> <span class="n"><span title="opentelemetry.trace.TracerProvider">TracerProvider</span></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">event_logger_provider</span><span class="p">:</span> <span class="n"><span title="opentelemetry._events.EventLoggerProvider">EventLoggerProvider</span></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Create instrumentation options.</p>


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
                <code>event_mode</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" title="typing.Literal" href="https://docs.python.org/3/library/typing.html#typing.Literal">Literal</a>['attributes', 'logs']</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The mode for emitting events. If <code>'attributes'</code>, events are attached to the span as attributes.
If <code>'logs'</code>, events are emitted as OpenTelemetry log-based events.</p>
              </div>
            </td>
            <td>
                  <code>'attributes'</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>tracer_provider</code>
            </td>
            <td>
                  <code><span title="opentelemetry.trace.TracerProvider">TracerProvider</span> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The OpenTelemetry tracer provider to use.
If not provided, the global tracer provider is used.
Calling <code>logfire.configure()</code> sets the global tracer provider, so most users don't need this.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>event_logger_provider</code>
            </td>
            <td>
                  <code><span title="opentelemetry._events.EventLoggerProvider">EventLoggerProvider</span> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The OpenTelemetry event logger provider to use.
If not provided, the global event logger provider is used.
Calling <code>logfire.configure()</code> sets the global event logger provider, so most users don't need this.
This is only used if <code>event_mode='logs'</code>.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/models/instrumented.py</code></summary>
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
<span class="normal">95</span></pre></div></td><td class="code"><div><pre id="__code_97"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_97 > code"></button><code tabindex="0"><span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">event_mode</span><span class="p">:</span> <span class="n">Literal</span><span class="p">[</span><span class="s1">'attributes'</span><span class="p">,</span> <span class="s1">'logs'</span><span class="p">]</span> <span class="o">=</span> <span class="s1">'attributes'</span><span class="p">,</span>
    <span class="n">tracer_provider</span><span class="p">:</span> <span class="n">TracerProvider</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">event_logger_provider</span><span class="p">:</span> <span class="n">EventLoggerProvider</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">):</span>
<span class="w">    </span><span class="sd">"""Create instrumentation options.</span>

<span class="sd">    Args:</span>
<span class="sd">        event_mode: The mode for emitting events. If `'attributes'`, events are attached to the span as attributes.</span>
<span class="sd">            If `'logs'`, events are emitted as OpenTelemetry log-based events.</span>
<span class="sd">        tracer_provider: The OpenTelemetry tracer provider to use.</span>
<span class="sd">            If not provided, the global tracer provider is used.</span>
<span class="sd">            Calling `logfire.configure()` sets the global tracer provider, so most users don't need this.</span>
<span class="sd">        event_logger_provider: The OpenTelemetry event logger provider to use.</span>
<span class="sd">            If not provided, the global event logger provider is used.</span>
<span class="sd">            Calling `logfire.configure()` sets the global event logger provider, so most users don't need this.</span>
<span class="sd">            This is only used if `event_mode='logs'`.</span>
<span class="sd">    """</span>
    <span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">__version__</span>

    <span class="n">tracer_provider</span> <span class="o">=</span> <span class="n">tracer_provider</span> <span class="ow">or</span> <span class="n">get_tracer_provider</span><span class="p">()</span>
    <span class="n">event_logger_provider</span> <span class="o">=</span> <span class="n">event_logger_provider</span> <span class="ow">or</span> <span class="n">get_event_logger_provider</span><span class="p">()</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">tracer</span> <span class="o">=</span> <span class="n">tracer_provider</span><span class="o">.</span><span class="n">get_tracer</span><span class="p">(</span><span class="s1">'pydantic-ai'</span><span class="p">,</span> <span class="n">__version__</span><span class="p">)</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">event_logger</span> <span class="o">=</span> <span class="n">event_logger_provider</span><span class="o">.</span><span class="n">get_event_logger</span><span class="p">(</span><span class="s1">'pydantic-ai'</span><span class="p">,</span> <span class="n">__version__</span><span class="p">)</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">event_mode</span> <span class="o">=</span> <span class="n">event_mode</span>
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